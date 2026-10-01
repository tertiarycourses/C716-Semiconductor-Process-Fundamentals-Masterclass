"""C716 Lesson Plan: explicit rewrite of the WSQ LP (TGS-2024051248) as the non-WSQ twin."""
import re, shutil, docx
from docxutil import *

SRC = "source-wsq/courseware/LP-Mastering Semiconductor Key Modules for Enhanced CMOS Process Integration and Device Performance - v9.0.docx"
OUT = "courseware/LP-Semiconductor Process Fundamentals Masterclass (C716).docx"
shutil.copy(SRC, OUT)
d = docx.Document(OUT)
retitle_all(d)

# Kept-slide map: source slides 2, 8, 9, 10, 13, 14, 15, 17, 132, 135, 136, 137 (1-based) were dropped.
DROPPED = [2, 8, 9, 10, 13, 14, 15, 17, 132, 135, 136, 137]
def m(n):
    n = int(n)
    assert n not in DROPPED, n
    return str(n - sum(1 for x in DROPPED if x < n))
def remap(text):
    return re.sub(r"\b\d+", lambda mo: m(mo.group(0)), text)

# Cover
set_text(para_by_text(d, "TGS Ref No:"), "Course Code: C716")
set_text(para_by_text(d, "Version 9.0"), "Version 1.0 · 1 October 2026")

t0, t1, t2, t3 = d.tables

# Version control record -> single v1.0 row
for r in list(t0.rows)[2:]:
    t0._tbl.remove(r._tr)
set_cell(t0.rows[1].cells[0], "1.0")
set_cell(t0.rows[1].cells[1], "1 October 2026")
set_cell(t0.rows[1].cells[2], "Initial release of the Semiconductor Process Fundamentals Masterclass lesson plan: two-day "
         "schedule (9:30am–5:30pm, 15 instructional hours), four learning blocks and eight activities.")
set_cell(t0.rows[1].cells[3], "Dr Alfred Ang")

# Overview
set_text(para_by_text(d, "This two-day WSQ course"),
         "This two-day course develops the ability to identify CMOS technology process flows, analyse cross-module "
         "interactions, determine device and reliability performance, verify integration against product specifications "
         "and define accountable follow-up action. The deck organises the two topics into four visual learning blocks.")

# Course information: drop TSC + Assessment rows, code, duration
set_cell(t1.rows[2].cells[1], "C716")
set_cell(t1.rows[3].cells[1], "15 hours over 2 days (9:30am–5:30pm, 7.5 instructional hours per day)")
for r in (t1.rows[4], t1.rows[1]):          # Assessment, TSC
    t1._tbl.remove(r._tr)

# Schedules: 9:30am-5:30pm, 450 min teaching + one 30-min lunch per day.
# WSQ teaching blocks rescaled proportionally onto 450 min; the 10-min teas and 45-min lunch become one 30-min lunch.
s2 = [[c.text for c in r.cells] for r in t2.rows]
s3 = [[c.text for c in r.cells] for r in t3.rows]
rebuild_rows(t2, [
    (1, ["9:30-9:50", "20 min", "Introductions, learning outcomes and course overview", s2[1][3], "Slides 1-10"]),
    (2, ["9:50-10:55", "65 min", s2[2][2], s2[2][3], remap(s2[2][4])]),
    (4, ["10:55-11:40", "45 min", s2[4][2], s2[4][3], remap(s2[4][4])]),
    (5, ["11:40-12:40", "60 min", s2[5][2], s2[5][3], remap(s2[5][4])]),
    (6, ["12:40-1:10", "30 min", "Lunch", "Break", "-"]),
    (7, ["1:10-2:30", "80 min", s2[7][2], s2[7][3], remap(s2[7][4])]),
    (9, ["2:30-3:25", "55 min", s2[9][2], s2[9][3], remap(s2[9][4])]),
    (10, ["3:25-4:20", "55 min", s2[10][2], s2[10][3], remap(s2[10][4])]),
    (11, ["4:20-5:30", "70 min", s2[11][2], s2[11][3], remap(s2[11][4])]),
])
rebuild_rows(t3, [
    (1, ["9:30-9:50", "20 min", "Day 1 retrieval", s3[1][3], "-"]),
    (2, ["9:50-11:20", "90 min", s3[2][2], s3[2][3], remap(s3[2][4])]),
    (4, ["11:20-12:20", "60 min", s3[4][2], s3[4][3], remap(s3[4][4])]),
    (6, ["12:20-12:50", "30 min", "Lunch", "Break", "-"]),
    (5, ["12:50-2:05", "75 min", s3[5][2], s3[5][3], remap(s3[5][4])]),
    (7, ["2:05-3:20", "75 min", s3[7][2], s3[7][3], remap(s3[7][4])]),
    (8, ["3:20-4:10", "50 min", s3[8][2], s3[8][3], remap(s3[8][4])]),
    (9, ["4:10-5:00", "50 min", s3[9][2], s3[9][3], remap(s3[9][4])]),
    (10, ["5:00-5:30", "30 min", "Course synthesis, review and feedback", "Q&A and wrap-up", "Slides 122-126"]),
])

# Topic / block / activity headings: remap slide refs
for p in d.paragraphs:
    if p.style.name in ("Heading 2", "Heading 3") and "Slide" in p.text:
        head, refs = p.text.rsplit("·", 1)
        set_text(p, head + "·" + remap(refs))

# Activity notes that referenced the Practical Performance tasks
set_text(para_by_text(d, "Produce the process-flow and challenge analysis"),
         "Produce the process-flow and challenge analysis for a shallow trench isolation integration.")
set_text(para_by_text(d, "Recreate the legacy P-chart/SPC exercises"),
         "Recreate the legacy P-chart/SPC exercises and generate the corrective-action chain for a CD excursion.")

# Resources
set_text(para_by_text(d, "v9.0 PowerPoint/PDF learner slides"), "v1.0 PowerPoint/PDF learner slides")
set_text(para_by_text(d, "v9.0 Learner Guide"), "v1.0 Learner Guide")
set_text(para_by_text(d, "LMS access for courseware"), "LMS access for courseware download")

# Assessment section (heading + 4 paragraphs) is the last block of the body
pars = d.paragraphs
i = next(k for k, p in enumerate(pars) if p.style.name == "Heading 1" and p.text == "Assessment")
for p in pars[i:]:
    delete(p)

# Footer / header
for s in d.sections:
    for part in (s.header, s.footer, s.first_page_footer, s.even_page_footer):
        for p in part.paragraphs:
            if "TGS-2024051248" in p.text:
                for r in p.runs:
                    r.text = r.text.replace("TGS-2024051248", "C716")

d.core_properties.title = "LP-Semiconductor Process Fundamentals Masterclass"
d.core_properties.subject = "C716"
d.save(OUT)
print("saved", OUT)
