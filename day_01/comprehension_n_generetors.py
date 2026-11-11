# 12- (a) titles of remote jobs paying at least 80000, (b) {title: salary} dict, (c) a set of all unique skills (nested).
from collections import Counter
import sys


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
my_skills = {
    "python",
    "javascript",
    "typescript",
    "react",
    "nextjs",
    "expressjs",
    "mongodb",
}


remote_jobs = [job["title"] for job in jobs if job["salary"] >= 80000 and job["remote"]]

title_and_salary = {job["title"]: job["salary"] for job in jobs}

unique_skills = {skill for job in jobs for skill in job["skills"]}

print(unique_skills)
print(remote_jobs)


# 13


comprehension_of_ex_5 = [print(f"{index}.{job["title"]} @ {job["company"]} - ${job["salary"]:,}") for index,job in enumerate(jobs,start=1)]

comprehension_of_ex_5


comprehension_of_ex_6_flat_list = [skill for job in jobs for skill in job["skills"]]
print(comprehension_of_ex_6_flat_list)


# 14 : Use of generator

def countdown(n):
    while n > 0:
        yield n
        n-=1

for number in countdown(5):
    print (number)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a ,b = b, a + b

f = fibonacci()


for i in range(11):
    print(next(f))

# what is the differences between using generator and list?
# A list holds everything in memory at once. A generator makes one item at a time, only when asked, which is called lazy.
# Practical examples:

# Reading a huge file. A 5 GB log file won’t fit in a list, but a generator can give you one line at a time.
# LLM streaming. When ChatGPT or Claude types a reply word by word, your code receives it through a generator-like loop (for chunk in stream).
# Paginated APIs. A job board returns 50 listings per page. A generator can fetch page 1, give you those jobs, then fetch page 2 only when you need it. This will be part of your Job Tracker project.


skills = ["python", "rag", "docker"]
bookmark = iter(skills)

while True:
    try:
        item = next(bookmark)
    except StopIteration:
        break
    print(item)


# 15

def is_ai_job(title):
    job_title = title.lower().split()
    match = ["ai", "ml", "llm"]
    return any(keyword in match for keyword in job_title)


def ai_jobs(jobs):
    for job in jobs:
        if is_ai_job(job["title"]) == True:
            yield job["title"]


for job in ai_jobs(jobs):
    print(job)


generator_count_lazy = sum(1 for job in jobs if is_ai_job(job["title"]))
print(generator_count_lazy)

# memory comparison

big_list = [x for x in range(1_000_000)]
big_generator = (x for x in range(1_000_000))

print(sys.getsizeof(big_list))  # 8448728 bytes = 8mb
print(sys.getsizeof(big_generator)) #200 bytes

