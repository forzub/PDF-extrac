import os
import cv2
from PIL import Image

# Папки
input_folder = 'photos/tiff'
output_folder = 'photo_opencv_resize'
os.makedirs(output_folder, exist_ok=True)

# Целевой DPI
target_dpi = 300

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.tif', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        print(f'Обработка: {input_path}')

        # Открываем через PIL, чтобы прочитать DPI
        pil_image = Image.open(input_path)
        dpi = pil_image.info.get("dpi", (96, 96))
        orig_dpi = dpi[0]
        print(f'Исходный DPI: {orig_dpi}')

        # Чтение изображения через OpenCV
        img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

        # Проверка на альфа-канал (RGBA)
        if img is None:
            print(f'Не удалось открыть файл: {input_path}')
            continue

        has_alpha = img.shape[2] == 4 if len(img.shape) == 3 else False

        # Масштабируем изображение
        scale_factor = target_dpi / orig_dpi
        new_width = int(img.shape[1] * scale_factor)
        new_height = int(img.shape[0] * scale_factor)
        interpolation = cv2.INTER_LANCZOS4

        resized_img = cv2.resize(img, (new_width, new_height), interpolation=interpolation)

        # Конвертация цветов
        if has_alpha:
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGRA2RGBA)
        elif len(resized_img.shape) == 3:
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

        # Перевод в PIL
        result_image = Image.fromarray(resized_img)

        # Новое имя
        new_filename = filename.replace('96dpi', '300dpi')
        output_path = os.path.join(output_folder, new_filename)

        # Сохраняем с 300 DPI
        result_image.save(output_path, dpi=(300, 300))

        print(f'Сохранено: {output_path}\n')
