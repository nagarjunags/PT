import json, pymupdf, re

doc = pymupdf.open("PYQs/Digital ec/GATE ECE Sequential Circuits Previous Year Questions with Answer Key.pdf")
full_text = ""
pages_text = []
for pno, page in enumerate(doc):
    txt = page.get_text()
    pages_text.append((pno + 1, txt))
    full_text += f"\n<<<PAGE_{pno+1}>>>\n" + txt

# Answers
ak_idx = full_text.find("Answer Key")
ak_text = full_text[ak_idx:]
ans_map = {}
for line in ak_text.split("\n"):
    m = re.match(r"^(\d+)\.\s*(.*)", line.strip())
    if m:
        ans_map[int(m.group(1))] = m.group(2).strip()

# Load images map from raw_data.json
with open("digital/sequential-circuits/raw_data.json", "r") as f:
    raw_data = json.load(f)
img_map = raw_data["images"]

# Split by Q{num}.
splits = re.split(r"(Q\d+\.)", full_text)
print("Splits count:", len(splits))

parsed_qs = []
for i in range(1, len(splits), 2):
    q_label = splits[i].strip()
    q_num = int(q_label[1:-1])
    content = splits[i+1].strip()
    
    # find page number
    page_match = re.findall(r"<<<PAGE_(\d+)>>>", full_text[:full_text.find(q_label)])
    pno = int(page_match[-1]) if page_match else 1
    
    # find year
    year_match = re.search(r"(GATE\s+[A-Z]+\s+\d{4}(?:\s+Set\s+\d+)?)", content)
    year = year_match.group(1) if year_match else "GATE ECE"
    
    # marks
    marks = "1 Mark" if q_num <= 31 else ("2 Marks" if q_num <= 72 else ("5 Marks" if q_num <= 78 else "8 Marks"))
    
    # clean content
    # cut off at Open solution
    if "Open solution" in content:
        body = content[:content.find("Open solution")].strip()
    else:
        body = content[:400].strip()
        
    # remove page markers
    body = re.sub(r"<<<PAGE_\d+>>>", "", body)
    body = re.sub(r"GATE\s+[A-Z]+\s+\d{4}(?:\s+Set\s+\d+)?", "", body).strip()
    
    # associate image if page has images
    diag = ""
    str_pno = str(pno)
    if str_pno in img_map and len(img_map[str_pno]) > 0:
        # choose image
        diag = img_map[str_pno][0]["file"]
        
    parsed_qs.append({
        "num": f"Q{q_num}.",
        "q_num": q_num,
        "year": year,
        "marks": marks,
        "body": body,
        "ans": ans_map.get(q_num, "See solution"),
        "page": pno,
        "diag": diag
    })

print(f"Successfully parsed {len(parsed_qs)} questions.")
print("Sample Q1:", parsed_qs[0])
print("Sample Q32:", parsed_qs[31])
print("Sample Q82:", parsed_qs[-1])
