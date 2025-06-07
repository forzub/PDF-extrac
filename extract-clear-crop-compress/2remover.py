from PyPDF2 import PdfReader, PdfWriter

def remove_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    """
    Удаляет указанные страницы из PDF и сохраняет результат в новый файл.
    
    :param input_pdf_path: Путь к исходному PDF.
    :param output_pdf_path: Путь для сохранения нового PDF.
    :param pages_to_remove: Список номеров страниц для удаления (нумерация с 1).
    """
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()

    # Номера страниц в Python начинаются с 0, поэтому преобразуем
    pages_to_remove_indices = [page - 1 for page in pages_to_remove]

    for page_num in range(len(pdf_reader.pages)):
        if page_num not in pages_to_remove_indices:
            pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Удаление страниц из PDF")
    parser.add_argument("input_pdf", help="Путь к исходному PDF-файлу")
    parser.add_argument("output_pdf", help="Путь к новому PDF-файлу")
    parser.add_argument("--remove", type=int, nargs="+", required=True, 
                       help="Номера страниц для удаления (через пробел, например: 3 5 7)")

    args = parser.parse_args()

    remove_pages(args.input_pdf, args.output_pdf, args.remove)
    print(f"Страницы {args.remove} удалены. Результат сохранён в {args.output_pdf}")