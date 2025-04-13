# Установка необходимых инструментов и зависимостей

# 🧪 Активируем окружение

Если ты его ещё не активировал, делаем так (из PowerShell или CMD):
```bash
isr_env\Scripts\activate
```
Если ругается PowerShell — тогда:

```powershell
powershell -ExecutionPolicy Bypass -NoExit -Command "isr_env\Scripts\activate"
```


# Шаг 1: Установка Python 3.9 (если у тебя ещё не установлен)
- Перейди на [страницу загрузки Python](https://www.python.org/downloads/release/python-3911/).
- Скачай установочный файл для Python 3.9.x.
- Установи Python, отметив чекбокс Add Python to PATH в процессе установки.

🔹 **Запусти PowerShell от имени администратора**

📍**Уточни путь к интерпретатору**

```powershell
py -3.9
```
Эта команда должна запустить именно Python 3.9, если он установлен.

✅ **Выйди из Python-интерпретатора:**
```python
exit()
```

📍**Создай виртуальное окружение с этой версией**
```powershell
py -3.9 -m venv myenv
```
После этого появится папка myenv, внутри которой будет всё нужное для независимого запуска.

📍 **Активируй окружение**
```powershell
myenv\Scripts\activate
```
Теперь в командной строке появится (myenv) — значит, окружение активировано, и всё, что ты ставишь, будет работать именно в нём.


# 🔧 Шаги для создания окружения

✅ **Обновление pip:**

(на всякий случай — чтоб всё было свежее)

```bash
pip install --upgrade pip setuptools wheel
```

# 🔧 Что за «компиляция зависимостей» и почему всё ломается?

🛠️ Когда ты ставишь старую или продвинутую библиотеку, вроде Real-ESRGAN или ISR, она может:
- использовать C/C++ код внутри себя;
- требовать специальные компиляторы, чтобы пересобрать этот код под твою систему;
- подтягивать неофициальные или устаревшие зависимости, которые не собираются «из коробки».


# Шаг 2: Установка Visual Studio Build Tools
Скачай и установи Visual Studio Build Tools для компиляции зависимостей, необходимых для некоторых библиотек, таких как torch и ISR.

Перейди [по ссылке](https://visualstudio.microsoft.com/visual-cpp-build-tools/) для установки и выбери C++ build tools. Убедись, что ты выбрал следующие компоненты:

Выбираем строго и без поэзии: тебе нужно только одно:

✅ Desktop development with C++

А дальше важное:

🔧 В правой панели обязательно включи:

✅ MSVC v142 - VS 2019 C++ x64/x86 build tools

✅ Windows 10 SDK (или Windows 11, если у тебя 11ка)

✅ C++ CMake tools for Windows

✅ C++ ATL for x86 and x64

✅ C++/CLI support (если будет доступен)

Это даст тебе полноценный C++ компилятор + нужный SDK, чтобы собрать и Real-ESRGAN, и любые кривые зависимости из ада. После установки перезагрузи комп — потому что переменные окружения обновляются не всегда автоматически.

✅ **Проверка готовности**

Проверь, что cl.exe (Visual C++ Compiler) доступен (cmd показывает, powershell - нет):

```powershell
where cl
```

Если выдаёт путь — отлично. Если нет, надо будет прописать путь вручную в переменную окружения.

🧭 **Где находится cl.exe?**
Обычно он лежит где-то вроде:

```java
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\<версия>\bin\Hostx64\x64\
```

✅ **Как добавить путь в переменные среды (Windows 10 / 11):**

Нажми Win + S, введи "environment variables" ("змінні оточення") и открой пункт:

"Edit the system environment variables"

Внизу нажми кнопку "Environment Variables…"

В разделе "System variables" (или "User variables", если хочешь только для себя) найди переменную Path → жми Edit.

Жми New, вставь путь к папке, где лежит cl.exe.

Жми OK → OK → OK.

Перезапусти терминал (PowerShell или CMD), чтобы он увидел обновление.

🔧 **Проверка компилятора**
Можешь дополнительно убедиться, что cl.exe работает, выполнив в cmd:

```cmd
cl
```

Если увидишь что-то вроде:

```mathematica
Microsoft (R) C/C++ Optimizing Compiler Version XX.XX for x64
```
— всё готово, и мы можем возвращаться к сборке Real-ESRGAN или ISR.

# 🚧 Что делаем дальше

📂 **Установка TensorFlow 1.13.1**
```bash
pip install tensorflow==1.13.1
```
***Это обязательно для ISR, не пытайся ставить новее — сломается*** 💀

# 🚧 Cосредоточимся на Real-ESRGAN. 

Для Windows это всё ещё возможно, просто надо идти по проверенному маршруту. Мы пойдём по пути установки Real-ESRGAN через Python API (не NCNN, не CLI), чтобы можно было интегрировать прямо в скрипт.

📥 **Скачиваем предобученную модель (пример: RealESRGAN_x4plus)**

📂 **Убедись, что структура файлов такая:**

```
project_folder/
│
├─ test_import.py
├─ sample.jpg                 ← (любая картинка для теста)
├─ weights/
│   └─ RealESRGAN_x4plus.pth
```

💣 **Удаляем версии, которые нам не подходят как следует:**

```bash
pip uninstall torch torchvision -y
pip uninstall numpy
pip uninstall realesrgan
```

Если сомневаешься, можешь дважды прогнать — pip не обидится, просто скажет, что уже удалено.

🔄 **Устанавливаем совместимые версии:**

```bash
pip install torch==1.10.1 torchvision==0.11.2
pip install numpy==1.26.4
```
После установки можно проверить:

```bash
python -c "import torch; import torchvision; print(torch.__version__, torchvision.__version__)"
```

Когда увидишь:
```
1.10.1 0.11.2
```

** ✅ Клонируем оригинальный репозиторий:**

```bash
git clone https://github.com/xinntao/Real-ESRGAN.git
cd Real-ESRGAN
```



