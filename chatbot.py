import fitz  # PyMuPDF

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.extract_text()
    
    def extract_text(self):
        """Extract text from the PDF file."""
        pdf_document = fitz.open(self.file_path)
        full_text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            full_text += page.get_text()
        pdf_document.close()
        return full_text

# Create a PDFReader instance
pdf_reader = PDFReader('Bruno_child_offers.pdf')


import re
from nltk.chat.util import Chat, reflections

class ChatBot:
    def __init__(self, catalog_text):
        self.catalog_text = catalog_text
        
    def respond(self, user_input):
        """Generate a response based on user input."""
        if re.search(r"(.*) oferta (.*)", user_input, re.IGNORECASE):
            return "I'm here to help with our summer offers. What would you like to know?"
        elif re.search(r"(.*) producto (.*)", user_input, re.IGNORECASE):
            return self.search_catalog(user_input)
        else:
            return "I can only answer questions related to our offers for children. Please ask about products or offers."

    def search_catalog(self, query):
        """Search the catalog text for information related to the query."""
        if query.lower() in self.catalog_text.lower():
            return "I found information related to your query in our catalog. Please specify your question for more details."
        else:
            return "Sorry, I couldn't find information related to your query in the catalog."

# Initialize the chatbot with the catalog text
chatbot = ChatBot(pdf_reader.text)
