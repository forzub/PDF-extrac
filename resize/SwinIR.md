# SwinIR

## 🚧 Особенности установки:
- Нет pip-пакета:
- Устанавливается не через pip install, а клонированием репозитория с GitHub и ручным запуском скриптов.
- → Ничего страшного, но немного больше действий.

**Torch версии:**
- Работает с PyTorch ≥1.7, но без особой привязанности к конкретной версии. Лучше брать проверенный тандем PyTorch + torchvision, который у тебя уже работает.

**NumPy и OpenCV:**
- Если у тебя они уже стоят (а стоят), конфликтов быть не должно.

**Нет GUI, только Python API или CLI:**
- Всё делается вручную или через скрипты. Зато можно гибко настраивать.

Pretrained модели нужно скачивать вручную (или через скрипт).

## ✅ Что хорошего:
- Не требует CUDA — работает и на CPU (медленно, но работает).
- Без каких-то жёстких зависимостей вроде pybind, cl.exe и других адских плясок.
- Уже проверен и стабилен, используется в научных публикациях.

## 🌀 Создание виртуальной среды для SwinIR
Выполни в терминале:

```bash
python -m venv swinir_env
```
Затем активируй её:

```
.\swinir_env\Scripts\Activate.ps1
```

## 🔧 Клонирование репозитория SwinIR

```bash
git clone https://github.com/JingyunLiang/SwinIR.git
cd SwinIR
```
## 🔧 Установим всё, что нужно для SwinIR:
```bash
pip install numpy opencv-python matplotlib scikit-image tqdm yacs
pip install requests
pip install timm
```

## 🛠 Проверим, всё ли установилось:
```bash
pip list
```

## 🧪 Скачиваем модель
Перейди в директорию SwinIR, если ты ещё не там:

```bash
cd SwinIR
```
Теперь качаем предобученную модель (например, для увеличения x4):

```bash
wget https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-M_x4_GAN.pth -P model_zoo
```

Если wget не установлен — можно скачать вручную и положить в SwinIR/model_zoo/:
- [Скачать модель ](https://github.com/JingyunLiang/SwinIR/releases)
- 003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-M_x4_GAN.pth
- или близкое название с L и x4 и GAN в имени

🗂 **Типовая структура внутри SwinIR, на всякий случай:**

```go
SwinIR/
├── main_test_swinir.py
├── model_zoo/
│   └── 003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-M_x4_GAN.pth
├── testsets/
│   └── real/
│       └── your_image.jpg
├── results/
│   └── swinir_real_sr_x4/
```


## ✅ Шаг 1: Подготовим тестовое изображение

Создай папку с изображениями ./testsets/real, и положи туда хоть один .png или .jpg.

## ✅ Шаг 2: Запускаем готовый скрипт
Теперь выполни следующую команду прямо в PowerShell из папки SwinIR:

```powershell
python main_test_swinir.py --task real_sr --scale 4 --large_model --model_path model_zoo/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth --folder_lq testsets/real_sr --tile 0
```
🧠 Объяснение:
- -task real_sr — задача увеличения реальных изображений.
- -scale 4 — увеличим в 4 раза.
- -model_path — путь к твоей модели.
- -folder_lq . — папка с изображением (текущая).
- -tile 128 — разделяем изображение на куски, чтобы не упасть с Out of Memory.

- Скрипт main_test_swinir.py ищет все изображения в указанной папке (--folder_lq).
- То есть можно положить туда любой файл: test.png, image.tif, kitty.jpg — всё сгодится.
- Он обработает все файлы с расширениями .png, .jpg, .jpeg, .bmp, .tif, .tiff





