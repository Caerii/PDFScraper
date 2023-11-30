import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    # Initialize a PDF file reader
    reader = PdfReader(pdf_path)
    text = ""

    # Iterate over each page and extract text
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text.strip()

def process_batch_pdfs(input_folder):
    # Dictionary to hold the content of all text files
    all_texts = {}
    
    # List all PDFs in the input directory
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        # Construct the full file path
        pdf_path = os.path.join(input_folder, pdf_file)
        
        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Count words in the extracted text
        word_count = len(text.split())
        
        # Create a corresponding text file name
        text_file_name = f"{os.path.splitext(pdf_file)[0]}_{word_count}_words.txt"
        
        # Write the extracted text to the text file
        with open(os.path.join(input_folder, text_file_name), 'w') as text_file:
            text_file.write(text)
        
        # Store the text and its file name
        all_texts[text_file_name] = text

    # Glue all texts together into a single text file
    glued_text = "\n\n".join([f"{filename}:\n{content}" for filename, content in all_texts.items()])
    glued_text_file_path = os.path.join(input_folder, "all_texts_glued.txt")
    with open(glued_text_file_path, 'w') as glued_file:
        glued_file.write(glued_text)
    
    return glued_text_file_path

# This function call is just a placeholder as the actual folder path needs to be provided.
# You would call the function like this, assuming the PDFs are located in a folder named 'pdf_folder':
# glued_file_path = process_batch_pdfs('/path/to/pdf_folder')
# print(f"Generated glued text file at: {glued_text_file_path}")
