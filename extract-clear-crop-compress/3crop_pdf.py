import fitz  # PyMuPDF
import argparse

def render_and_crop(input_file, output_file, left, right, top, bottom, zoom=2.0):
    doc = fitz.open(input_file)
    new_doc = fitz.open()

    for page in doc:
        # Берём размер страницы в поинтах
        rect = page.rect

        # Переводим cm в поинты (1 inch = 72 points, 1 inch = 2.54 cm)
        def cm_to_pt(cm):
            return cm * 72 / 2.54

        l = rect.x0 + cm_to_pt(left)
        r = rect.x1 - cm_to_pt(right)
        t = rect.y0 + cm_to_pt(top)
        b = rect.y1 - cm_to_pt(bottom)

        # Убедимся, что обрезаем правильно
        if l >= r or t >= b:
            print(f"❌ Ошибка: слишком большая обрезка на странице {page.number + 1}")
            return

        clip = fitz.Rect(l, t, r, b)

        # Рендерим с клипом и масштабом
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, clip=clip)

        # Создаём новую страницу с размерами pix
        new_page = new_doc.new_page(width=pix.width, height=pix.height)

        # Вставляем изображение
        new_page.insert_image(new_page.rect, pixmap=pix)

    new_doc.save(output_file)
    print(f"✅ PDF обрезан и сохранён: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Физическая обрезка PDF через рендер")
    parser.add_argument("input", help="Исходный PDF")
    parser.add_argument("output", help="Результат")
    parser.add_argument("--left", type=float, default=0, help="Обрезка слева в см")
    parser.add_argument("--right", type=float, default=0, help="Обрезка справа в см")
    parser.add_argument("--top", type=float, default=0, help="Обрезка сверху в см")
    parser.add_argument("--bottom", type=float, default=0, help="Обрезка снизу в см")
    args = parser.parse_args()

    render_and_crop(args.input, args.output, args.left, args.right, args.top, args.bottom)
