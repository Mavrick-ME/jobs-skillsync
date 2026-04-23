import re

# Common names to anonymize
MALE_NAMES = [
    "james", "john", "robert", "michael", "william", "david", "richard",
    "joseph", "thomas", "charles", "alex", "raj", "rahul", "amit", "suvan"
]

FEMALE_NAMES = [
    "mary", "patricia", "jennifer", "linda", "barbara", "elizabeth",
    "susan", "jessica", "sarah", "karen", "priya", "sara", "akshitha"
]

GENDERED_WORDS = [
    "he", "she", "him", "her", "his", "hers", "himself", "herself",
    "mr.", "mrs.", "ms.", "miss", "sir", "madam"
]

def anonymize_name(text: str) -> str:
    """Replace candidate names with anonymous placeholders."""
    words = text.split()
    anonymized = []
    counter = [1]

    for i, word in enumerate(words):
        word_lower = word.lower().strip(".,")
        if word_lower in MALE_NAMES or word_lower in FEMALE_NAMES:
            anonymized.append(f"Candidate_{counter[0]}")
            counter[0] += 1
        else:
            anonymized.append(word)

    return " ".join(anonymized)


def remove_gender_signals(text: str) -> str:
    """Remove gendered pronouns and titles."""
    for word in GENDERED_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
    return text


def remove_age_signals(text: str) -> str:
    """Remove graduation years and age indicators."""
    # Remove years that look like graduation years (1990-2010)
    text = re.sub(r'\b(19[6-9]\d|200[0-9]|201[0-5])\b', '[YEAR]', text)
    # Remove age mentions
    text = re.sub(r'\b\d{2}\s*years?\s*old\b', '[AGE REDACTED]', text, flags=re.IGNORECASE)
    return text


def remove_location_signals(text: str) -> str:
    """Remove address and location details."""
    # Remove email addresses
    text = re.sub(r'\S+@\S+\.\S+', '[EMAIL]', text)
    # Remove phone numbers
    text = re.sub(r'[\+\d][\d\s\-\(\)]{8,}', '[PHONE]', text)
    return text


def apply_bias_filter(text: str, settings: dict = None) -> str:
    """
    Apply all bias mitigation filters based on settings.
    Default: all filters ON.
    """
    if settings is None:
        settings = {
            "anonymize_names": True,
            "remove_gender": True,
            "remove_age": True,
            "remove_location": True
        }

    if settings.get("remove_location"):
        text = remove_location_signals(text)

    if settings.get("anonymize_names"):
        text = anonymize_name(text)

    if settings.get("remove_gender"):
        text = remove_gender_signals(text)

    if settings.get("remove_age"):
        text = remove_age_signals(text)

    return text


def get_anonymized_name(original_name: str, index: int) -> str:
    """Return anonymized candidate label."""
    return f"Candidate {index + 1}"