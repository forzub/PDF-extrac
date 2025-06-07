import subprocess

def compress_pdf(input_file, output_file):
    gs_command = [
        "gswin64c",  # команда для Ghostscript (64-битная консольная версия)
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",  # Можно менять на /ebook или /printer для качества
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_file}",
        input_file
    ]

    print(f"Запускаю Ghostscript для сжатия {input_file}...")
    result = subprocess.run(gs_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Успешно сжал {input_file} до {output_file}")
    else:
        print("Ошибка при сжатии:")
        print(result.stderr.decode())

if __name__ == "__main__":
    import sys
    compress_pdf(sys.argv[1], sys.argv[2])
