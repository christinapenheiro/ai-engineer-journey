# D. Add type hints and run mypy
# Input: is_ai_job, salary_stats, and group_by_company from Day 1
# Steps:
# Add hints, for example def is_ai_job(title: str) -> bool: and def salary_stats(salaries: list[int], round_to: int = 0) -> tuple[int, int, float]:.
# Install and run: pip install mypy, then mypy yourfile.py.
# Break it on purpose: call salary_stats("abc") and read the error.
# Expected: Success: no issues found first, then an error about an incompatible argument type for the broken call.
# Check: after you remove the bad call, mypy is clean again.

from dataclasses import dataclass,field
from typing import Any

@dataclass
class Job:
    title: str
    company: str
    salary: int
    remote: bool
    skills: list[str] = field(default_factory=list)

    def is_ai(self)->bool:
        ai:list[str] = ["ai", "ml", "llm"]
        for word in self.title.lower().split():
            if word in ai:
                return True
        return False

    @staticmethod #use static methods when do not need any attribute from self(class)
    def salary_stats(salaries:list[int], round_to=0)->tuple[int,int,float]:
        total = 0
        max_num = salaries[0]
        lowest = salaries[0]
        for salary in salaries:
            if salary > max_num:
                max_num = salary
            if salary < lowest:
                lowest = salary
            total = total + salary
        average = total / len(salaries)
        return lowest, max_num, round(average, round_to)


jobs:list[dict[str,Any]] = [
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
salaries = [job["salary"] for job in jobs]

job_1 = Job(
    "Email Support Agent",
    "Mailly",
    30000,
    True,
    ["english", "crm"],
)


print(job_1.is_ai())

print(job_1.salary_stats(salaries))

# Why this error? bacause I the argument is a list of int PS F:\ai-engineer-journey\day_02> python -m mypy type_hints.py                                
# type_hints.py:92: error: Argument 1 to "salary_stats" of "Job" has incompatible type "list[object]"; expected "list[int]"
# salaries = [job["salary"] for job in jobs]

# Each job dict holds values of different types: a string ("AI Engineer"), an int (95000), a bool (True), and a list (["python", ...]). mypy sees a dict with mixed values and gives up on the exact type. It falls back to object, which means “could be anything”. So job["salary"] is object, and the list becomes list[object]. A list of “anything” is not guaranteed to be a list of int, so mypy complains.

# It’s like a drawer labelled “stuff”: you may know there are only forks inside, but the label doesn’t promise it.

# The fix: convert dicts to Job objects

# Steps:
# At the top, add from typing import Any.
# Annotate the list: jobs: list[dict[str, Any]] = [ ... ]. Any tells mypy “I accept that I don’t know these types”. Use it only at this one place, where raw data comes in.
# Build objects: job_objects = [Job(**d) for d in jobs]
# Get salaries from the objects: salaries = [job.salary for job in job_objects]
# Run python -m mypy type_hints.py