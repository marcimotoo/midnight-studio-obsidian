"""Render illustrative README examples using the actual theme palette.

Requires Python and Pillow; uses Windows Segoe UI and Consolas fonts.
"""

from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "theme.css").read_text(encoding="utf-8")
VALUES = dict(re.findall(r"--([\w-]+):\s*([^;]+);", CSS))
FONTS = Path("C:/Windows/Fonts")


def color(name):
    value = VALUES[name].strip()
    if value.startswith("var("):
        return color(value[6:-1])
    if len(value) == 9 and value.startswith("#"):
        alpha = int(value[7:9], 16) / 255
        background = VALUES["background-primary"]
        return tuple(round(int(value[i:i + 2], 16) * alpha + int(background[i:i + 2], 16) * (1 - alpha)) for i in (1, 3, 5))
    return value


def font(size=26, bold=False, mono=False):
    return ImageFont.truetype(str(FONTS / ("consola.ttf" if mono else "segoeuib.ttf" if bold else "segoeui.ttf")), size)


def preview(title, subtitle, active):
    image = Image.new("RGB", (1800, 1200), color("background-secondary"))
    draw = ImageDraw.Draw(image)

    def text(x, y, value, role="text-normal", size=26, bold=False, mono=False):
        draw.text((x, y), value, fill=color(role), font=font(size, bold, mono))

    def box(bounds, role, radius=8, outline=None):
        draw.rounded_rectangle(bounds, radius, fill=color(role), outline=color(outline) if outline else None, width=2)

    text(54, 34, "MIDNIGHT STUDIO", "midnight-mint", 22, True)
    text(54, 78, title, "h1-color", 44, True)
    text(54, 145, subtitle, "text-muted", 24)
    box((44, 212, 1756, 1082), "background-primary", outline="background-modifier-border")
    draw.rectangle((46, 214, 348, 1080), fill=color("background-secondary"))
    draw.line((348, 214, 348, 1080), fill=color("divider-color"), width=2)
    text(76, 252, "DEMO VAULT", "nav-heading-color", 20, True)
    for index, label in enumerate(["Welcome", "Project notes", "Components", "Archive"]):
        y = 310 + index * 62
        if label == active:
            box((65, y - 8, 325, y + 45), "background-primary-alt")
            draw.rectangle((65, y - 8, 69, y + 45), fill=color("midnight-mint"))
        text(92, y, label, "nav-item-color-active" if label == active else "nav-item-color", 24)
    draw.rectangle((350, 214, 1753, 278), fill=color("tab-container-background"))
    box((372, 219, 662, 279), "tab-background-active", radius=5)
    draw.line((380, 220, 654, 220), fill=color("midnight-mint"), width=3)
    text(399, 231, active, "tab-text-color-active", 23)
    text(399, 300, "Notes  /  " + active, "text-faint", 20)
    text(54, 1130, "GENERATED EXAMPLE  •  Colors taken from theme.css", "text-muted", 22)
    text(1240, 1130, "Dark surfaces. Clear accents.", "text-faint", 22)
    return image, draw, text, box


image, draw, text, box = preview("A calm space for your notes", "Navigation, typography, links and tasks — with a precise #00FF99 accent.", "Welcome")
text(408, 355, "Make room for your ideas.", "inline-title-color", 46, True)
text(410, 432, "A quiet workspace for planning, writing and connecting your thoughts.", size=25)
for x, label, width in [(410, "#notes", 112), (540, "#creative", 140), (697, "#planning", 153)]:
    box((x, 488, x + width, 529), "background-primary-alt", outline="tag-border-color")
    text(x + 12, 492, label, "tag-color", 22)
text(410, 568, "Today's focus", "h2-color", 32, True)
for index, (label, done) in enumerate([("Capture one useful idea", True), ("Connect it to your project notes", False), ("Choose the next small step", False)]):
    y = 632 + index * 58
    box((412, y + 5, 438, y + 31), "checkbox-color" if done else "background-primary", radius=3, outline=None if done else "checkbox-border-color")
    if done:
        draw.line([(418, y + 18), (424, y + 24), (434, y + 11)], fill=color("checkbox-marker-color"), width=3)
    text(455, y, label, "checklist-done-color" if done else "text-normal", 26)
text(410, 827, "Follow the connection", "h2-color", 32, True)
text(410, 883, "Open Project notes", "link-color", 27)
draw.line((410, 921, 635, 921), fill=color("link-color"), width=1)
draw.line((410, 963, 410, 1030), fill=color("blockquote-border-color"), width=3)
text(432, 978, "Good notes make the next step easier.", "blockquote-color", 27)
(ROOT / "images").mkdir(exist_ok=True)
image.save(ROOT / "images/overview.png")

image, draw, text, box = preview("The details, thoughtfully balanced", "Tables, callouts and code — soft secondary colors keep content readable.", "Components")
text(407, 355, "Useful building blocks", "inline-title-color", 43, True)
box((409, 431, 1020, 690), "background-primary", outline="table-border-color")
draw.rectangle((411, 433, 1018, 487), fill=color("table-header-background"))
text(432, 441, "Element", "table-header-color", 24, True)
text(734, 441, "Purpose", "table-header-color", 24, True)
for index, (a, b) in enumerate([("Links", "Connect ideas"), ("Tasks", "Track progress"), ("Callouts", "Highlight context")]):
    y = 497 + index * 62
    text(432, y, a, size=24)
    text(734, y, b, "text-muted", 24)
    if index < 2:
        draw.line((410, y + 51, 1019, y + 51), fill=color("table-border-color"), width=1)
for y, title, body, role in [(722, "TIP", "Keep related notes close together.", "color-cyan"), (870, "WARNING", "Check your assumptions before acting.", "color-yellow")]:
    box((409, y, 1020, y + 120), "background-primary-alt", outline="background-modifier-border")
    draw.rectangle((410, y + 5, 414, y + 115), fill=color(role))
    text(432, y + 15, title, role, 23, True)
    text(432, y + 59, body, size=24)
box((1050, 431, 1700, 794), "code-background", outline="background-modifier-border")
text(1075, 448, "JAVASCRIPT", "text-faint", 19, True)
lines = [
    [("// Small steps, clear intent", "code-comment")],
    [("const ", "code-keyword"), ("note ", "code-normal"), ("= ", "code-operator"), ('"A new idea"', "code-string"), (";", "code-normal")],
    [("const ", "code-keyword"), ("progress ", "code-normal"), ("= ", "code-operator"), ("3", "code-value"), (";", "code-normal")],
    [],
    [("function ", "code-keyword"), ("capture", "code-function"), ("(title) {", "code-normal")],
    [("  return ", "code-keyword"), ("{ ", "code-normal"), ("title", "code-property"), (", ", "code-normal"), ("done", "code-property"), (": ", "code-operator"), ("false", "code-value"), (" };", "code-normal")],
    [("}", "code-normal")],
]
for index, spans in enumerate(lines):
    x, y = 1075, 493 + index * 37
    for value, role in spans:
        text(x, y, value, role, 23, mono=True)
        x += draw.textlength(value, font=font(23, mono=True))
for index, (label, role) in enumerate([("Keywords", "code-keyword"), ("Functions", "code-function"), ("Strings", "code-string"), ("Numbers / values", "code-value"), ("Properties", "code-property"), ("Comments", "code-comment")]):
    column, row = index % 2, index // 2
    x, y = 1070 + column * 310, 834 + row * 61
    box((x, y + 5, x + 27, y + 32), role, radius=4)
    text(x + 41, y, label, "text-muted", 23)
image.save(ROOT / "images/details.png")
