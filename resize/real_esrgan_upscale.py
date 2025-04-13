import os
import time
import numpy as np
from PIL import Image
from glob import glob
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

def format_time(seconds):
    """Форматирование времени в читаемый вид"""
    if seconds < 1:
        return f"{seconds*1000:.0f} мс"
    elif seconds < 60:
        return f"{seconds:.1f} сек"
    else:
        mins = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{mins} мин {secs} сек"

def process_tiff_files():
    # Конфигурация
    input_dir = 'photos/tiff'
    output_dir = 'photo_esrgan_resize'
    model_name = 'RealESRGAN_x4plus'
    model_path = os.path.join('weights', f'{model_name}.pth')
    scale = 4
    tile_size = 0  # 0 - без разделения на тайлы
    
    # Создаем выходную папку
    os.makedirs(output_dir, exist_ok=True)

    # Инициализация модели
    print("\nИнициализация модели RealESRGAN...")
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
    upsampler = RealESRGANer(
        scale=4,
        model_path=model_path,
        model=model,
        tile=tile_size
    )
    print("Модель успешно загружена\n")

    # Получаем список TIFF-файлов
    tiff_files = glob(os.path.join(input_dir, '*.tif')) + glob(os.path.join(input_dir, '*.tiff'))
    
    if not tiff_files:
        print("Не найдено TIFF-файлов для обработки")
        return

    print(f"Найдено {len(tiff_files)} файлов для обработки\n")
    
    for input_path in tiff_files:
        try:
            filename = os.path.basename(input_path)
            print(f"Начало обработки: {filename}")
            start_time = time.time()

            # Загрузка изображения
            img = Image.open(input_path).convert('RGB')
            original_size = f"{img.width}x{img.height}"
            
            # Увеличение разрешения
            print("Увеличение разрешения...")
            output_img, _ = upsampler.enhance(np.array(img), outscale=scale)
            
            # Формирование имени выходного файла
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}-300dpi.tif"
            output_path = os.path.join(output_dir, output_filename)
            
            # Сохранение с LZW-сжатием (без параметра quality)
            print("Сохранение с LZW-сжатием...")
            Image.fromarray(output_img).save(
                output_path,
                format='TIFF',
                dpi=(300, 300),
                compression="tiff_lzw"  # Убрали параметр quality
            )
            
            # Расчет времени обработки
            proc_time = time.time() - start_time
            new_size = f"{output_img.shape[1]}x{output_img.shape[0]}"
            
            print(f"Успешно обработан: {filename}")
            print(f"Размер: {original_size} -> {new_size}")
            print(f"Время обработки: {format_time(proc_time)}\n")
            
        except Exception as e:
            print(f"\nОшибка при обработке {filename}: {str(e)}\n")

if __name__ == '__main__':
    print("=== Обработка TIFF-файлов RealESRGAN ===")
    print("Параметры:")
    print(f"- Масштаб: x4")
    print(f"- Выходной DPI: 300")
    print(f"- Сжатие: LZW\n")
    
    start_total = time.time()
    process_tiff_files()
    
    total_time = time.time() - start_total
    print(f"\nОбщее время работы: {format_time(total_time)}")
    print("Обработка завершена. Результаты в папке 'photo_esrgan_resize'")