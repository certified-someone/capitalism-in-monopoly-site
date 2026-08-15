#!/usr/bin/env python3
import os

OUT = "/home/claude/site"

ICONS = {
"dice": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8" cy="8" r="1.1" fill="currentColor" stroke="none"/><circle cx="16" cy="8" r="1.1" fill="currentColor" stroke="none"/><circle cx="8" cy="16" r="1.1" fill="currentColor" stroke="none"/><circle cx="16" cy="16" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none"/></svg>',
"house": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11 L12 4 L20 11"/><path d="M6 10 V20 H18 V10"/><rect x="10" y="14" width="4" height="6"/></svg>',
"bank": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9 L12 4 L21 9"/><rect x="4" y="9" width="16" height="11"/><line x1="7" y1="9" x2="7" y2="20"/><line x1="12" y1="9" x2="12" y2="20"/><line x1="17" y1="9" x2="17" y2="20"/><line x1="3" y1="20" x2="21" y2="20"/></svg>',
"tophat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="19" rx="9" ry="2"/><path d="M8 19 V9 Q8 5 12 5 Q16 5 16 9 V19"/><line x1="8" y1="10" x2="16" y2="10"/></svg>',
"money": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="11" rx="1.5"/><circle cx="12" cy="12.5" r="2.6"/></svg>',
"train": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="6" width="14" height="11" rx="2"/><line x1="5" y1="11" x2="19" y2="11"/><circle cx="9" cy="19.4" r="1.3"/><circle cx="15" cy="19.4" r="1.3"/><line x1="8" y1="6" x2="8" y2="3.5"/><line x1="4" y1="3.5" x2="8" y2="3.5"/></svg>',
"handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12 L6 8 L10 11 L8 13"/><path d="M22 12 L18 8 L14 11 L16 13"/><path d="M8 13 L11 16 Q12 17 13 16 L16 13"/></svg>',
"tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 3H5a2 2 0 00-2 2v6a2 2 0 00.6 1.4l9 9a2 2 0 002.8 0l6.6-6.6a2 2 0 000-2.8l-9-9A2 2 0 0011 3z"/><circle cx="7.5" cy="7.5" r="1.1" fill="currentColor" stroke="none"/></svg>',
"scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="21"/><line x1="5" y1="7" x2="19" y2="7"/><path d="M5 7 L2 14 Q5 16.2 8 14 Z"/><path d="M19 7 L15.5 14.6 Q19 16.7 22.5 14.6 Z"/></svg>',
"card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="7" y1="14" x2="13" y2="14"/></svg>',
"chest": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="10" width="18" height="9" rx="1.5"/><path d="M3 10 Q3 5 12 5 Q21 5 21 10"/><line x1="10" y1="13" x2="14" y2="13"/></svg>',
"jail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="1"/><line x1="9" y1="4" x2="9" y2="20"/><line x1="14" y1="4" x2="14" y2="20"/></svg>',
"arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/></svg>',
# tokens
"car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 16 L4 11 Q5 9 7 9 H17 Q19 9 20 11 L21 16"/><rect x="2" y="16" width="20" height="3" rx="1"/><circle cx="7" cy="19.3" r="1.5"/><circle cx="17" cy="19.3" r="1.5"/></svg>',
"dog": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18 Q3 12 8 11 L9 7 L11 10 Q14 9 16 11 L18 9 L18 13 Q20 13 20 16 V18"/><line x1="7" y1="18" x2="7" y2="20"/><line x1="17" y1="18" x2="17" y2="20"/></svg>',
"thimble": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M8 5 H16 L15 13 A3 3 0 0 1 9 13 Z"/><line x1="7" y1="16" x2="17" y2="16"/></svg>',
"boot": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3 V13 L13 15 H20 A1 1 0 0 1 21 16 V18 H4 V13 Q4 11 6 11 H9"/></svg>',
"iron": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17 Q3 9 11 8 H16 A4 4 0 0 1 20 12 Q20 14 18 15 L20 17 Z"/><line x1="8" y1="5" x2="11" y2="8"/></svg>',
"wheelbarrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 10 H18 L16 16 H8 Z"/><circle cx="7" cy="19" r="2"/><line x1="9" y1="16" x2="7" y2="19"/><line x1="2" y1="10" x2="6" y2="10"/><line x1="2" y1="17" x2="2" y2="10"/></svg>',
}

