import fitz
from pathlib import Path
pdf = Path('attached_assets/Prahari_Netra_Professional_Web_App_Spec_for_Claude_1788289106931.pdf')
out = Path('.agents/outputs/prahari-pages')
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
print('pages', doc.page_count)
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False)
    path = out / f'page-{i+1:02d}.png'
    pix.save(path)
    print(path)
