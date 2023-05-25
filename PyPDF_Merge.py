import PyPDF2

"""
DODAĆ GUI w TKINTER!!!
"""

# Nazwa istniejącego dokumentu PDF
first_pdf = 'Test 1.pdf'
# Nazwa dokumentu PDF, z którego chcesz dodać strony
second_pdf = 'Test 2.pdf'
# Nazwa wynikowego dokumentu PDF z dodanymi stronami
output_pdf = 'Merged.pdf'

# Otwórz pierwszy dokument PDF w trybie do odczytu binarnego
with open(first_pdf, 'rb') as file:
    first_pdf_reader = PyPDF2.PdfReader(file)
    # Otwórz drugi dokument dokument PDF, z którego chcesz dodać stronę
    with open(second_pdf, 'rb') as new_page_file:
        second_pdf_reader = PyPDF2.PdfReader(new_page_file)
        
        # Utwórz nowy obiekt PdfWriter
        output_pdf_writer = PyPDF2.PdfWriter()

        # Dodaj wszystkie strony z pierwszego dokumentu do nowego obiektu PdfWriter
        for page in first_pdf_reader.pages:
            output_pdf_writer.add_page(page)

        # Dodaj wszystkie strony z drugiego dokumentu do nowego obiektu PdfWriter
        for page in second_pdf_reader.pages:
            output_pdf_writer.add_page(page)

        # Zapisz wynikowy dokument PDF z dodaną stroną
        with open(output_pdf, 'wb') as output_file:
            output_pdf_writer.write(output_file)

print("Strona została pomyślnie dodana do dokumentu PDF.")
