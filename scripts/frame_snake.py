"""Recolour and frame the snake SVG produced by Platane/snk.

Usage: python3 scripts/frame_snake.py <input.svg> <output.svg>
The snake colours are CSS variables on :root, so they are replaced in place;
a rounded burgundy background and padding are added around the grid.
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
svg = open(src, encoding="utf-8").read()

COLORS = {
    "--cb": "#451126", "--cs": "#E5B5C7", "--ce": "#22101A",
    "--c0": "#4A1529", "--c1": "#4A1529", "--c2": "#7A1F45", "--c3": "#B04A77", "--c4": "#E5B5C7",
}
root = re.search(r":root\{([^}]*)\}", svg)
if root:
    body = root.group(1)
    for k, v in COLORS.items():
        body = re.sub(rf"{re.escape(k)}:[^;}}]+", f"{k}:{v}", body)
    svg = svg.replace(root.group(0), f":root{{{body}}}", 1)

m = re.match(r'<svg viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)" width="[\d.]+" height="[\d.]+"', svg)
if m:
    x, y, w, h = (float(v) for v in m.groups())
    pad = 28
    nx, ny, nw, nh = x - pad, y - pad, w + 2 * pad, h + 2 * pad
    head_end = svg.index(">") + 1
    head = f'<svg viewBox="{nx:g} {ny:g} {nw:g} {nh:g}" width="{nw:g}" height="{nh:g}" xmlns="http://www.w3.org/2000/svg">'
    bg = (f'<rect x="{nx:g}" y="{ny:g}" width="{nw:g}" height="{nh:g}" rx="16" fill="#10070C"/>'
          f'<rect x="{nx+0.5:g}" y="{ny+0.5:g}" width="{nw-1:g}" height="{nh-1:g}" rx="16" fill="none" stroke="#451126"/>')
    svg = head + bg + svg[head_end:]

open(dst, "w", encoding="utf-8").write(svg)
print("wrote", dst)
