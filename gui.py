import tkinter as tk
from tkinter import ttk
from fuzzy_logic import hesapla_fuzzy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hesapla():
    try:
        uyku = float(uyku_entry.get())
        uyanma = uyanma_slider.get()
        gurultu = gurultu_slider.get()
        gun_text = gun_combobox.get()
        is_miktari = is_slider.get()

        gun_dict = {"Hafta içi": 0, "Cumartesi": 1, "Pazar": 2}
        gun = gun_dict[gun_text]

        alarm, muzik = hesapla_fuzzy(uyku, uyanma, gurultu, gun, is_miktari)

        # Alarm ve müzik seviyeleri
        if alarm < 33:
            alarm_desc = "Düşük"
        elif alarm < 66:
            alarm_desc = "Orta"
        else:
            alarm_desc = "Yüksek"

        if muzik < 33:
            muzik_desc = "Rahatlatıcı"
        elif muzik < 66:
            muzik_desc = "Orta"
        else:
            muzik_desc = "Canlandırıcı"

        # Açıklamalar
        alarm_explanation = {
            "Düşük": "Alarm hafif, sessiz bir uyanma.",
            "Orta": "Alarm orta seviyede, uyanmanız destekleniyor.",
            "Yüksek": "Alarm yüksek, sizi kesinlikle uyandıracak."
        }

        muzik_explanation = {
            "Rahatlatıcı": "Müzik türü rahatlatıcı, sakin bir başlangıç için.",
            "Orta": "Müzik orta tempoda, dengeli enerji sağlar.",
            "Canlandırıcı": "Müzik canlandırıcı, enerjik bir uyanış için."
        }

        verbal_output = (
            f"Alarm Şiddeti: {round(alarm)} ({alarm_desc})\n"
            f"{alarm_explanation[alarm_desc]}\n\n"
            f"Müzik Türü: {round(muzik)} ({muzik_desc})\n"
            f"{muzik_explanation[muzik_desc]}"
        )

        # Grafik alanını temizle
        for widget in grafik_frame.winfo_children():
            widget.destroy()

        # Grafik oluştur
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(["Alarm Şiddeti", "Müzik Türü"], [alarm, muzik], color=["skyblue", "lightcoral"])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Değer")
        ax.set_title("Duru Çıktı")

        canvas = FigureCanvasTkAgg(fig, master=grafik_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Sonuç label'ını güncelle (grafik altına 2 boşlukla ayrılmış)
        sonuc_label.config(text="\n\n" + verbal_output)

    except Exception as e:
        sonuc_label.config(text=f"Hata: {str(e)}")

# Arayüz
pencere = tk.Tk()
pencere.title("Alarm Sistemi")
pencere.geometry("750x500")
pencere.resizable(False, False)

# Sol giriş çerçevesi
input_frame = tk.Frame(pencere)
input_frame.pack(side="left", padx=10, pady=10)

tk.Label(input_frame, text="Uyku (saat):").pack(pady=2)
uyku_entry = tk.Entry(input_frame)
uyku_entry.pack(pady=2)

tk.Label(input_frame, text="Uyanma süresi (dk):").pack(pady=2)
uyanma_slider = tk.Scale(input_frame, from_=0, to=30, orient=tk.HORIZONTAL)
uyanma_slider.pack(pady=2)

tk.Label(input_frame, text="Gürültü seviyesi:").pack(pady=2)
gurultu_slider = tk.Scale(input_frame, from_=0, to=100, orient=tk.HORIZONTAL)
gurultu_slider.pack(pady=2)

tk.Label(input_frame, text="Gün:").pack(pady=2)
gun_combobox = ttk.Combobox(input_frame, values=["Hafta içi", "Cumartesi", "Pazar"])
gun_combobox.pack(pady=2)
gun_combobox.current(0)

tk.Label(input_frame, text="İş miktarı:").pack(pady=2)
is_slider = tk.Scale(input_frame, from_=0, to=100, orient=tk.HORIZONTAL)
is_slider.pack(pady=2)

hesapla_button = tk.Button(input_frame, text="HESAPLA", command=hesapla, font=("Arial", 12, "bold"),
                           height=2, width=15, bg="#4CAF50", fg="white")
hesapla_button.pack(pady=5)

# Sağ taraf: grafik + açıklama
right_frame = tk.Frame(pencere)
right_frame.pack(side="right", padx=10, pady=10)

grafik_frame = tk.Frame(right_frame)
grafik_frame.pack()

sonuc_label = tk.Label(right_frame, text="", font=("Arial", 11), justify="left", anchor="w")
sonuc_label.pack(fill="x", padx=10)

# Ana döngü
pencere.mainloop()
