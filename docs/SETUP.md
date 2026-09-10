# Profile README setup

One-time steps that need account access (never automated here).

## 1. GitHub stats cards

Served by the public instance of https://github.com/stats-organization/github-stats-extended (`github-stats-extended.vercel.app`) — API-compatible with github-readme-stats, so the README uses it directly. To self-host instead: fork that repo, deploy to Vercel with a GitHub PAT in `PAT_1` (`read:user` + `repo` for `count_private=true`), then replace every `github-stats-extended.vercel.app` in `README.md` with your domain.

## 2. WakaTime

1. https://wakatime.com/settings/api-key → copy key.
2. Repo → Settings → Secrets and variables → Actions → new secret `WAKATIME_API_KEY`.
3. Run **Update WakaTime stats** workflow manually once.

## 3. Latest articles

Feed live at https://www.sumonselim.com/rss.xml. Run **Update latest articles** workflow manually once.

## 4. Snake

Runs on next push to `main` or manually. Writes SVGs to `output` branch; README already references them.
