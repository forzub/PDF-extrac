# extract_pdf_pages.py
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()

    if start_page < 0 or end_page >= len(pdf_reader.pages):
        raise ValueError("Некорректные номера страниц")

    for page_num in range(start_page, end_page + 1):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Извлечение страниц из PDF")
    parser.add_argument("input_pdf", help="Путь к исходному PDF-файлу")
    parser.add_argument("output_pdf", help="Путь к новому PDF-файлу")
    parser.add_argument("--start", type=int, required=True, help="Начальная страница (начиная с 1)")
    parser.add_argument("--end", type=int, required=True, help="Конечная страница (включительно)")

    args = parser.parse_args()

    # Конвертируем номера страниц в индексы (Python считает с 0)
    start_idx = args.start - 1
    end_idx = args.end - 1

    extract_pages(args.input_pdf, args.output_pdf, start_idx, end_idx)
    print(f"Страницы {args.start}-{args.end} сохранены в {args.output_pdf}")