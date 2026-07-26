import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extracts all text from an uploaded PDF file.

    Parameters:
        pdf_file: Uploaded PDF from Streamlit

    Returns:
        str: Complete text extracted from the PDF
    """

    text = ""

    # Open the uploaded PDF
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    # Read every page
    for page in document:
        text += page.get_text()

    document.close()

    return text