def icon(name):
    return ICONS[name]

PAGES = [
    dict(file="index.html", nav="Home Page"),
    dict(file="rules-of-the-game.html", nav="What Is Capitalism?"),
    dict(file="manufacturing-the-consumer.html", nav="Manufacturing the Consumer"),
    dict(file="the-states-hand.html", nav="The State's Hand in the Market"),
    dict(file="capitalism-without-borders.html", nav="Capitalism Without Borders"),
    dict(file="bankruptcy.html", nav="Bankruptcy"),
]

def nav_html(current_file):
    items = ""
    for p in PAGES:
        active = ' class="active"' if p["file"] == current_file else ""
        items += f'<li><a href="{p["file"]}"{active}>{p["nav"]}</a></li>'
    return items

BOARD_STRIP = '<div class="board-strip"><span class="c1"></span><span class="c2"></span><span class="c3"></span><span class="c4"></span><span class="c5"></span><span class="c6"></span><span class="c7"></span><span class="c8"></span></div>'

def base(file, page_color, hero_class, hero_eyebrow, hero_icon, hero_title, hero_lede,
          badge_label, badge_icon, deed_line, body_html, fact_chip, sources_html=None):
    nav = nav_html(file)
    badge_icon_html = f'<span class="qmark">?</span>' if badge_icon == "qmark" else f'<span class="icon">{icon(badge_icon)}</span>'
    deed_html = f'<p class="hero-deed-line">{deed_line}</p>' if deed_line else ""
    sources_block = ""
    if sources_html:
        sources_block = f"""
<footer class="sources">
  <div class="sources-inner">
    <h3>Sources</h3>
    <p class="sources-sub">Covers every statistic, date, and named claim used across all six pages of this site.</p>
    <div class="sources-grid">
      <div>
        <h4>Course lecture slides</h4>
        <ol>{sources_html[0]}</ol>
      </div>
      <div>
        <h4>External sources</h4>
        <ol>{sources_html[1]}</ol>
      </div>
    </div>
  </div>
</footer>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{hero_title} | The Making of Capitalism — LSO440</title>
<meta name="description" content="{hero_lede[:150]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;0,9..144,900;1,9..144,600;1,9..144,800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body style="--page-color:{page_color};">
<nav class="topnav">
  <div class="topnav-inner">
    <a class="brand" href="index.html"><span class="diamond"></span>LSO440 / Globalization</a>
    <ul class="navlinks">{nav}</ul>
  </div>
</nav>

<header class="hero board-texture {hero_class}">
  <div class="hero-inner">
    <div class="hero-text">
      <p class="hero-eyebrow"><span class="icon">{icon(hero_icon)}</span>{hero_eyebrow}</p>
      <h1>{hero_title}</h1>
      <p class="lede">{hero_lede}</p>
      {deed_html}
    </div>
    <div class="corner-badge">
      {badge_icon_html}
      <span class="corner-badge-label">{badge_label}</span>
    </div>
  </div>
</header>
{BOARD_STRIP}

<main class="board-texture">
  <div class="layout">
    <div class="content-spine content">
      {body_html}
    </div>
    <aside class="factrail">
      <div class="fact-chip">
        <p class="fact-chip-label">{fact_chip[0]}</p>
        <p class="fact-chip-value">{fact_chip[1]}</p>
        <p class="fact-chip-note">{fact_chip[2]}</p>
      </div>
    </aside>
  </div>
</main>
{sources_block}
<p class="sitefoot">LSO440 Individual Website Project &mdash; Capitalism, told through the game of Monopoly</p>
</body>
</html>
"""

def divider(icon_name):
    return f'<div class="divider">{icon(icon_name)}<span class="rule"></span></div>'

