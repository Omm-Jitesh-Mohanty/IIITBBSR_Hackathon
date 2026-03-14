import fitz
import numpy as np
import cv2
from paddleocr import PaddleOCR


ocr = PaddleOCR(use_angle_cls=True, lang="en")


def extract_text_from_handwritten_pdf(pdf_file):

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    extracted_text = ""

    for page in doc:

        # Increase resolution for handwriting
        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

        img = np.frombuffer(pix.samples, dtype=np.uint8)

        img = img.reshape(pix.height, pix.width, pix.n)

        # Handle different channel formats
        if pix.n == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        elif pix.n == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # Improve handwriting visibility
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        thresh = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        # Convert back to 3 channel
        thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

        try:
            result = ocr.ocr(thresh)
        except Exception as e:
            print("OCR Error:", e)
            continue

        if result and result[0]:
            for line in result[0]:
                extracted_text += line[1][0] + " "

        extracted_text += "\n"

    return extracted_text