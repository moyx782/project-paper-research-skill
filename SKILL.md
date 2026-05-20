---
name: project-paper-research
description: Collect, filter, analyze, and report academic papers for a software/robotics/AI project. Use this skill when the user needs literature search, paper matrix creation, project-related citation support, or a Markdown literature review.
---

# Project Paper Research Skill

## Purpose

This skill helps collect academic papers that are directly useful for a project. It should not only list links. It should build a project-aware literature map, evaluate relevance, and produce a paper matrix plus a Markdown literature review.

Use this skill when the user asks for:

- papers related to a project
- literature review support
- academic references for a report or proposal
- papers that justify a system architecture
- papers for AI agents, note-taking systems, robotics, RAG, OCR, ASR, local-first software, or plugin architectures
- a table of papers with relevance and citation notes

## Core Principle

Always connect each paper back to the user's project.

For every paper, answer:

1. What problem does this paper solve?
2. What method/system does it propose?
3. What evidence does it provide?
4. Which part of the user's project can use it?
5. Is it a must-read, useful, or background-only paper?

## Workflow

### Stage 1: Clarify Project Context

If the project context is missing, infer from the conversation when possible. Do not ask unnecessary questions. Create a short project profile:

```markdown
## Project Profile

- Project name:
- Domain:
- Target users:
- Core features:
- Technical stack:
- Research areas:
- Expected deliverable:
```

If the user has already described the project, use that context directly.

### Stage 2: Build Literature Search Outline

Create 6-12 search topics. Each topic should include:

- topic name
- why it matters to the project
- search keywords
- recommended databases
- expected paper types

Preferred databases and sources:

Default anonymous/free sources:

- arXiv
- Crossref public REST metadata
- DBLP publication search

Optional sources when configured by the user:

- Semantic Scholar
- OpenAlex
- Crossref polite pool using `CROSSREF_MAILTO`

Manual verification sources:

- Google Scholar
- ACM Digital Library
- IEEE Xplore
- SpringerLink
- ScienceDirect
- ACL Anthology
- CHI / UIST / CSCW / IUI proceedings
- NeurIPS / ICML / ICLR / ACL / EMNLP proceedings

Source policy:

- If `ANONYMOUS_MODE=true`, do not ask for or use API keys, email addresses, or personalized identifiers.
- If `.env` enables optional sources, use them only as configured.
- Never expose API keys in reports, logs, prompts, or final output.

### Stage 3: Define Inclusion and Exclusion Criteria

Use these default criteria unless the user says otherwise.

Include papers that:

- are directly related to the project design, architecture, algorithm, interaction model, or evaluation
- are peer-reviewed or widely cited preprints
- provide system design, user studies, benchmarks, algorithms, or design implications
- can support a project report, proposal, poster, or dissertation-style literature review

Exclude or down-rank sources that:

- are only blog posts without technical depth
- are product marketing pages
- have no clear method or evidence
- are unrelated even if they contain similar keywords
- are too old unless they are foundational

### Stage 4: Collect Papers

For each search topic, collect papers in this structure:

```markdown
| Priority | Title | Year | Venue | Link | DOI/arXiv | Why relevant |
|---|---:|---:|---|---|---|---|
```

Priority labels:

- Must read: directly supports the project core
- Useful: supports one module or argument
- Background only: useful for context but not central

### Stage 5: Deep Paper Analysis

For each selected paper, use the following fields:

```markdown
## Paper: <title>

- Authors:
- Year:
- Venue:
- Source link:
- DOI / arXiv:
- Research problem:
- Proposed method:
- System architecture / model:
- Dataset / experiment / user study:
- Key findings:
- Limitations:
- Relevance to the user's project:
- How to use this paper in the report:
- Related project module:
- Priority: Must read / Useful / Background only
- BibTeX:
```

### Stage 6: Build Paper Matrix

Create a matrix that allows the user to compare papers quickly.

Required columns:

```markdown
| ID | Priority | Topic | Paper | Year | Venue | Method | Evidence | Project relevance | Use in report | Limitations | Link | BibTeX available |
|---|---|---|---:|---:|---|---|---|---|---|---|---|---|
```

### Stage 7: Generate Literature Review Report

Create a Markdown report using this structure:

