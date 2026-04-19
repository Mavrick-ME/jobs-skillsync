// Global API base URL
const API_BASE = "http://127.0.0.1:8000/api";

// Utility: show a toast notification
function showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.style.cssText = `
        position: fixed; bottom: 2rem; right: 2rem;
        background: ${type === "error" ? "#3b1a1a" : "#064e3b"};
        color: ${type === "error" ? "#f87171" : "#34d399"};
        border: 1px solid ${type === "error" ? "#f87171" : "#34d399"};
        padding: 1rem 1.5rem; border-radius: 10px;
        font-size: 0.9rem; font-weight: 600;
        z-index: 9999; opacity: 0;
        transition: opacity 0.3s ease;
        max-width: 300px;
    `;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.style.opacity = "1", 10);
    setTimeout(() => {
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}