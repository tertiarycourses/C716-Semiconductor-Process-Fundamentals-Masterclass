"""C716 Learner Guide: explicit rewrite of the WSQ LG (TGS-2024051248) as the non-WSQ twin."""
import re, shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LG-Mastering Semiconductor Key Modules for Enhanced CMOS Process Integration and Device Performance - v9.0.docx"
OUT = "courseware/LG-Semiconductor Process Fundamentals Masterclass (C716).docx"
URL = "https://www.tertiarycourses.com.sg/semiconductor-process-fundamentals-masterclass.html"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)
retitle_all(d)

# Cover
set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C716")
set_text(para_by_text(d, "Version 9.0"), "Version 1.0 · 1 October 2026")

tables = d.tables
t0, t1 = tables[0], tables[1]

# Version control record -> single v1.0 row
for r in list(t0.rows)[2:]:
    t0._tbl.remove(r._tr)
set_cell(t0.rows[1].cells[0], "1.0")
set_cell(t0.rows[1].cells[1], "1 October 2026")
set_cell(t0.rows[1].cells[2], "Initial release of the Semiconductor Process Fundamentals Masterclass learner guide: "
         "four learning blocks and eight step-by-step activities.")
set_cell(t0.rows[1].cells[3], "Dr Alfred Ang")

# Course information: code, duration; drop TSC + Assessment rows
set_cell(t1.rows[2].cells[1], "C716")
set_cell(t1.rows[4].cells[1], "15 hours over 2 days (9:30am–5:30pm)")
for r in (t1.rows[5], t1.rows[3]):          # Assessment, TSC
    t1._tbl.remove(r._tr)

# Learning outcomes stay; the K/A competency criteria go
set_text(para_by_text(d, "Learning and Assessment Alignment"), "Learning Outcomes")
delete_range(d, "Knowledge and Ability Criteria", "Before You Start")

set_text(para_by_text(d, "The current v9.0 learner slides"), "The current v1.0 learner slides and this Learner Guide.")
set_text(para_by_text(d, "Access to the LMS for courseware"), "Access to the LMS for courseware download.")

# Activity tables: "LO1 · K1, A1, A2" -> "LO1"; PP references in goals
for t in tables[2:]:
    for row in t.rows:
        key, val = row.cells[0].text, row.cells[1].text
        if key == "Alignment":
            set_cell(row.cells[1], re.match(r"LO\d", val).group(0))
        elif "Practical Performance" in val:
            set_cell(row.cells[1], {
                "Produce the process-flow and challenge analysis used as the foundation for Practical Performance Task 1.":
                    "Produce the process-flow and challenge analysis for a shallow trench isolation integration.",
                "Recreate the legacy P-chart/SPC exercises and generate the corrective-action chain used in Practical Performance Task 2.":
                    "Recreate the legacy P-chart/SPC exercises and generate the corrective-action chain for a CD excursion.",
            }[val])

# Assessment Flow section (heading .. Support)
delete_range(d, "Assessment Flow", "Support")
sup = para_by_text(d, "Email enquiry@")
set_text(sup, f"Email enquiry@tertiaryinfotech.com or call +65 6100 0613. Course page: {URL}")

for s in d.sections:
    for part in (s.header, s.footer, s.first_page_footer, s.even_page_footer):
        for p in part.paragraphs:
            for r in p.runs:
                r.text = r.text.replace("TGS-2024051248", "C716")

d.core_properties.title = "LG-Semiconductor Process Fundamentals Masterclass"
d.core_properties.subject = "C716"
d.save(OUT)
print("saved", OUT)
