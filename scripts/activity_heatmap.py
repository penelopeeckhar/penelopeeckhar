"""Render the GitHub contribution calendar as a burgundy SVG heatmap.

Run by .github/workflows/snake.yml every day:
    GITHUB_TOKEN=... python3 scripts/activity_heatmap.py <login> <output.svg>

Data comes from the GitHub GraphQL API (contributionCalendar); nothing is invented.
For a local design preview only: python3 scripts/activity_heatmap.py --demo <output.svg>
"""
import datetime as dt
import json
import os
import random
import sys
import urllib.request

MID, WINE_DARK, BURG, WINE = "#10070C", "#190B12", "#451126", "#701A3D"
ROSE, PALE, IVORY = "#C77B9B", "#E5B5C7", "#F8F0F3"
LEVELS = ["#22101A", "#4A1529", "#7A1F45", "#B04A77", "#E5B5C7"]
SERIF = "Georgia, 'Times New Roman', serif"
MONO = "'JetBrains Mono', Consolas, 'Courier New', monospace"
SANS = "'Segoe UI', Helvetica, Arial, sans-serif"

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionCount}}}}}}"""


def fetch(login):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [[(d["date"], d["contributionCount"]) for d in w["contributionDays"]] for w in cal["weeks"]]
    return weeks, cal["totalContributions"]


def demo():
    rnd = random.Random(7)
    start = dt.date.today() - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)
    weeks, day = [], start
    while day <= dt.date.today():
        w = []
        for _ in range(7):
            if day <= dt.date.today():
                w.append((day.isoformat(), max(0, int(rnd.gauss(2, 3)))))
            day += dt.timedelta(days=1)
        weeks.append(w)
    return weeks, sum(c for w in weeks for _, c in w)


def stats(weeks):
    days = [(d, c) for w in weeks for d, c in w]
    longest = cur = run = 0
    for _, c in days:
        run = run + 1 if c else 0
        longest = max(longest, run)
    tail = days[:-1] if days and days[-1][1] == 0 else days  # today not over yet
    for _, c in reversed(tail):
        if not c:
            break
        cur += 1
    active = sum(1 for _, c in days if c)
    return longest, cur, active


def level(c, peak):
    if c == 0:
        return 0
    q = c / peak if peak else 0
    return 1 if q <= 0.25 else 2 if q <= 0.5 else 3 if q <= 0.75 else 4


def render(weeks, total, demo_mode=False):
    p = "pac"
    W, H = 1200, 420
    cell, gap = 16, 4
    gx, gy = 70, 196
    peak = max((c for w in weeks for _, c in w), default=0)
    longest, current, active = stats(weeks)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="{p}-t">',
           f'<title id="{p}-t">Contribution activity: {total} contributions in the last year, longest streak {longest} days</title>',
           f'''<defs>
  <linearGradient id="{p}-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{MID}"/><stop offset="0.6" stop-color="{WINE_DARK}"/><stop offset="1" stop-color="#240A16"/></linearGradient>
  <linearGradient id="{p}-rule" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ROSE}"/><stop offset="1" stop-color="{WINE}" stop-opacity="0"/></linearGradient>
  <linearGradient id="{p}-scan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PALE}" stop-opacity="0"/><stop offset="0.5" stop-color="{PALE}" stop-opacity="0.12"/><stop offset="1" stop-color="{PALE}" stop-opacity="0"/></linearGradient>
  <filter id="{p}-cg" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>
  <filter id="{p}-sg" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="2.5"/></filter>
  <clipPath id="{p}-clip"><rect width="{W}" height="{H}" rx="16"/></clipPath>
</defs>''',
           f'<g clip-path="url(#{p}-clip)"><rect width="{W}" height="{H}" fill="url(#{p}-bg)"/>',
           f'<text x="56" y="56" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{ROSE}">05 · ACTIVITY</text>',
           f'<text x="56" y="100" font-family="{SERIF}" font-size="34" fill="{IVORY}">A year of building, one square at a time.</text>',
           f'<rect x="56" y="116" width="160" height="2" fill="url(#{p}-rule)">'
           f'<animate attributeName="width" values="120;240;120" dur="6s" repeatCount="indefinite"/></rect>',
           f'<circle cx="56" cy="117" r="2.6" fill="{IVORY}"><animate attributeName="cx" values="56;286;56" dur="5s" repeatCount="indefinite"/>'
           f'<animate attributeName="opacity" values="0.2;1;0.2" dur="2.5s" repeatCount="indefinite"/></circle>']

    for i, (big, lab) in enumerate([(f"{total:,}", "contributions"), (str(active), "active days"),
                                    (str(longest), "longest streak"), (str(current), "current streak")]):
        x = 1144 - (3 - i) * 130
        out.append(f'<text x="{x}" y="80" text-anchor="end" font-family="{SERIF}" font-size="30" fill="{IVORY}">{big}</text>')
        out.append(f'<text x="{x}" y="102" text-anchor="end" font-family="{MONO}" font-size="11" fill="{ROSE}">{lab}</text>')

    for r, lab in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        out.append(f'<text x="{gx-12}" y="{gy + r*(cell+gap) + 12}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{PALE}" fill-opacity="0.6">{lab}</text>')

    last_month = None
    for wi, w in enumerate(weeks):
        x = gx + wi * (cell + gap)
        m = dt.date.fromisoformat(w[0][0]).strftime("%b")
        if m != last_month and wi < len(weeks) - 2:
            out.append(f'<text x="{x}" y="{gy-12}" font-family="{MONO}" font-size="11" fill="{PALE}" fill-opacity="0.6">{m}</text>')
            last_month = m
        for d, c in w:
            r = (dt.date.fromisoformat(d).weekday() + 1) % 7
            y = gy + r * (cell + gap)
            col = LEVELS[level(c, peak)]
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="{col}"><title>{d}: {c}</title></rect>')

    # snake: a short white trail winding through the grid, down one week, up the next
    pts = []
    for wi in range(len(weeks)):
        rows = range(7) if wi % 2 == 0 else range(6, -1, -1)
        pts += [(gx + wi * (cell + gap), gy + r * (cell + gap)) for r in rows]
    path = "M" + " L".join(f"{x},{y}" for x, y in pts)
    step = 0.11                      # seconds per cell
    dur = round(step * (len(pts) - 1), 2)
    trail = [(IVORY, 1.0), (IVORY, 0.85), (PALE, 0.7), (PALE, 0.5), (ROSE, 0.35)]
    n = len(trail)
    for k, (colr, op) in reversed(list(enumerate(trail))):
        begin = -(n - k) * step      # all segments already running, tail lags behind head
        glow = (f'<rect width="{cell}" height="{cell}" rx="4" fill="{IVORY}" opacity="0.6" filter="url(#{p}-sg)"/>'
                if k == 0 else "")
        out.append(f'<g>{glow}<rect width="{cell}" height="{cell}" rx="3.5" fill="{colr}" opacity="{op}"/>'
                   f'<animateMotion path="{path}" dur="{dur}s" begin="{begin:.2f}s" calcMode="linear" repeatCount="indefinite"/></g>')

    ly = gy + 7 * (cell + gap) + 26
    out.append(f'<text x="{gx}" y="{ly}" font-family="{MONO}" font-size="11" fill="{PALE}" fill-opacity="0.6">'
               f'{"design preview · sample data" if demo_mode else "live from GitHub · updated daily"}</text>')
    lx = 1144 - 5 * 20 - 40
    out.append(f'<text x="{lx-10}" y="{ly}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{PALE}" fill-opacity="0.6">less</text>')
    for i, c in enumerate(LEVELS):
        out.append(f'<rect x="{lx + i*20}" y="{ly-11}" width="14" height="14" rx="3" fill="{c}"/>')
    out.append(f'<text x="{lx + 5*20 + 4}" y="{ly}" font-family="{MONO}" font-size="11" fill="{PALE}" fill-opacity="0.6">more</text>')
    out.append(f'</g><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="{BURG}"/>')
    # comet: a short white streak racing around the border
    rr, x0, y0, w0, h0 = 15, 1, 1, W - 2, H - 2
    d = (f"M{x0+rr},{y0} H{x0+w0-rr} A{rr},{rr} 0 0 1 {x0+w0},{y0+rr} V{y0+h0-rr} A{rr},{rr} 0 0 1 {x0+w0-rr},{y0+h0} "
         f"H{x0+rr} A{rr},{rr} 0 0 1 {x0},{y0+h0-rr} V{y0+rr} A{rr},{rr} 0 0 1 {x0+rr},{y0} Z")
    anim = '<animate attributeName="stroke-dashoffset" values="1000;0" dur="4.8s" repeatCount="indefinite"/>'
    out.append(f'<path d="{d}" fill="none" stroke="{IVORY}" stroke-width="5" stroke-opacity="0.55" filter="url(#{p}-cg)" '
               f'pathLength="1000" stroke-dasharray="60 940" stroke-linecap="round">{anim}</path>')
    out.append(f'<path d="{d}" fill="none" stroke="{IVORY}" stroke-width="1.6" '
               f'pathLength="1000" stroke-dasharray="60 940" stroke-linecap="round">{anim}</path></svg>')
    return "\n".join(out)


if __name__ == "__main__":
    if sys.argv[1] == "--demo":
        weeks, total = demo()
        svg = render(weeks, total, demo_mode=True)
    else:
        weeks, total = fetch(sys.argv[1])
        svg = render(weeks, total)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    with open(sys.argv[2], "w") as f:
        f.write(svg)
    print("wrote", sys.argv[2])
