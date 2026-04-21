# sandlot

*A reliable, reproducible Python client for MLB Statcast data.*

---

## Why this exists

If you've ever tried to pull Statcast data for a project, you know the drill: scrape some endpoints, hope they haven't moved, re-pull the same data three times because something timed out, and never quite trust that the CSV you have today matches the one you pulled last month.

The open baseball community deserves better. Retrosheet, Baseball Reference, and FanGraphs built the foundation of modern analytics by making data accessible to anyone with a laptop and curiosity. That tradition is worth protecting.

**sandlot** is a small, focused Python library with one job: get you Statcast data reliably, cache it properly, and let you reproduce any pull exactly — today, next week, or two years from now when a reviewer asks for your dataset.

If you write Substack posts, publish research, or just learned what xwOBA is last week and want to poke at the numbers yourself — sandlot is built for you.

## Install

```bash
pip install sandlot
```

Requires Python 3.10+.

## Quickstart

```python
import sandlot

# Pull a date range — cached automatically, politely rate-limited
df = sandlot.fetch_statcast("2024-04-01", "2024-04-30")

print(df.head())
```

That's it. The first call pulls from Baseball Savant. Every call after that reads from your local cache — no waiting, no re-scraping, no rate limits.

### A full season

```python
df = sandlot.fetch_statcast_season(2024)
```

### A specific player

```python
ohtani = sandlot.fetch_statcast_player(mlbam_id=660271, season=2024)
```

## Reproducibility — the part researchers will love

Every cached pull is tagged with the date you fetched it. If you're publishing a paper or citing a dataset, you can pin to a specific snapshot and anyone can reproduce your exact dataset:

```python
# Fetch and tag the snapshot
df = sandlot.fetch_statcast("2024-04-01", "2024-04-30", snapshot="paper-v1")

# Months later, anywhere, anyone can pull the identical dataset
df = sandlot.load_snapshot("paper-v1")
```

Snapshots are stored as Parquet. Share them, check them into Git LFS, host them on OSF — whatever your workflow needs.

## What sandlot does well

- **Reliable fetching.** Polite rate limiting, exponential backoff, automatic retry on transient failures.
- **Local caching.** Never pull the same data twice. Cache lives at `~/.sandlot/` by default; fully configurable.
- **Schema validation.** If Baseball Savant adds, removes, or renames a column, you'll get a clear warning — not silent corruption.
- **Clean DataFrames.** Typed columns, consistent naming, documented fields.
- **Helpful errors.** When something goes wrong, you'll know exactly what and why.

## What sandlot does NOT do (yet)

Honesty upfront — the roadmap is ambitious, but v0.1 is narrow on purpose:

- ❌ Minor league data (coming in v0.3)
- ❌ Historical data pre-Statcast (Retrosheet/Lahman integration in v0.2)
- ❌ College or international data (longer-term)
- ❌ A hosted API or web interface (v0.5+)

If you need any of the above today, [pybaseball](https://github.com/jldbc/pybaseball) is a wonderful project and we stand on its shoulders.

## Roadmap

| Version | Focus                                     |
|---------|-------------------------------------------|
| **0.1** | Statcast fetching, caching, snapshots     |
| 0.2     | Retrosheet + Lahman integration           |
| 0.3     | MiLB data ingestion                       |
| 0.4     | Hosted Parquet archive for common datasets |
| 0.5+    | REST API, R client                        |

## Contributing

sandlot is built in the open, by and for the baseball analytics community. Whether you've found a bug, want to add a feature, improve docs, or just correct a typo — please open an issue or PR.

A few principles the project holds to:

1. **Correctness over everything.** Wrong data poisons every downstream analysis. Tests are not optional.
2. **Polite scraping.** We respect rate limits and robots.txt. Always.
3. **Backward compatibility.** If you relied on a function in v0.1, it will still work in v1.0.
4. **Kind code review.** We're all learning.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Acknowledgments

This project exists because others did the hard work first:

- **[Retrosheet](https://www.retrosheet.org/)** — the gold standard for historical baseball data, volunteer-maintained for decades.
- **[pybaseball](https://github.com/jldbc/pybaseball)** — the package most of us learned on. sandlot aims to complement it, not replace it.
- **[Baseball Reference](https://www.baseball-reference.com/)** and **[FanGraphs](https://www.fangraphs.com/)** — for making research accessible to generations of fans and analysts.
- Every indie analyst who ever shared a Jupyter notebook publicly. You built this community.

## License

MIT. Go build something with it.

---

*sandlot is maintained by Nickolis Kacludis and contributors. Not affiliated with Major League Baseball or Baseball Savant.*
