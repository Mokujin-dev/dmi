import os
import platform

def restart_windows():
    if platform.system() == "Windows":
        try:
            # Menggunakan os.system untuk menjalankan perintah restart
            os.system("shutdown /r /t 0")
        except Exception as e:
            print(f"An error occurred while trying to restart: {e}")
    else:
        print("This script is designed to run on Windows only.")

if __name__ == "__main__":
    restart_windows()
