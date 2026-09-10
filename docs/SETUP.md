# Profile README setup

One-time steps that need account access (never automated here).

## 1. GitHub stats cards

Served by the public instance of https://github.com/stats-organization/github-stats-extended (`github-stats-extended.vercel.app`) — API-compatible with github-readme-stats, so the README uses it directly.

## 2. WakaTime

Served live by the github-stats-extended WakaTime card from the public WakaTime profile (`wakatime.com/@306f904d-42f5-43e6-bb95-1e979d459985`). Requires "Display code time publicly" and "Display languages, editors, os, categories publicly" to stay enabled in WakaTime settings.

## 3. Latest articles

Feed live at https://www.sumonselim.com/rss.xml. Run **Update latest articles** workflow manually once.

## 4. Snake

Runs on next push to `main` or manually. Writes SVGs to `output` branch; README already references them.
