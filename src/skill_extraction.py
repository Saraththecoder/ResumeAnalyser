import pandas as pd

skills = pd.read_csv("data/skill_dictionary.csv")["skill"].tolist()

def extract_skills(text):
    found_skills = []
    for skill in skills:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))
