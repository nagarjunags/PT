import pymupdf, os, re

pdf_dir = "PYQs/Digital ec"
files = sorted([f for f in os.listdir(pdf_dir) if f.endswith(".pdf")])

for f in files:
    path = os.path.join(pdf_dir, f)
    doc = pymupdf.open(path)
    
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n--- PAGE BREAK ---\n"
        
    ak_pos = full_text.find("Answer Key")
    ak_text = full_text[ak_pos:ak_pos+1000] if ak_pos != -1 else "NOT FOUND"
    
    q_matches = re.findall(r"Q\d+\.", full_text)
    
    print("=" * 60)
    print("FILE:", f)
    print("PAGES:", len(doc))
    print("QUESTIONS FOUND:", len(q_matches), q_matches[:5], "...", q_matches[-3:] if len(q_matches)>3 else "")
    print("ANSWER KEY SNIPPET:\n", ak_text[:300].strip())
