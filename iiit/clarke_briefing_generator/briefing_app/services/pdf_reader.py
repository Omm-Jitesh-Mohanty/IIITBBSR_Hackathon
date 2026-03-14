from pdfminer.high_level import extract_text
from .handwritten_reader import extract_text_from_handwritten_pdf


def extract_text_from_pdf(file):

    try:
        # Reset pointer before reading
        file.seek(0)

        text = extract_text(file)

        # If very little text → assume scanned/handwritten
        if not text or len(text.strip()) < 50:
            file.seek(0)
            text = extract_text_from_handwritten_pdf(file)

        return text

    except Exception as e:

        print("PDF text extraction failed:", e)

        file.seek(0)

        return extract_text_from_handwritten_pdf(file)