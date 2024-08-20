import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

import pandas as pd

data = {
    'title': [
        # İngilizce Filmler
        'The Matrix', 
        'Inception', 
        'Interstellar', 
        'The Dark Knight', 
        'The Prestige', 
        'The Shawshank Redemption', 
        'The Godfather', 
        'Forrest Gump', 
        'Pulp Fiction', 
        'Fight Club', 
        'The Lord of the Rings: The Return of the King', 
        'The Empire Strikes Back', 
        'Gladiator', 
        'The Silence of the Lambs', 
        'Schindler\'s List',
        
        # Türkçe Filmler
        'Recep İvedik', 
        'Aşk Tesadüfleri Sever', 
        'Eyyvah Eyvah', 
        'İncir Reçeli', 
        'Issız Adam', 
        'Gelinim Mutfakta', 
        'Kardeşim Benim', 
        'Ayla', 
        'Kötü Kedi Şerafettin', 
        'Dünyayı Kurtaran Adam', 
        'Güneşin Oğlu', 
        'Müslüm', 
        'Bir İstanbul Masalı', 
        'Görümce', 
        'Ayla: The Daughter of War'
    ]
}

df = pd.DataFrame(data)
df = pd.DataFrame(data)

def rastgele_film_sec():
    random_film = df['title'].sample().values[0]
    messagebox.showinfo("Tavsiye Edilen Film", f"Bugün izlemenizi önerdiğimiz film: {random_film}")

root = tk.Tk()
root.title("Film Tavsiye Sistemi")

root.geometry('300x150')

buton = tk.Button(root, text="Film Öner", command=rastgele_film_sec)
buton.pack(pady=20)

root.mainloop()