def card(label, icon_name, quote):
    return f"""<div class="card">
      <div class="card-head">
        <span class="card-icon">{icon(icon_name)}</span>
        <span class="card-label">{label}</span>
      </div>
      <p class="card-quote">&ldquo;{quote}&rdquo;</p>
    </div>"""

def src(text, url=None, note=None):
    inner = f'<a href="{url}" target="_blank" rel="noopener">{text}</a>' if url else text
    n = f'<span class="note">{note}</span>' if note else ""
    return f"<li>{inner}{n}</li>"

# ---------------- PAGE 1: HOME ----------------
home_body = f"""
<p>This site walks through the real economy using Monopoly, since the game was basically built to explain property and profit. Nobody questions the rules once a board game starts &mdash; capitalism works the same way. Six pages, six mechanics: the rules, the desire to play, the banker, the trades, and the ending you probably already saw coming.</p>

{divider("tophat")}
<h2 class="section-title">Choose Your Player</h2>
<p>The pieces alone tell you something about class before anyone rolls a die. When Parker Brothers introduced metal tokens in 1937, three of them stood for wealth and leisure. Four more were working-class tools. Everyone still starts with the same $1,500 no matter which one they pick.</p>

<div class="tokens">
  <div class="token-group">
    <p class="token-group-label">The Wealthy</p>
    <div class="token-row">
      <div class="token"><span class="token-icon">{icon('tophat')}</span><span class="token-name">Top Hat</span></div>
      <div class="token"><span class="token-icon">{icon('car')}</span><span class="token-name">Car</span></div>
      <div class="token"><span class="token-icon">{icon('dog')}</span><span class="token-name">Dog</span></div>
    </div>
  </div>
  <div class="token-group">
    <p class="token-group-label">The Working Class</p>
    <div class="token-row">
      <div class="token"><span class="token-icon">{icon('thimble')}</span><span class="token-name">Thimble</span></div>
      <div class="token"><span class="token-icon">{icon('boot')}</span><span class="token-name">Boot</span></div>
      <div class="token"><span class="token-icon">{icon('iron')}</span><span class="token-name">Iron</span></div>
      <div class="token"><span class="token-icon">{icon('wheelbarrow')}</span><span class="token-name">Wheelbarrow</span></div>
    </div>
  </div>
</div>

{card("Choose Your Player", "tophat", "The board doesn&rsquo;t care what your token represents, only what you can afford to do next.")}

{divider("house")}
<h2 class="section-title">The Real History of the Landlord&rsquo;s Game</h2>
<p>Monopoly wasn&rsquo;t built to be played the way we play it now. Around 1902&ndash;1903, a Washington, D.C. stenographer named Elizabeth &ldquo;Lizzie&rdquo; Magie designed a board game called <em>The Landlord&rsquo;s Game</em> and patented it on January 5, 1904. Magie followed Henry George&rsquo;s theory of Georgism &mdash; the idea that land, unlike labor or capital, shouldn&rsquo;t be privately profited from, since nobody actually creates land. Her game was meant to make that argument playable.</p>
<p>The original board actually had two rulesets. Under the &ldquo;Prosperity&rdquo; rules, rent collected from developed land went into a shared pot, and everyone&rsquo;s fortunes rose together. Under the &ldquo;Monopolist&rdquo; rules &mdash; the version we still play &mdash; the goal was to bankrupt everyone else and own it all. Magie wanted people to play both back to back and feel which system actually worked better.</p>
<p>It never took off under her name. She self-published it and pitched it to Parker Brothers in 1909, who turned it down for being too political and too complicated. So it spread the slow way &mdash; hand-drawn copies passed through Quaker communities in Atlantic City and college economics classes across the Northeast. A Wharton professor named Scott Nearing even used it to teach students about the flaws of industrial capitalism, until he was fired in 1915 for exactly that kind of thing.</p>
<p>By the early 1930s, an unemployed Philadelphia salesman named Charles Darrow learned a hand-copied version from friends, redrew it with Atlantic City street names, and started selling it as his own. He patented it, sold it to Parker Brothers in 1935, and got credited as Monopoly&rsquo;s sole inventor. Parker Brothers knew about Magie&rsquo;s original patent &mdash; they just bought it from her quietly for about $500 flat, no royalties, and let her disappear from the story for decades.</p>
<p>Her name didn&rsquo;t resurface publicly until 1973, when Parker Brothers sued economics professor Ralph Anspach over his own game, <em>Anti-Monopoly</em>. Building his defense, Anspach dug up Magie&rsquo;s 1904 patent, and her role finally made it into the record &mdash; first legal, then public.</p>
"""

