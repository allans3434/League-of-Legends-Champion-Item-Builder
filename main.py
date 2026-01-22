import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)

CHAMPIONS = [
    {"name": "Ahri", "img": "images/champions/ahri.png"},
    {"name": "Garen", "img": "images/champions/garen.png"},
    {"name": "Jinx", "img": "images/champions/jinx.png"},
    {"name": "Singed", "img": "images/champions/singed.png"},
    {"name": "Shaco", "img": "images/champions/shaco.png"},
    {"name": "Gragas", "img": "images/champions/gragas.png"},
]

BUILDS = {
    "Ahri": [
        {"name": "Luden's Companion", "img": "images/items/ludens.png"},
        {"name": "Shadowflame", "img": "images/items/shadowflame.png"},
        {"name": "Rabadon's Deathcap", "img": "images/items/rabadons.png"},
    ],
    "Garen": [
        {"name": "Stridebreaker", "img": "images/items/stridebreaker.png"},
        {"name": "Dead Man's Plate", "img": "images/items/deadmans.png"},
        {"name": "Sterak's Gage", "img": "images/items/steraks.png"},
    ],
    "Jinx": [
        {"name": "Kraken Slayer", "img": "images/items/kraken.png"},
        {"name": "Infinity Edge", "img": "images/items/infinity_edge.png"},
        {"name": "Runaan's Hurricane", "img": "images/items/runaans.png"},
    ],
    "Singed": [
        {"name": "Rylai's Crystal Scepter", "img": "images/items/rylais.png"},
        {"name": "Demonic Embrace", "img": "images/items/demonic.png"},
        {"name": "Liandry's Torment", "img": "images/items/liandry.png"},
    ],
    "Shaco": [
        {"name": "Duskblade of Draktharr", "img": "images/items/duskblade.png"},
        {"name": "Essence Reaver", "img": "images/items/essence_reaver.png"},
        {"name": "The Collector", "img": "images/items/collector.png"},
    ],
    "Gragas": [
        {"name": "Everfrost", "img": "images/items/everfrost.png"},
        {"name": "Cosmic Drive", "img": "images/items/cosmic_drive.png"},
        {"name": "Zhonya's Hourglass", "img": "images/items/zhonyas.png"},
    ],
}

class LoLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LoL Item Builder")
        self.geometry("820x560")
        self.configure(bg="#0f172a")

        tk.Label(
            self,
            text="League of Legends Item Builder",
            font=("Helvetica", 18, "bold"),
            fg="#e5e7eb",
            bg="#0f172a"
        ).pack(pady=14)

        tk.Label(
            self,
            text="Izvēlies čempionu",
            font=("Helvetica", 12),
            fg="#94a3b8",
            bg="#0f172a"
        ).pack()

        self._img_cache = {}

        self.top = tk.Frame(self, bg="#0f172a")
        self.top.pack(pady=18)

        for i, c in enumerate(CHAMPIONS):
            champ_img = self.load_image(c["img"], (96, 96))
            btn = tk.Button(
                self.top,
                image=champ_img,
                text=c["name"],
                compound="top",
                font=("Helvetica", 10, "bold"),
                fg="#e5e7eb",
                bg="#1e293b",
                activebackground="#334155",
                activeforeground="#ffffff",
                bd=0,
                padx=14,
                pady=12,
                command=lambda name=c["name"]: self.show_build(name)
            )
            btn.grid(row=i // 3, column=i % 3, padx=18, pady=10)

        self.items_title = tk.Label(
            self,
            text="Izvēlies čempionu, lai redzētu itemus",
            font=("Helvetica", 12, "bold"),
            fg="#e5e7eb",
            bg="#0f172a"
        )
        self.items_title.pack(pady=(8, 6))

        self.items_area = tk.Frame(self, bg="#020617")
        self.items_area.pack(fill="both", expand=True, padx=18, pady=14)

    def load_image(self, rel_path, size):
        full = resource_path(rel_path)
        key = (full, size)
        if key in self._img_cache:
            return self._img_cache[key]
        img = Image.open(full).resize(size)
        photo = ImageTk.PhotoImage(img)
        self._img_cache[key] = photo
        return photo

    def clear_items(self):
        for w in self.items_area.winfo_children():
            w.destroy()

    def show_build(self, champion):
        self.items_title.config(text=f"{champion} — ieteiktie itemi")
        self.clear_items()

        items = BUILDS.get(champion, [])
        if not items:
            tk.Label(
                self.items_area,
                text="Nav itemu datu šim čempionam.",
                font=("Helvetica", 12),
                fg="#e5e7eb",
                bg="#020617"
            ).pack(pady=20)
            return

        grid = tk.Frame(self.items_area, bg="#020617")
        grid.pack(pady=18)

        cols = 3
        for i, it in enumerate(items):
            r = i // cols
            c = i % cols

            card = tk.Frame(grid, bg="#0b1220")
            card.grid(row=r, column=c, padx=18, pady=14)

            item_img = self.load_image(it["img"], (72, 72))
            tk.Label(card, image=item_img, bg="#0b1220").pack(padx=14, pady=(14, 8))

            tk.Label(
                card,
                text=it["name"],
                font=("Helvetica", 10, "bold"),
                fg="#e5e7eb",
                bg="#0b1220",
                wraplength=170,
                justify="center"
            ).pack(padx=12, pady=(0, 14))

if __name__ == "__main__":
    app = LoLApp()
    app.mainloop()
