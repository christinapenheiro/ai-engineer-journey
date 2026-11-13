# A. Write a Job class (manual)
# Input: the values of the first job in jobs
# Steps:
# Write class Job with __init__(self, title, company, salary, remote, skills).
# Add a method is_ai(self) that reuses your is_ai_job logic on self.title.
# Add __repr__ that returns Job(title='AI Engineer', company='Nova', salary=95000).
# Expected output: print(job) shows the line above, and job.is_ai() prints True.
# Check: make a second Job for “Email Support Agent”. is_ai() must be False.


class Job:
    def __init__(self, title, company, salary, remote, skills):
        self.title = title
        self.company = company
        self.salary = salary
        self.remote = remote
        self.skills = skills

    def is_ai(self):
        self.ai = ["ai", "ml", "llm"]
        for word in self.title.lower().split():
            if word in self.ai:
                return True
        return False


    def __repr__(self):
        return f"Job(title={self.title},company={self.company},salary={self.salary})"


ai_engineer_job = Job(
    "AI Engineer",
    "Nova",
    95000,
    True,
    ["python", "fastapi", "rag"],
)

email_support_job = Job(
    "Email Support Agent",
    "Mailly",
    30000,
    True,
    ["english", "crm"],
)


print(ai_engineer_job.is_ai())
print(email_support_job.is_ai())
print(ai_engineer_job)

# B. Convert your data to objects
# Input: your jobs list of dicts
# Steps: build job_objects = [Job(**d) for d in jobs]. The **d unpacks a dict into named arguments.
# Expected: len(job_objects) is 5.
# Check: [j.title for j in job_objects if j.is_ai()] should give ['AI Engineer', 'ML Engineer', 'LLM Application Developer'].
# with list of dict inside class

jobs = [
    {
        "title": "AI Engineer",
        "company": "Nova",
        "salary": 95000,
        "remote": True,
        "skills": ["python", "fastapi", "rag"],
    },
    {
        "title": "Email Support Agent",
        "company": "Mailly",
        "salary": 30000,
        "remote": True,
        "skills": ["english", "crm"],
    },
    {
        "title": "ML Engineer",
        "company": "Orbit",
        "salary": 110000,
        "remote": False,
        "skills": ["python", "pytorch", "sql"],
    },
    {
        "title": "LLM Application Developer",
        "company": "Nova",
        "salary": 85000,
        "remote": True,
        "skills": ["python", "langgraph", "rag", "docker"],
    },
    {
        "title": "Frontend Developer",
        "company": "Pixel",
        "salary": 60000,
        "remote": True,
        "skills": ["react", "typescript"],
    },
]


job_object = [
    Job(job["title"], job["company"], job["salary"], job["remote"], job["skills"])
    for job in jobs
]

ai_job_list = [job.title for job in job_object if job.is_ai()]
print(ai_job_list)
