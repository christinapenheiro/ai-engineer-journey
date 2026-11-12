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
