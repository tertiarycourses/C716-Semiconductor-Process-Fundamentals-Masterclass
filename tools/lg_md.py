"""Write the LG Markdown mirror from the converted LG DOCX."""
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph
SRC = "courseware/LG-Semiconductor Process Fundamentals Masterclass (C716).docx"
OUT = "LG-Semiconductor Process Fundamentals Masterclass (C716).md"
d = docx.Document(SRC)
out, n, started = ["# Learner Guide — Semiconductor Process Fundamentals Masterclass (C716)", "",
                   "Version 1.0 · 1 October 2026 · Tertiary Infotech Academy Pte Ltd", ""], 0, False
for el in d.element.body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag == 'p':
        p = Paragraph(el, d); t = p.text.strip(); s = p.style.name
        if s == "Heading 1" and t == "How to Use This Guide": started = True
        if not started or not t: continue
        if s.startswith("Heading"):
            out += ["", "#" * (int(s[-1]) + 1) + " " + t, ""]; n = 0
        elif s == "List Number":
            n += 1; out.append(f"{n}. {t}")
        elif s == "List Bullet":
            out.append(f"- {t}")
        else:
            out += [t, ""]; n = 0
    elif tag == 'tbl' and started:
        rows = [[c.text.replace("\n", " ").replace("|", "/") for c in r.cells] for r in Table(el, d).rows]
        out += ["", "| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
        out += ["| " + " | ".join(r) + " |" for r in rows[1:]] + [""]
open(OUT, "w").write("\n".join(out).replace("\n\n\n", "\n\n") + "\n")
print(OUT)
