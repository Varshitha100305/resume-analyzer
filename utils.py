def create_prompt(resume, job_desc):
    return f"""
Compare the resume and job description.

Extract:
1. Matching skills
2. Missing skills
3. Suggestions

Resume:
{resume}

Job Description:
{job_desc}

Give output clearly in points.
"""
