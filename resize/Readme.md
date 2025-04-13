# Установка необходимых инструментов и зависимостей

# Шаг 1: Установка Python 3.9 (если у тебя ещё не установлен)
- Перейди на [страницу загрузки Python](https://www.python.org/downloads/release/python-3911/).
- Скачай установочный файл для Python 3.9.x.
- Установи Python, отметив чекбокс Add Python to PATH в процессе установки.
📍**Уточни путь к интерпретатору**

```powershell
py -3.9
```
Эта команда должна запустить именно Python 3.9, если он установлен.

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






# Шаг 2: Установка Visual Studio Build Tools
Скачай и установи Visual Studio Build Tools для компиляции зависимостей, необходимых для некоторых библиотек, таких как torch и ISR.

Перейди [по ссылке](https://visualstudio.microsoft.com/visual-cpp-build-tools/) для установки и выбери C++ build tools. Убедись, что ты выбрал следующие компоненты:

Desktop development with C++

MSVC v142 - VS 2019 C++ x64/x86 build tools

Windows 10 SDK

После установки, перезагрузи компьютер.















# 🧪 Активируем окружение

Если ты его ещё не активировал, делаем так (из PowerShell или CMD):
```bash
isr_env\Scripts\activate
```
Если ругается PowerShell — тогда:

```powershell
powershell -ExecutionPolicy Bypass -NoExit -Command "isr_env\Scripts\activate"
```

