import os
import pytest
import PyPDF2
from reportlab.lib.pagesizes import A4
from your_module import create_addition_worksheet  # Adjust the import according to your file structure

@pytest.fixture
def output_filename():
    return 'test_addition_worksheet.pdf'

def test_create_addition_worksheet(output_filename):
    # Create the worksheet
    input_digits = "1 2 3 4 5"
    create_addition_worksheet(input_digits, output_filename)
    
    # Check if the file was created
    assert os.path.exists(output_filename)
    
    # Read the PDF and verify its content
    with open(output_filename, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        assert reader.numPages > 0
        
        # Check the title
        first_page = reader.getPage(0)
        text = first_page.extract_text()
        assert "Addition Worksheet" in text
        
        # Check if some problems are present in the PDF
        for digit in input_digits.split():
            assert f"{digit} +" in text or f"+ {digit}" in text

    # Cleanup the created PDF file
    os.remove(output_filename)
