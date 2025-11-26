# skills.py

import re
from collections import Counter

# A simple predefined skills list (expand as needed)
SKILL_KEYWORDS = [
    "python", "java", "c++", "flask", "django", "javascript",
    "html", "css", "sql", "machine learning", "data analysis",
    "react", "node", "aws", "docker", "kubernetes", "springboot"
]

def extract_skills(text):
    text_lower = text.lower()

    found_skills = []

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    # Count occurrences (not necessary now but useful later)
    counter = Counter(found_skills)

    # Return top 2
    return [skill for skill, count in counter.most_common(2)]
