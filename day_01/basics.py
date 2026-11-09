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


# 1. study_hours
hours_per_day = 4
days_per_week = 6
weeks = 26

print(f"Weekly hours - {4*6}\nTotal hours - {4*6*26}")


# 2. string cleaner
job = "  Senior AI Engineer (Remote)  "
string_cleaner = job.strip().lower().replace("(", "").replace(")", "").split()
print(string_cleaner[0], string_cleaner[-1])
if "remote" in string_cleaner:
    print("remote is here.")


# 3. is_ai_job(title) -> bool


def is_ai_job(title):
    job_title = title.lower().split()
    match = ["ai", "ml", "llm"]
    return any(keyword in match for keyword in job_title)


print(is_ai_job("AI Engineer"))  # True
print(is_ai_job("ML Engineer"))  # True
print(is_ai_job("LLM Application Developer"))  # True
print(is_ai_job("Email Support Agent"))  # False
# print(is_ai_job("Senior AI-Engineer"))


# 4. salary_stats(salaries, round_to=0)


def salary_stats(salaries, round_to=0):
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


salaries = [job["salary"] for job in jobs]
low, high, avg = salary_stats(salaries)


assert low == min(salaries)
assert high == max(salaries)
assert avg == round(sum(salaries) / len(salaries), 0)
print("All correct!")

# 5. Loops

job_details = [
    f"{index}.{key["title"]} @ {key["company"]} - ${key["salary"]:,}"
    for index, key in enumerate(jobs, start=1)
]

# print(job_details)

title = [key["title"] for key in jobs]
# print(title)
salaries_ = [key["salary"] for key in jobs]
# print(salaries_)


for title, salaries in zip(title, salaries_):
    print(title, salaries)


total_ = 0
i = 0
while i < len(salaries_):
    if total_ > 200000:
        print("total passes 200000")
        break
    print(total_)
    total_ += salaries_[i]
    i+=1
