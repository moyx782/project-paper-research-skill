# Project Paper Research Skill

这个 skill 用来帮你为项目搜集论文、筛选论文、做阅读矩阵，并生成 Markdown 文献综述。

It is designed for project-aware academic paper collection, not random link gathering.

## Files

```text
project-paper-research-skill/
├── SKILL.md
├── README.md
├── .env.example
├── .gitignore
├── docs/
│   └── source_config.md
├── templates/
│   ├── paper_matrix_template.md
│   └── literature_review_report_template.md
├── examples/
│   ├── ai_note_app_project.md
│   └── uav_swarm_project.md
└── prompts/
    └── one_shot_prompt.md
```

## Install

### Generic skill directory

Copy the folder into your agent's skills directory:

```bash
mkdir -p ~/.codex/skills
cp -r project-paper-research-skill ~/.codex/skills/project-paper-research
```

### Windows WSL example

```bash
cd /mnt/c/Users/$USER/Downloads
unzip project-paper-research-skill.zip
mkdir -p ~/.codex/skills
cp -r project-paper-research-skill ~/.codex/skills/project-paper-research
```

### Pi Agent / custom agent usage

If your Pi Agent supports a skill folder, copy this folder into its skill directory. If it only supports prompt files, paste `SKILL.md` as the system/skill instruction.


## Configure sources

This skill works without any API key by default. Use the provided environment template:

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

Optional API keys should be added only to your local `.env` file, never to `SKILL.md` or GitHub:

```env
SEMANTIC_SCHOLAR_API_KEY=your_key_here
OPENALEX_API_KEY=your_key_here
CROSSREF_MAILTO=your_email@example.com
```

See `docs/source_config.md` for details.

## Example command

```text
Use the project-paper-research skill to collect papers for my Markdown-native AI note app with Milkdown editor, Pi Agent sidebar, plugin architecture, local-first Markdown storage, and future OCR/ASR/RAG plugins.
```

## Output goal

The final output should include:

1. Literature search outline
2. Paper collection fields
3. Paper matrix
4. Deep paper analysis
5. Markdown literature review report
6. BibTeX appendix when available
