class PDFReader:
    def open_pdf(self, filename):
        print(f"Opening PDF file: {filename}")

class EPUBReader:
    def load_epub(self, filename):
        print(f"Loading EPUB file: {filename}")

class EBUBAdapter:
    def __init__(self, epub):
        self.epub = epub
    
    def open(self, filename):
        self.epub.load_epub(filename)

ebub = EPUBReader()
adapter = EBUBAdapter(ebub)
adapter.open("thakkali.txt")