import fitz  # PyMuPDF

# ✅ PDF se clickable links extract karo
def extract_links_from_pdf(file_path):
    links = []
    doc = fitz.open(file_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        link_annotations = page.get_links()
        for link in link_annotations:
            if 'uri' in link:
                links.append(link['uri'])
    
    return links

# ✅ Links ko classify karo
def classify_links(pdf_path):
    print("Extracting links from PDF...")
    links = extract_links_from_pdf(pdf_path)
    links = list(set(links))  # ✅ Duplicate removal
    
    github_links = []
    linkedin_links = []
    certificate_links = []
    
    for link in links:
        if 'github.com' in link:
            github_links.append(link)
        elif 'linkedin.com' in link:
            linkedin_links.append(link)
        else:
            certificate_links.append(link)  # ✅ Fixed this line
    
    return github_links, linkedin_links, certificate_links

