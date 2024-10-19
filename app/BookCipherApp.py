import tkinter as tk
from tkinter import messagebox, filedialog

from app.BookCipher import BookCipher
from app.Key import Key


class BookCipherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Книжковий шифр")
        self.geometry("600x500")

        self.text_area = tk.Text(self, wrap='word', height=15)
        self.text_area.pack(expand=True, fill='both')

        self.key_label = tk.Label(self, text="Ключ:")
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(self, width=64)
        self.key_entry.pack(pady=5)

        self.encrypt_button = tk.Button(self, text="Шифрувати", command=self.encrypt_file)
        self.decrypt_button = tk.Button(self, text="Розшифрувати", command=self.decrypt_file)
        self.encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.decrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Створити", command=self.create_file)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.quit_app)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Довідка", menu=help_menu)
        help_menu.add_command(label="Про програму", command=self.about)

        self.current_file = None

    def create_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        messagebox.showinfo("Створити", "Новий файл створено.")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Відкрити файл",
            filetypes=(("Текстові файли", "*.txt"), ("Усі файли", "*.*"))
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file_content)
                self.current_file = file_path
            messagebox.showinfo("Відкрити", f"Файл відкрито: {file_path}")

    def save_file(self):
        if self.current_file:
            file_content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(file_content)
            messagebox.showinfo("Зберегти", f"Файл збережено: {self.current_file}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            title="Зберегти файл як",
            defaultextension=".txt",
            filetypes=(("Текстові файли", "*.txt"), ("Усі файли", "*.*"))
        )
        if file_path:
            file_content = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_content)
            self.current_file = file_path
            messagebox.showinfo("Зберегти", f"Файл збережено: {file_path}")

    def encrypt_file(self):
        try:
            text = self.text_area.get(1.0, tk.END).strip()

            key_str = self.key_entry.get().strip()
            key = Key.parse(key_str)
            encrypted = BookCipher.encode(text, key)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, encrypted)
            messagebox.showinfo("Шифрування", "Текст зашифровано.")
        except ValueError:
            messagebox.showerror("Помилка", "В тексті знайдено невідому літеру.")

    def decrypt_file(self):
        try:
            text = self.text_area.get(1.0, tk.END).strip()

            key_str = self.key_entry.get().strip()
            key = Key.parse(key_str)
            encrypted = BookCipher.decode(text, key)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, encrypted)
            messagebox.showinfo("Розшифрування", "Текст розшифровано.")
        except ValueError:
            messagebox.showerror("Помилка", "В тексті знайдено невідому літеру.")

    def quit_app(self):
        self.quit()

    def about(self):
        messagebox.showinfo("Про програму",
                            "Ця програма реалізує книжковий шифр. "
                            "Автор: Іван Куруч.")


if __name__ == "__main__":
    app = BookCipherApp()
    app.mainloop()
