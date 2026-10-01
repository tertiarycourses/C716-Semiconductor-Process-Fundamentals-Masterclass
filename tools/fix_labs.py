"""C716 activities: rewrite the WSQ identity in every .md and edit the ReportLab PDFs' content streams in place."""
import re, glob, pypdf

OLD_T = "Mastering Semiconductor Key Modules for Enhanced CMOS Process Integration and Device Performance"
NEW_T = "Semiconductor Process Fundamentals Masterclass"
MIN = {"01": 45, "02": 60, "03": 55, "04": 55, "05": 60, "06": 75, "07": 50, "08": 50}
PP5 = ("used as the foundation for Practical Performance Task 1.", "for a shallow trench isolation integration.")
PP7 = ("used in Practical Performance Task 2.", "for a CD excursion.")
KA = r"(LO\d)(?:\s*[·|]\s*(?:[KA]\d+(?:,\s*)?)+)"

def act_no(path):
    mo = re.search(r"activity-(\d\d)-", path)
    return mo.group(1) if mo else None

def fix_text(t, path):
    t = t.replace(OLD_T, NEW_T).replace("TGS-2024051248", "C716")
    t = t.replace("v9.0 · 20 August 2026", "v1.0 · 1 October 2026").replace("· v9.0", "· v1.0")
    t = t.replace(*PP5).replace(*PP7)
    t = re.sub(KA, r"\1", t)
    n = act_no(path)
    if n:
        t = re.sub(r"(\*\*Duration:\*\*) \d+ minutes", rf"\1 {MIN[n]} minutes", t)
    else:   # index README: "Folder: `activity-0N-…` · LO1 · 45 minutes"
        t = re.sub(r"(`activity-(\d\d)-[^`]+` · LO\d · )\d+ minutes", lambda m: f"{m.group(1)}{MIN[m.group(2)]} minutes", t)
    return t

for f in glob.glob("activities/**/*.md", recursive=True):
    s = open(f, encoding="utf-8").read()
    open(f, "w", encoding="utf-8").write(fix_text(s, f))

def b(s):
    return s.encode("latin-1")

for f in glob.glob("activities/**/*.pdf", recursive=True):
    n = act_no(f)
    w = pypdf.PdfWriter(clone_from=f)
    for pg in w.pages:
        co = pg.get_contents()
        d = co.get_data()
        # wrapped course title: "(Course: Mastering … and Device) Tj … (Performance) Tj"
        d = re.sub(rb"\(Course: " + re.escape(b(OLD_T[:-12])) + rb"\) Tj(.*?)\(Performance\) Tj",
                   lambda m: b"(Course: " + b(NEW_T) + b") Tj" + m.group(1) + b"() Tj", d, flags=re.S)
        d = d.replace(b(OLD_T), b(NEW_T)).replace(b"TGS-2024051248", b"C716")
        d = d.replace(b"v9.0 | 20 August 2026", b"v1.0 | 1 October 2026").replace(b"| v9.0", b"| v1.0")
        d = d.replace(b(PP5[0]), b(PP5[1]))
        d = re.sub(rb"chain used in Practical\) Tj(.*?)\(Performance Task 2\.\) Tj",
                   lambda m: b"chain for a CD excursion.) Tj" + m.group(1) + b"() Tj", d, flags=re.S)
        d = re.sub(rb"(LO\d)(?: \| (?:[KA]\d+(?:, )?)+)", rb"\1", d)
        if n:
            d = re.sub(rb"> Duration: \d+ minutes", b"> Duration: %d minutes" % MIN[n], d)
        else:
            d = re.sub(rb"(Folder: activity-(\d\d)-[a-z0-9-]+ \| LO\d \| )\d+ minutes",
                       lambda m: m.group(1) + b"%d minutes" % MIN[m.group(2).decode()], d)
        co.set_data(d)
        pg.replace_contents(co)
    w.write(open(f, "wb"))
print("done")
