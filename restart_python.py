import os
import platform
import subprocess

def restart_windows():
    if platform.system() == "Windows":
        # Menggunakan os.system untuk menjalankan perintah restart
        os.system("shutdown /r /t 0")
    else:
        raise EnvironmentError("This script is designed to run on Windows only.")

if __name__ == "__main__":
    try:
        restart_windows()
    except Exception as e:
        print(f"An error occurred: {e}")
