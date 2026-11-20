import fitz


# ==========================================
# PDF RESUME TEXT EXTRACTION
# ==========================================

def extract_resume_text(pdf_path):
    """
    Extract text from an uploaded PDF resume.

    Args:
        pdf_path (str): Path to the uploaded PDF file.

    Returns:
        str: Extracted resume text.

    Raises:
        ValueError: If the PDF cannot be read or contains no text.
    """

    document = None

    try:

        # Open the PDF document
        document = fitz.open(pdf_path)

        extracted_text = []

        # Extract text from every page
        for page in document:

            page_text = page.get_text("text")

            if page_text:
                extracted_text.append(page_text)

        # Combine extracted text
        resume_text = "\n".join(extracted_text).strip()

        # Check whether readable text exists
        if not resume_text:

            raise ValueError(
                "No readable text found. "
                "Please upload a text-based PDF resume."
            )

        return resume_text

    except ValueError:

        raise

    except Exception as error:

        raise ValueError(
            f"Resume extraction failed: {str(error)}"
        ) from error

    finally:

        # Close the PDF document
        if document is not None:
            document.close()