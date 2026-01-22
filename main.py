import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup

CHAMPIONS = {
    "Ahri": "images/ahri.png",
    "Garen": "images/garen.png",
    "Jinx": "images/jinx.png",
}

def get_items_from_opgg(champion):
    try:
        url = f"https://www.op.gg/champions/{champion.lower()}/build"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        items = []
        for img in soup.select("img[alt]"):
            alt = img.get("alt")
            if alt and "Item" in alt:
                items.append(alt.replace(" Item", ""))
        return list(dict.fromkeys(items))[:6] or ["Neizdevās ielādēt itemus"]
    except Exception:
        return ["Kļūda savienojumā ar op.gg"]

class LoLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LoL Item Builder")
        self.geometry("600x450")
        self.configure(bg="#0f172a")

        self.title_label = tk.Label(
            self,
            text="League of Legends Item Builder",
            font=("Helvetica", 18, "bold"),
            fg="#e5e7eb",
            bg="#0f172a"
        )
        self.title_label.pack(pady=15)

        self.subtitle = tk.Label(
            self,
            text="Izvēlies čempionu",
            font=("Helvetica", 12),
            fg="#94a3b8",
            bg="#0f172a"
        )
        self.subtitle.pack()

        self.frame = tk.Frame(self, bg="#0f172a")
        self.frame.pack(pady=20)

        self.images = {}
        for champ, img_path in CHAMPIONS.items():
            img = Image.open(img_path).resize((90, 90))
            photo = ImageTk.PhotoImage(img)
            self.images[champ] = photo

            btn = tk.Button(
                self.frame,
                image=photo,
                text=champ,
                compound="top",
                font=("Helvetica", 10, "bold"),
                fg="#e5e7eb",
                bg="#1e293b",
                activebackground="#334155",
                activeforeground="#ffffff",
                bd=0,
                padx=10,
                pady=10,
                command=lambda c=champ: self.show_items(c)
            )
            btn.pack(side="left", padx=12)

        self.text_frame = tk.Frame(self, bg="#020617")
        self.text_frame.pack(fill="both", expand=True, padx=20, pady=15)

        self.text = tk.Text(
            self.text_frame,
            height=10,
            bg="#020617",
            fg="#e5e7eb",
            font=("Consolas", 11),
            insertbackground="white",
            bd=0
        )
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

    def show_items(self, champion):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, f" {champion} - ieteiktie itemi:\n")
")
        items = get_items_from_opgg(champion)
        for item in items:
            self.text.insert(tk.END, f"• {item}
")
    def __init__(self):
        super().__init__()
        self.title("LoL Item Builder")
        self.geometry("500x400")

        tk.Label(self, text="Izvēlies čempionu", font=("Arial", 16)).pack(pady=10)

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.images = {}
        for champ, img_path in CHAMPIONS.items():
            img = Image.open(img_path).resize((80, 80))
            photo = ImageTk.PhotoImage(img)
            self.images[champ] = photo

            btn = tk.Button(self.frame, image=photo, text=champ, compound="top",
                            command=lambda c=champ: self.show_items(c))
            btn.pack(side="left", padx=10)

        self.text = tk.Text(self, height=10, width=55)
        self.text.pack(pady=15)

    def show_items(self, champion):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, f"Itemi priekš {champion}:\n\n")
        items = get_items_from_opgg(champion)
        for item in items:
            self.text.insert(tk.END, f"- {item}\n")

if __name__ == "__main__":
    app = LoLApp()
    app.mainloop()
