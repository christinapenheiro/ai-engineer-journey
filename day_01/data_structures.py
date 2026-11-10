from collections import Counter
from collections import defaultdict
import copy

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


# 6

skill_list_all = []
skillList = []

for job in jobs:
    for skill in job["skills"]:
        skill_list_all.append(skill)
        if skill in skillList:
            continue
        skillList.append(skill)

print("No Duplicates",skillList)
print("All skill Flat List",skill_list_all)


skillSet = set()

for job in jobs:
    for skill in job["skills"]:
        skillSet.add(skill)

# print(skillSet)


sortedSkillList = sorted(skillList)
print(sortedSkillList)
skillList.sort()
print(skillList)


# 7


required = {"python", "rag", "docker", "fastapi"}
skillGap = required - my_skills
skillgap_ = ", ".join(skillGap)
my_skills_sort = sorted(list(my_skills))
my__skills = ", ".join(my_skills_sort)
combined = ", ".join(my_skills | required)
print(f"I have {my__skills} and I am missing {skillgap_} and everything combined {combined}.")
learning_list = list(skillGap)
print(learning_list)


# 8

companies = [job["company"] for job in jobs]

# using normal count no method

counts = {}

for word in companies:
    counts[word] = counts.get(word,0) + 1

print(counts)


# Now using method counter from collection

applying_method = Counter(companies).most_common(3)
print(applying_method)


# 9 group jobs by company

# At first trying manually

job_dict = {}

for job in jobs:
    company = job["company"]
    if company not in job_dict:
        job_dict[company] = []
    job_dict[company].append(job["title"])
print(job_dict)


# using by trying setdefault()

groups = {}

for job in jobs:
    groups.setdefault(job["company"],[]).append(job["title"])

# using by trying default dict() imported from collections

groups_ = defaultdict(list)

for job in jobs:
    groups_[job["company"]].append(job["title"])

# print(groups_)


# compare all 3 methods

print(job_dict == groups == groups_)


# 10

job_dupli = copy.deepcopy(jobs)


for job in jobs:
    new_attribute = job.get("benefits","not listed")
    if "benefits" in job:
        print(job.get("benefits"))
    print("Salary in job",job.get("salary"))


# update a salary using next

target_job = next((job for job in job_dupli if job["title"] == "Frontend Developer"),None)

if target_job:
    target_job["salary"] = target_job["salary"] * 2


# delete a key

for job in job_dupli:
    del job["company"]


frontend_original = next(j for j in jobs if j["title"] == "Frontend Developer")
frontend_copy = next(j for j in job_dupli if j["title"] == "Frontend Developer")

print(f"compare {frontend_original["salary"]}, {frontend_copy["salary"]}")
print(f"compare {"company" in jobs[0]}, {"company" in job_dupli[0]}")


# 11

sorting_tuples = sorted(
    [(job["title"], job["salary"]) for job in jobs], key=lambda x: x[1], reverse=True
)
print(sorting_tuples[:3])

jobs.sort(key=lambda x: x["salary"], reverse=True)