home_sources_lecture = "\n".join([
    src("Coloma-Moya, N. (2026, May 18). <em>LSO440 Week 3 Lecture: Capitalism, the State, and Transnational Corporations</em> [PowerPoint slides]. Seneca Polytechnic."),
    src("Coloma-Moya, N. (2026, May 25). <em>LSO440 Week 4 Lecture: Neoliberalism and Global Inequality</em> [PowerPoint slides]. Seneca Polytechnic."),
])
home_sources_external = "\n".join([
    src("Cool Material. (n.d.). The story behind each Monopoly piece.", "https://coolmaterial.com/lifestyle/entertainment/the-story-behind-monopoly-pieces/", "Token history"),
    src("National Women&rsquo;s History Museum. (n.d.). Monopoly&rsquo;s lost female inventor.", "https://www.womenshistory.org/articles/monopolys-lost-female-inventor", "Magie biography, rulesets, Parker Brothers acquisition"),
    src("Pilon, M. (2015, April 11). The secret history of Monopoly. <em>The Guardian</em>.", "https://www.theguardian.com/lifeandstyle/2015/apr/11/secret-history-monopoly-capitalist-game-leftwing-origins", "Anspach lawsuit, 1973 rediscovery"),
    src("CUNY Graduate Center. (2019, June 6). Capitalism and Democracy: Can They Coexist? [Video]. YouTube.", "https://www.youtube.com/watch?v=oXJfXweo1dM", "Background context"),
])

# ---------------- PAGE 2: RULES ----------------
rules_body = f"""
<p>Monopoly&rsquo;s basic rule is simple: a few players own properties, everyone else pays to land on them. That&rsquo;s more or less how capitalism works too. It&rsquo;s a mode of production built on private ownership of factories, land, and equipment, which means most people end up selling their labor for a wage instead of owning a piece of what they make.</p>

{divider("money")}
<p>That&rsquo;s not a one-time trade, it&rsquo;s a loop. Something gets made, sold for more than it cost, and the profit gets reinvested to keep the cycle going &mdash; what economists call capital accumulation. Monopoly runs the same loop: collect rent, build houses and hotels, collect more rent. Everyone starts with the same $1,500, but the board is designed so ownership snowballs once it gets moving.</p>

{card("The Rules", "dice", "Ownership snowballs once it gets moving.")}

<p>Three positions come out of that cycle. Capitalists accumulate profit. Laborers accumulate wages. Consumers accumulate goods. None of that comes down to talent or effort &mdash; it&rsquo;s baked into the rules before anyone even sits down at the board. That&rsquo;s why owning one full color set, which doubles rent on undeveloped property, puts you on a completely different track than someone still paying rent square by square.</p>
"""

# ---------------- PAGE 3: CONSUMER ----------------
consumer_body = f"""
<p>Nobody sits down to a Monopoly game already wanting Boardwalk. That desire gets built roll by roll, the same way American consumers were taught to want things they didn&rsquo;t know they needed. Nineteenth-century culture actually pushed the opposite &mdash; frugality, saving, buying only what you needed. Early department stores reflected that too: goods were just stock, stacked with no real thought behind it.</p>

{divider("tag")}
<p>That changed in 1902, when Marshall Field&rsquo;s in Chicago started arranging its store around making goods look desirable, not just available. The department store stopped selling what people needed and started teaching them what to want &mdash; how to dress, how to decorate, how to spend free time. National ads picked up the same job soon after, and TV took it even further.</p>

{card("Manufactured Desire", "tag", "The desire was designed in long before anyone thought they chose it.")}

<p>It didn&rsquo;t stop at retail. Universities built whole programs around business and marketing. Museums shifted their missions to fit a culture built on buying. Even the family, as an institution, picked up the job of teaching kids what was worth wanting. Boardwalk sits at the top of the board for the same reason a name-brand product sits at eye level on a shelf.</p>
"""

