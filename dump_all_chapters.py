import pymupdf, os, re, json

chapters = [
    {
        "slug": "semiconductor-memories",
        "title": "Semiconductor Memories",
        "pdf": "GATE ECE Semiconductor Memories Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "adc-dac",
        "title": "Analog to Digital and Digital to Analog Converters",
        "pdf": "GATE ECE Analog to Digital and Digital to Analog Converters Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "logic-families",
        "title": "Logic Families",
        "pdf": "GATE ECE Logic Families Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "boolean-algebra",
        "title": "Boolean Algebra",
        "pdf": "GATE ECE Boolean Algebra Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "logic-gates",
        "title": "Logic Gates",
        "pdf": "GATE ECE Logic Gates Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "combinational-circuits",
        "title": "Combinational Circuits",
        "pdf": "GATE ECE Combinational Circuits Previous Year Questions with Answer Key.pdf"
    },
    {
        "slug": "sequential-circuits",
        "title": "Sequential Circuits",
        "pdf": "GATE ECE Sequential Circuits Previous Year Questions with Answer Key.pdf"
    }
]

base_pdf_dir = "PYQs/Digital ec"

for ch in chapters:
    pdf_path = os.path.join(base_pdf_dir, ch["pdf"])
    out_dir = os.path.join("digital", ch["slug"])
    img_dir = os.path.join(out_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    doc = pymupdf.open(pdf_path)
    print(f"\nProcessing {ch['title']} ({len(doc)} pages)...")
    
    # 1. Extract Images
    img_map = {}
    for pno in range(len(doc)):
        page = doc[pno]
        for idx, img in enumerate(page.get_images()):
            xref = img[0]
            base = doc.extract_image(xref)
            # Filter out tiny icons, ExamGOAL logo (120x120 or small barcodes)
            if base["width"] > 140 and base["height"] > 60:
                # check if not just a generic square logo
                if base["width"] == 120 and base["height"] == 120:
                    continue
                fname = f"p{pno+1}_img{idx}_{xref}.{base['ext']}"
                fpath = os.path.join(img_dir, fname)
                with open(fpath, "wb") as f:
                    f.write(base["image"])
                if pno+1 not in img_map:
                    img_map[pno+1] = []
                img_map[pno+1].append({
                    "file": f"images/{fname}",
                    "width": base["width"],
                    "height": base["height"]
                })
                
    # 2. Extract Text by page
    pages_text = []
    for pno in range(len(doc)):
        pages_text.append({
            "page": pno + 1,
            "text": doc[pno].get_text()
        })
        
    # Save extraction json for reference
    data = {
        "slug": ch["slug"],
        "title": ch["title"],
        "pages_count": len(doc),
        "images": img_map,
        "pages": pages_text
    }
    with open(os.path.join(out_dir, "raw_data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {ch['slug']}/raw_data.json with {sum(len(v) for v in img_map.values())} diagrams.")
