// ===== CREDENTIALS =====
const CREDENTIALS = {
    recruiter: {
        username: "recruiter",
        password: "skillsync@123",
        role: "recruiter"
    },
    admin: {
        username: "admin",
        password: "admin@skillsync",
        role: "admin"
    }
};

// ===== LOGIN =====
function login(role, username, password) {
    const user = CREDENTIALS[role];
    if (user && user.username === username && user.password === password) {
        localStorage.setItem("auth_role", role);
        localStorage.setItem("auth_user", username);
        localStorage.setItem("auth_time", Date.now());
        return true;
    }
    return false;
}

// ===== LOGOUT =====
function logout() {
    localStorage.removeItem("auth_role");
    localStorage.removeItem("auth_user");
    localStorage.removeItem("auth_time");
}

// ===== CHECK IF LOGGED IN =====
function isLoggedIn(requiredRole) {
    const role = localStorage.getItem("auth_role");
    const time = localStorage.getItem("auth_time");

    // Session expires after 2 hours
    const TWO_HOURS = 2 * 60 * 60 * 1000;
    if (!role || !time || Date.now() - time > TWO_HOURS) {
        logout();
        return false;
    }
    return role === requiredRole;
}

// ===== PROTECT PAGE =====
// Call this at the top of every protected page
function requireAuth(role, loginPage) {
    if (!isLoggedIn(role)) {
        window.location.href = loginPage;
    }
}

// ===== GET LOGGED IN USER =====
function getUser() {
    return localStorage.getItem("auth_user");
}