# ---------------- PAGE 4: STATE ----------------
state_body = f"""
<p>It&rsquo;s easy to think of the Banker as neutral, but the Banker sets loan terms, runs auctions, and hands out windfalls through Chance and Community Chest. That&rsquo;s basically what a state does inside capitalism &mdash; not standing outside the market, but shaping who gets to keep playing. A state, at its core, is the public institutions with authority over a territory: government, courts, police. In return for a working social contract, citizens accept the state&rsquo;s monopoly on legitimate force &mdash; the same authority the game hands the Banker.</p>

{divider("bank")}
<p>Historically, the American state did a lot more than referee. The Department of Commerce, set up in 1921, worked to boost merchandising and consumption nationwide. Homeownership got pushed as a basic American right. Credit expanded through interest-rate caps, truth-in-lending laws, and loans specifically opened up to women, minorities, and students who&rsquo;d been shut out before.</p>

{card("Legitimation", "chest", "The system is still basically fair, even when it isn&rsquo;t working in your favor.")}

<p>This work splits into two jobs. The accumulation function backs business directly: regulating trade, training workers, building infrastructure. The legitimation function is quieter &mdash; keeping people convinced the whole system is fair and natural, mostly through law, policing, and culture. A Chance card fining you for street repairs and a Community Chest card handing you a small inheritance are both doing legitimation work in miniature.</p>
"""

# ---------------- PAGE 5: GLOBAL ----------------
global_body = f"""
<p>The real power moves in Monopoly happen through trades &mdash; one player consolidating a whole color set by dealing across the board instead of waiting to land on every square. Transnational corporations do the same thing at a much bigger scale, growing past what any single country can hold by cutting deals that concentrate ownership beyond what any one &ldquo;square&rdquo; could manage alone.</p>

{divider("handshake")}
<p>That shift runs on real infrastructure. The IMF, World Bank, and WTO all came out of the post-WWII Bretton Woods system, built specifically to manage a global economy. The IMF hands out loans through Structural Adjustment Programmes, tied to opening trade and cutting public spending. The WTO, set up in 1995 to replace GATT, exists to negotiate and enforce open trade rules between countries.</p>

{card("Trading Across Borders", "train", "Trading a full color set takes one good conversation. Trading across the real board takes years of exactly that kind of relationship.")}

<p>Then there are the informal networks &mdash; private councils like the World Economic Forum, which one scholar called a &ldquo;consciousness-raising&rdquo; space: not a secret government, just a place where the same small group of state and corporate figures get to know and influence each other over time.</p>
"""

# ---------------- PAGE 6: BANKRUPTCY ----------------
bankruptcy_body = f"""
<p>Every Monopoly game ends the same way &mdash; one player owns everything, everyone else is bankrupt, fully out, not just behind. That&rsquo;s not a glitch, it&rsquo;s the point of the rules. The real economy has followed a similar path since the 1970s: the income gap between world regions now sits around 19 to 1, up from as low as 13 to 1. Between individual countries, it&rsquo;s gone from about 3 to 1 in the 1800s to somewhere around 72 to 1 today.</p>

{divider("scale")}
<p>Sociologist Manuel Castells tracked a similar shift in global income shares: between the 1960s and 1990s, the poorest 20% of the world went from holding 2.3% of global income to just 1.4%, while the richest 20% climbed from 70% to 85%. Consumption tells the same story &mdash; the wealthiest fifth accounts for about 86% of all private spending, the poorest fifth just 1.3%. That same top fifth eats 45% of the world&rsquo;s meat and fish and burns 58% of its energy; the poorest fifth gets 5% and 4%.</p>

{card("The Rules of the Game", "dice", "Growth doesn&rsquo;t lift every player. It was never built to.")}

<p>None of this is an accident, and it&rsquo;s not a bug in an otherwise fair system. It follows straight from everything on the earlier pages: a system built to manufacture demand, backed by a state that makes it feel natural, scaled by institutions that answer to a narrow elite.</p>

<div class="reflection">Where do you land in this system &mdash; producer, consumer, or both? If bankruptcy in Monopoly is a design choice and not an accident, what would it take to design the real version differently?</div>
"""

