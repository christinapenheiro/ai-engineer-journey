# AI Engineer Journey

I'm learning AI engineering in public. This repo holds my code, notes, and progress while I follow a 6-month plan to become a job-ready AI engineer.

## About me

- Web developer with MERN stack experience
- Basic Python, NumPy, and pandas, now revising and going deeper

## The plan

- **Time:** 6 months, at least 4 hours a day, 6 days a week
- **Rules I follow:**
  - Write core Python myself, without AI autocomplete, in the first weeks
  - Explain every line I ship, even if AI helped
  - Finish a project before starting the next level
  - Measure results (for example, test-set accuracy) instead of saying "it works"

| Weeks | Focus | Project |
|---|---|---|
| 1-3 | Python, FastAPI, Git, SQL, Docker basics, testing | REST service with no AI |
| 4-6 | LLM basics, APIs, streaming, structured outputs, tool calling, prompting | Streaming tool-using assistant |
| 7-10 | RAG: chunking, embeddings, vector search | Deployed RAG app with a frontend |
| 11-15 | Agents, MCP, LangGraph, context engineering | Production-style agent |
| 16-19 | Evals and AI security | Eval suite and red-team tests for my projects |
| 20-23 | System design, Docker, cloud deploy, monitoring | Live, containerized projects |
| 24-26 | Portfolio polish and interview prep | 3-5 public projects |

## Progress

| Day | Topic | Status |
|---|---|---|
| 1 | Python core: functions, data structures, comprehensions, iterators, generators | Completed |


## Repo structure

```
ai-engineer-journey/
├── day-01/
│   ├── basics.py
│   ├── data_structures.py
│   ├── comprehensions.py
├── notes/
│   ├── day-01-interview-qa.pdf
│   └── 82a658ec-21b0-4b9c-95bc-db7c380166bc_day-01-interview-qa_my_answer.pdf
└── README.md
```

## What I learned so far

- A shallow copy shares the objects inside it. `deepcopy` makes them fully separate.
- Checking `"ai" in "email"` matches letters, not words. Split into words first.
- `a, b = b, a + b` updates both values at once, which is why it works for Fibonacci.
- Generators are lazy: they make one item at a time, so they stay small in memory.

## Follow along

I post updates as I finish each project. Feel free to open an issue if you spot a mistake in my notes.
