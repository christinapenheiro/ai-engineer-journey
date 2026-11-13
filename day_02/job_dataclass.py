from dataclasses import dataclass, field


@dataclass
class Job:
    title: str
    company: str
    salary: int
    remote: bool
    # skills:list[str]=[] #error result: mutable default <class 'list'> for field skills is not allowed
    skills: list[str] = field(default_factory=list)

    def is_ai(self):
        self.ai = ["ai", "ml", "llm"]
        for word in self.title.lower().split():
            if word in self.ai:
                return True
        return False


job_1 = Job(
    "Email Support Agent",
    "Mailly",
    30000,
    True,
    ["english", "crm"],
)
print(job_1)
print(Job("A", "X", 1, True, []) == Job("A", "X", 1, True, []))


class Job2:
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

print(Job2("A", "X", 1, True, []) == Job2("A", "X", 1, True, []))

# @dataclass automatically generates a special method called __eq__(). This method compares the attributes of both objects, field by field.A normal class compares object identity by default. A dataclass automatically gives you value-based equality through __eq__().That's the main reason my example prints True with a dataclass and False with a plain class.
