import os, re

files_to_check = [
    "digital/semiconductor-memories/notes.html",
    "digital/adc-dac/notes.html",
    "digital/logic-families/notes.html",
    "digital/boolean-algebra/notes.html",
    "digital/logic-gates/notes.html",
    "digital/combinational-circuits/notes.html",
    "digital/sequential-circuits/notes.html"
]

all_passed = True

for path in files_to_check:
    print(f"\nVerifying {path}...")
    if not os.path.exists(path):
        print(f"❌ File does not exist: {path}")
        all_passed = False
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    size_kb = len(content) / 1024
    print(f"  Size: {size_kb:.1f} KB, Lines: {content.count(chr(10))}")
    
    # Check key tags
    for tag in ["html", "head", "body", "style", "script", "main", "aside"]:
        open_count = len(re.findall(f"<{tag}[ >]", content, re.IGNORECASE))
        close_count = len(re.findall(f"</{tag}>", content, re.IGNORECASE))
        if open_count != close_count:
            print(f"  ❌ Tag mismatch for <{tag}>: {open_count} open vs {close_count} close")
            all_passed = False
        else:
            print(f"  ✓ Tag <{tag}> balanced ({open_count})")
            
    # Check image paths
    base_dir = os.path.dirname(path)
    img_srcs = re.findall(r'src="(images/[^"]+)"', content)
    missing_imgs = []
    for img in set(img_srcs):
        full_img_path = os.path.join(base_dir, img)
        if not os.path.exists(full_img_path):
            missing_imgs.append(full_img_path)
            
    if missing_imgs:
        print(f"  ❌ Missing images ({len(missing_imgs)}): {missing_imgs[:3]}")
        all_passed = False
    else:
        print(f"  ✓ All {len(set(img_srcs))} referenced images verified on disk")
        
    # Check data-target IDs exist
    targets = re.findall(r'data-target="([^"]+)"', content)
    missing_targets = []
    for tid in set(targets):
        if f'id="{tid}"' not in content:
            missing_targets.append(tid)
    if missing_targets:
        print(f"  ❌ Missing data-target IDs: {missing_targets[:3]}")
        all_passed = False
    else:
        print(f"  ✓ All {len(set(targets))} solution drawers matched with buttons")

if all_passed:
    print("\n🎉 ALL 7 CHAPTERS PASSED FULL STRUCTURAL & ASSET VERIFICATION!")
else:
    print("\n❌ SOME VERIFICATIONS FAILED")
