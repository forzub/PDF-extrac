# PDF-extrac

**extract_pdf_images.py**
- извлечение всех картинок из файла Albom.pdf в папку photos
- формат изображений - jpg и tif
- имя формируется порядком считывания и указанием разрешения в dpi.
планируется передавать имя файла и выходную папку как параметры.

**opencv_upscale.py = увеличиваем чёткость и DPI через PIL и OpenCV.увеличиваем чёткость и DPI через PIL и OpenCV.**
Конечно, без нейросетей результат будет скромнее, но можно выжать максимум из классических методов

🛠 Что будет делать скрипт:
- Находит все .tif (или .tiff) в папке photos/tiff.
- Увеличивает изображение в 2-4 раза (по пикселям), сохраняя физический размер (в дюймах), но поднимая DPI до 300.
- Делает интерполяцию с помощью OpenCV (cv2.INTER_LANCZOS4 — максимально чёткий ресайз).
- Сохраняет результат в esrgan_tif/, меняя 96dpi на 300dpi в имени.

🔋 Бонусы:
- Интерполяция LANCZOS4 даёт максимально чёткий результат без ИИ.
- Физический размер (например, 10x10 см) остаётся прежним — только DPI и детализация увеличиваются.
- Цвета остаются верными (конвертация BGR → RGB)
- Работает на любом Python без тяжёлых зависимостей.

💉 Установка OpenCV:
```bash
pip install opencv-python
```
