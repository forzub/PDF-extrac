import os
import fitz  # PyMuPDF
from PIL import Image

def extract_images_from_pdf(pdf_path, jpg_quality=95):
    # Создаем папки для TIFF и JPG
    os.makedirs("photos/tiff", exist_ok=True)
    os.makedirs("photos/jpg", exist_ok=True)
    print("📁 Созданы папки: photos/tiff, photos/jpg")

    doc = fitz.open(pdf_path)
    total_images = 0

    print(f"🔍 Анализ PDF: {pdf_path} (страниц: {len(doc)})")

    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        if not image_list:
            print(f"   ⚠️ На странице {page_num + 1} изображений не найдено.")
            continue

        print(f"   📄 Страница {page_num + 1}: найдено {len(image_list)} изображений")

        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            img_width = base_image["width"]
            img_height = base_image["height"]
            dpi = base_image.get("xres", 96)  # DPI (по умолчанию 96)

            # Имя файла без расширения: номер_DPI
            img_name = f"{total_images + 1}_{int(dpi)}dpi"

            # Сохранение в TIFF (без потерь)
            tiff_path = os.path.join("photos", "tiff", f"{img_name}.tiff")
            with open(tiff_path, "wb") as tiff_file:
                tiff_file.write(image_data)

            # Конвертация в JPG (с настраиваемым качеством)
            jpg_path = os.path.join("photos", "jpg", f"{img_name}.jpg")
            with Image.open(tiff_path) as img_pil:
                img_pil.save(jpg_path, "JPEG", quality=jpg_quality)

            total_images += 1
            print(f"      💾 Извлечено: {img_name}")
            print(f"         TIFF: {tiff_path} ({img_width}x{img_height}, {int(dpi)} DPI)")
            print(f"         JPG: {jpg_path} (качество: {jpg_quality}%)")

    doc.close()
    print(f"✅ Готово! Извлечено изображений: {total_images}")

if __name__ == "__main__":
    pdf_file = "Albom.pdf"  # Имя вашего PDF-файла
    extract_images_from_pdf(pdf_file, jpg_quality=90)  # Можно изменить качество JPG (по умолчанию 90%)