def skill_gap(jd_skills, resume_skills):
    missing = list(set(jd_skills) - set(resume_skills))
    return missing
