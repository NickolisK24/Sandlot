# Contributing to sandlot

Thanks for your interest in sandlot. Bug reports, feature requests, docs fixes, and typo corrections are all welcome — open an issue or a PR.

## Project principles

1. **Correctness over everything.** Wrong data poisons every downstream analysis. Tests are not optional.
2. **Polite scraping.** We respect rate limits and robots.txt. Always.
3. **Backward compatibility.** If you relied on a function in v0.1, it will still work in v1.0.
4. **Kind code review.** We're all learning.

## Dev environment

```bash
python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
```

Run the checks before pushing:

```bash
ruff check .
mypy
pytest
```
