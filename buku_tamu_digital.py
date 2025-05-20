from collections import deque
import os

FILE_PATH = "buku_tamu_digital.txt"

def load_data():
    queue = deque()
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            for line in file:
                queue.append(line.strip())
    return queue

def save_data(queue):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        for item in queue:
            file.write(item + '\n')

def sign(queue, nama, pesan):
    entry = f"{nama}: {pesan}"
    queue.append(entry)
    save_data(queue)
    print("✅ Entri berhasil ditambahkan.")

def show(queue):
    if not queue:
        print("📭 Buku tamu kosong.")
    else:
        print("📖 Daftar Buku Tamu:")
        for i, entry in enumerate(queue, start=1):
            print(f"{i}. {entry}")

def main():
    queue = load_data()
    print("📘 Buku Tamu Digital (CLI)")
    print("Perintah: sign <nama> <pesan> | show | exit")

    while True:
        command = input("\n> ").strip()
        if command.startswith("sign "):
            parts = command.split(" ", 2)
            if len(parts) < 3:
                print("⚠️ Format: sign <nama> <pesan>")
                continue
            nama, pesan = parts[1], parts[2]
            sign(queue, nama, pesan)
        elif command == "show":
            show(queue)
        elif command == "exit":
            print("👋 Keluar dari aplikasi.")
            break
        else:
            print("❓ Perintah tidak dikenali.")

if __name__ == "__main__":
    main()
