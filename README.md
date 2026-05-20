# Project Paper Research Skill

A Codex / Pi Agent skill for collecting project-related academic papers, building a paper matrix, and generating a project-focused Markdown literature review.

这个 skill 的目标不是“随便列论文链接”，而是把论文和你的项目设计、报告写作、引用策略连接起来。

## What it does

Use this skill to:

- turn a project idea into literature search topics
- collect academic papers from free / anonymous sources by default
- classify papers as `Must read`, `Useful`, or `Background only`
- build a paper matrix for fast comparison
- produce a Markdown literature review report
- prepare citation notes and BibTeX placeholders

## Repository structure

```text
project-paper-research-skill/
├── SKILL.md
├── README.md
├── .env.example
├── .gitignore
├── docs/
│   └── source_config.md
├── examples/
│   ├── ai_note_app_project.md
│   └── uav_swarm_project.md
├── prompts/
│   └── one_shot_prompt.md
├── templates/
│   ├── paper_matrix_template.md
│   └── literature_review_report_template.md
└── scripts/
    └── validate_skill.py
```

## Install from GitHub

### macOS / Linux / WSL

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/moyx782/project-paper-research-skill.git ~/.codex/skills/project-paper-research
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force $HOME\.codex\skills
git clone https://github.com/moyx782/project-paper-research-skill.git $HOME\.codex\skills\project-paper-research
```

## Update the skill

```bash
cd ~/.codex/skills/project-paper-research
git pull
```

On Windows PowerShell:

```powershell
cd $HOME\.codex\skills\project-paper-research
git pull
```

## Configure paper sources

This skill works without API keys by default.

```bash
cp .env.example .env
```

Default anonymous/free mode:

```env
PAPER_RESEARCH_SOURCES=arxiv,crossref,dblp
ANONYMOUS_MODE=true
USE_SEMANTIC_SCHOLAR=false
USE_OPENALEX=false
USE_CROSSREF_POLITE_POOL=false
```

Optional API keys should be added only to your local `.env` file, never to GitHub:

```env
SEMANTIC_SCHOLAR_API_KEY=your_key_here
OPENALEX_API_KEY=your_key_here
CROSSREF_MAILTO=your_email@example.com
```

See [`docs/source_config.md`](docs/source_config.md) for details.

## Use in Codex

After installation, ask Codex:

```text
Use the project-paper-research skill to collect papers for my Markdown-native AI note app with Milkdown editor, Pi Agent sidebar, plugin architecture, local-first Markdown storage, and future OCR/ASR/RAG plugins.
```

Or for robotics:

```text
Use the project-paper-research skill to collect papers for my LLM-Agent-based decentralized UAV swarm project for disaster search and no-network environments.
```

## Use in Pi Agent / other agents

If your agent supports skill folders, copy or clone this repository into its skill directory.

If your agent only supports prompt files, use `SKILL.md` as the skill/system instruction and keep the templates as references.

## Validate before publishing

Run the validation script before pushing changes:

```bash
python scripts/validate_skill.py
```

It checks:

- `SKILL.md` exists
- YAML front matter contains `name` and `description`
- `.env.example` uses one variable per line
- `.gitignore` ignores `.env`
- no local `.env` file is accidentally present

## Output goal

A complete run should produce:

1. literature search outline
2. paper collection fields
3. paper matrix
4. deep paper analysis
5. Markdown literature review report
6. BibTeX appendix when available

## Privacy and secret handling

- Commit `.env.example` only.
- Never commit `.env`.
- Never put real API keys in `SKILL.md`, `README.md`, examples, prompts, templates, or generated reports.
- Keep `ANONYMOUS_MODE=true` when using only arXiv, Crossref public REST, and DBLP.
