def add_skill(skill, skills=None):
    if skills is None:
        skills = []
    skills.append(skill)
    return skills


print(add_skill("python"))
print(add_skill("rag"))

# Predict first: write down what you think each line prints, then run it.
# Actual output: ['python'] then ['python', 'rag']. The default list is created once, so every call shares it.
# Fix: use skills=None, and inside write if skills is None: skills = [].
# Expected after the fix: ['python'] then ['rag'].
# Then try: a = [1, 2], b = a, b.append(3), print(a), and print(a is b). Explain in one sentence why a changed. It’s the same reason copy() didn’t work yesterday.

# 1st line- ["python"]
# 2nd line- ["python","rag"]

a = [1,2]
b = a
b.append(3)
print(a)
print(a is b)

# when assigning a = b, then both refers to the same value. Append an item to a mutable list in b, also changed value for a. Because list is mutable, changing another variable items also change the original list.
# Also because of both a, b refers to the same variable (They’re two names for the same list. There’s only one list.) a is b is also true, because is checks whether both names point to the same object. == checks whether the values are equal..
# Also copy() didn't work because its only shallow copy the mutable objects, when mutable objects becomes nested, shallow copy doesn't remain unchanged, so deepcopy is needed.A shallow copy makes a new outer container, but the objects inside are still shared.


# F. Optional: JobTracker class
# What it is: a class that holds a list of Job objects. It’s the seed of your Job Tracker project.
# Steps: write methods add(job), ai_jobs() (returns only AI jobs), and average_salary().
# Expected: with your 5 jobs, average_salary() is 76000.0 and len(tracker.ai_jobs()) is 3.


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


# A class object and a dictionary can contain similar information, but they are different types of objects.
# Data type	Access method	Example
# Dictionary	Square brackets	d["title"]
# Class object	Dot notation	j.title
# List	Index	my_list[0]
# Tuple	Index	my_tuple[0]


def is_ai_job(title):
    ai_keywords = {"ai", "ml", "llm"}
    for word in title.lower().split():
        if word in ai_keywords:
            return True
    return False


class JobTracker:
    def __init__(self):
        self.jobs = []

    def add(self,job):
        self.jobs.append(job)

    def ai_jobs(self):
        return [job for job in self.jobs if is_ai_job(job["title"])]

    def average_salary(self):
        self.salary = [job["salary"] for job in self.jobs]
        self.avg_salary = sum(self.salary) / len(self.jobs)
        return self.avg_salary


tracker = JobTracker()

for d in jobs:
    tracker.add(d)


print(len(tracker.jobs)) 
print(len(tracker.ai_jobs()))  
print(tracker.average_salary())