```markdown
# Literature Review for <Project Name>

## 1. Project Background

## 2. Research Scope

## 3. Paper Map by Topic

## 4. Must-Read Papers

## 5. Topic Review

### 5.1 <Topic A>
### 5.2 <Topic B>
### 5.3 <Topic C>

## 6. Design Implications for This Project

## 7. Research Gaps

## 8. Recommended Citation Strategy

## 9. Paper Matrix

## 10. BibTeX Appendix
```


## Environment Configuration

If an `.env` file is available, treat it as private local configuration. Do not write its secret values into outputs.

Default variables:

```env
PAPER_RESEARCH_SOURCES=arxiv,crossref,dblp
ANONYMOUS_MODE=true
PAPER_RESEARCH_LANGUAGE=zh-CN
PAPER_RESEARCH_MAX_RESULTS_PER_QUERY=10
PAPER_RESEARCH_MAX_PAPERS_TOTAL=50
PAPER_RESEARCH_OUTPUT_DIR=./research-output
```

Optional identified variables:

```env
USE_SEMANTIC_SCHOLAR=true
USE_OPENALEX=true
USE_CROSSREF_POLITE_POOL=true
SEMANTIC_SCHOLAR_API_KEY=...
OPENALEX_API_KEY=...
CROSSREF_MAILTO=...
```

Rules:

- `.env.example` may be committed.
- `.env` must stay local and private.
- API keys belong in `.env`, not in `SKILL.md`, `README.md`, prompts, examples, or generated reports.
- In anonymous mode, use only sources listed in `PAPER_RESEARCH_SOURCES` that do not require identity.

## Output Rules

- Prefer Markdown.
- Do not only list links.
- Do not mix weak blogs with academic papers unless clearly labeled.
- Always explain relevance to the user's project.
- Use tables for comparison.
- Mark uncertainty clearly.
- If web browsing/search tools are available, use them for current and accurate paper metadata.
- When a DOI, arXiv ID, venue, or year is uncertain, mark it as `needs verification`.
- Keep filenames in English.

## Default Project Profiles

### Profile A: AI Note Application

Use this when the user mentions Milkdown, Markdown notes, Pi Agent, AI note app, local-first storage, OCR, ASR, handwriting, RAG, or plugin-based notes.

Research topics:

1. AI-assisted note-taking systems
2. Personal knowledge management
3. Markdown and structured document editing
4. Human-AI collaborative writing
5. AI annotation and learning support
6. Tool-using LLM agents
7. Agent workflow automation
8. RAG over personal knowledge bases
9. Local-first software and offline-first sync
10. Plugin architecture for extensible editors
11. OCR, ASR, and handwriting recognition for notes
12. Educational technology and learning analytics

### Profile B: LLM-Agent UAV Swarm Robotics

Use this when the user mentions UAV swarm, decentralized robotics, disaster search, ROS2, Gazebo, AirSim, Isaac Sim, MAVLink, task allocation, CBBA, or mission JSON.

Research topics:

1. Multi-UAV task allocation
2. Decentralized swarm coordination
3. CBBA and auction-based allocation
4. Human-swarm interaction
5. Natural language mission planning
6. LLM agents for robotics
7. Tool-using LLMs in embodied systems
8. Communication-constrained multi-agent systems
9. Disaster search and rescue UAV systems
10. ROS2 multi-robot simulation
11. Safe high-level autonomy with LLM planners
12. Map-based mission planning and task decomposition

## One-Shot Prompt Template

Use this prompt when starting the workflow:

```text
Use the project-paper-research skill.

Project:
<describe the project here>

Goal:
Collect academic papers and high-quality references that can support the design, implementation, and report writing of this project.

Please run the workflow in stages:
1. Build a literature search outline.
2. Define paper collection fields.
3. Search and collect papers by topic.
4. Analyze the most relevant papers.
5. Build a paper matrix.
6. Generate a Markdown literature review report.

For every paper, include:
- title
- authors
- year
- venue
- DOI/arXiv if available
- source link
- research problem
- method
- evidence or evaluation
- limitations
- relevance to my project
- how I can cite it in my report
- priority: must-read / useful / background only
- BibTeX if available

Do not only list links. Explain why each paper matters to the project.
```