pages_out = [
    dict(file="index.html", color="var(--green)", hero_class="", eyebrow="Home Page &middot; Welcome to Monopoly", hero_icon="dice",
         title="Roll the Dice. Someone Always Owns the Board.",
         lede="This site walks through the real economy using Monopoly, since the game was basically built to explain property and profit.",
         badge_label="GO", badge_icon="arrow", deed_line=None,
         body=home_body, fact_chip=("Six Pages", "1904 &rarr; Now", "From Magie&rsquo;s patent to the modern board"),
         sources=(home_sources_lecture, home_sources_external)),

    dict(file="rules-of-the-game.html", color="var(--blue)", hero_class="", eyebrow="What Is Capitalism? &middot; The Rules of the Game", hero_icon="dice",
         title="The Rules of the Game",
         lede="A few players own properties. Everyone else pays to land on them. That&rsquo;s capitalism, in miniature.",
         badge_label="Title Deed", badge_icon="card", deed_line="This certifies that private ownership entitles the holder to collect rent from all who land here.",
         body=rules_body, fact_chip=("Starting Cash", "$1,500", "Same for every player, regardless of position"),
         sources=None),

    dict(file="manufacturing-the-consumer.html", color="var(--orange)", hero_class="hero--chance", eyebrow="Manufacturing the Consumer &middot; Why You Want to Land on Boardwalk", hero_icon="tag",
         title="Why You Want to Land on Boardwalk",
         lede="Nobody starts the game wanting Boardwalk. They&rsquo;re taught to, roll by roll.",
         badge_label="Chance", badge_icon="qmark", deed_line=None,
         body=consumer_body, fact_chip=("Top Property", "$400", "Boardwalk&rsquo;s face value on the classic board"),
         sources=None),

    dict(file="the-states-hand.html", color="var(--teal)", hero_class="hero--ledger", eyebrow="The State&rsquo;s Hand in the Market &middot; Chance, Community Chest &amp; the Banker", hero_icon="bank",
         title="Chance, Community Chest &amp; the Banker",
         lede="The Banker was never a neutral referee. Neither is the state.",
         badge_label="Community Chest", badge_icon="chest", deed_line=None,
         body=state_body, fact_chip=("Established", "1921", "U.S. Department of Commerce"),
         sources=None),

    dict(file="capitalism-without-borders.html", color="var(--red)", hero_class="hero--rail", eyebrow="Capitalism Without Borders &middot; Trading Across the Board", hero_icon="train",
         title="Trading Across the Board",
         lede="The biggest moves in Monopoly happen through trades. So does global capitalism.",
         badge_label="Railroad", badge_icon="train", deed_line=None,
         body=global_body, fact_chip=("Railroads", "4", "The board&rsquo;s only cross-network property group"),
         sources=None),

    dict(file="bankruptcy.html", color="var(--navy)", hero_class="hero--stamp", eyebrow="Bankruptcy &middot; Winners, Losers, and Inequality", hero_icon="scale",
         title="Bankruptcy",
         lede="Every game of Monopoly ends with one winner and everyone else bankrupt. That&rsquo;s not an accident.",
         badge_label="Go To Jail", badge_icon="jail", deed_line=None,
         body=bankruptcy_body, fact_chip=("Income Gap", "72:1", "Between the richest and poorest countries today"),
         sources=None),
]

os.makedirs(OUT, exist_ok=True)
for p in pages_out:
    html = base(p["file"], p["color"], p["hero_class"], p["eyebrow"], p["hero_icon"], p["title"], p["lede"],
                p["badge_label"], p["badge_icon"], p["deed_line"], p["body"], p["fact_chip"], p["sources"])
    with open(os.path.join(OUT, p["file"]), "w") as f:
        f.write(html)
    print("wrote", p["file"])
