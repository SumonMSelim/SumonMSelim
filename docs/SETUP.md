# Profile README setup

One-time steps that need account access (never automated here).

## 1. Self-host github-readme-stats on Vercel

1. Fork https://github.com/anuraghazra/github-readme-stats
2. Create a GitHub PAT (fine-grained, no scopes needed for public data; add `read:user` + `repo` for `count_private=true`).
3. Import the fork in Vercel. Set env var `PAT_1=<token>`. Deploy.
4. Replace every `STATS_HOST` in `README.md` with your Vercel domain, e.g. `github-readme-stats-sumonmselim.vercel.app`.

## 2. WakaTime

1. https://wakatime.com/settings/api-key → copy key.
2. Repo → Settings → Secrets and variables → Actions → new secret `WAKATIME_API_KEY`.
3. Run **Update WakaTime stats** workflow manually once.

## 3. Latest articles

Feed live at https://www.sumonselim.com/rss.xml. Run **Update latest articles** workflow manually once.

## 4. Snake

Runs on next push to `main` or manually. Writes SVGs to `output` branch; README already references them.
