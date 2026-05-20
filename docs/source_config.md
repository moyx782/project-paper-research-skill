# Source Configuration

This skill is platform-agnostic. By default, it uses free anonymous sources only.

## Default anonymous mode

Use this when you do not want to provide accounts, API keys, or email identifiers.

```env
PAPER_RESEARCH_SOURCES=arxiv,crossref,dblp
ANONYMOUS_MODE=true
USE_SEMANTIC_SCHOLAR=false
USE_OPENALEX=false
USE_CROSSREF_POLITE_POOL=false
```

Default sources:

| Source | Key needed | Purpose |
|---|---:|---|
| arXiv | No | Preprints for AI, CS, robotics, HCI, RAG, agents |
| Crossref public REST | No | DOI and publication metadata |
| DBLP | No | Computer science bibliography and BibTeX metadata |

## Optional identified mode

Use this only when you want better metadata coverage or higher API stability.

```env
PAPER_RESEARCH_SOURCES=arxiv,crossref,dblp,semantic_scholar,openalex
ANONYMOUS_MODE=false
USE_SEMANTIC_SCHOLAR=true
USE_OPENALEX=true
USE_CROSSREF_POLITE_POOL=true

SEMANTIC_SCHOLAR_API_KEY=your_key_here
OPENALEX_API_KEY=your_key_here
CROSSREF_MAILTO=your_email@example.com
```

## Do not commit secrets

Only commit `.env.example`.
Never commit `.env`.

The repository `.gitignore` already ignores `.env`.
