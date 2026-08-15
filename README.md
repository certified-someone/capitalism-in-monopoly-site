# The Making of Capitalism — Monopoly Site

LSO440 Individual Website Project. A 6-page site explaining capitalism through the mechanics and real history of Monopoly / The Landlord's Game.

## Files

- `index.html` — Home (hero + Choose Your Player + Landlord's Game history)
- `rules-of-the-game.html` — What Is Capitalism?
- `manufacturing-the-consumer.html` — Manufacturing the Consumer
- `the-states-hand.html` — The State's Hand in the Market
- `capitalism-without-borders.html` — Capitalism Without Borders
- `bankruptcy.html` — Bankruptcy: Winners, Losers, and Inequality
- `assets/styles.css` — all styling (design tokens at the top of the file)
- `build.py` — the generator script that produced the HTML pages from the content (not needed for hosting, kept for editing convenience — see below)

## How to put this on GitHub Pages (free hosting, ~5 minutes)

1. **Create a repository.** Go to github.com → New repository → name it something like `capitalism-monopoly-site` → Public → Create repository (don't initialize with a README, you already have one).

2. **Upload the files.** Easiest way if you're not using git on the command line:
   - On the new repo page, click **"uploading an existing file"**.
   - Drag in `index.html`, all the other `.html` files, `README.md`, `build.py`, and the whole `assets` folder (drag the folder in directly — GitHub preserves the folder structure).
   - Scroll down, click **Commit changes**.

3. **Turn on GitHub Pages.**
   - In your repo, go to **Settings** → **Pages** (left sidebar, under "Code and automation").
   - Under **Build and deployment → Source**, choose **Deploy from a branch**.
   - Under **Branch**, choose **main** and folder **/ (root)**, then **Save**.

4. **Wait about a minute**, then refresh that same Pages settings screen. GitHub will show your live URL, something like:
   `https://yourusername.github.io/capitalism-monopoly-site/`

That link is what you submit and present from. It updates automatically any time you edit a file and commit again.

## If you want to edit content later

Easiest option: edit the `.html` files directly on GitHub (click a file → pencil icon → edit → commit). Every page has clearly separated `<p>` paragraphs and a `Sources for this page` list at the bottom, so text is easy to find and change.

If you want to regenerate all six pages at once from scratch (e.g. after changing shared content), `build.py` is a Python script that builds every page from a single source — edit the body text or sources near the bottom of the file and re-run `python3 build.py` locally, then re-upload the changed `.html` files.

## Before you submit

- Every page's "Sources for this page" footer should list everything cited on that page — double check nothing was added without a matching source.
- Test the live link in an incognito/private window to make sure it actually loads for someone who isn't you.
- Check the site on your phone too — it's responsive, but worth a look before presenting.
