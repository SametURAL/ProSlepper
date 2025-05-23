# Alarm Sistemi - Bulanık Mantık Tabanlı Uyanma Yardımcısı

Bu proje, kullanıcının uyku kalitesi, uyanma süresi, çevresel gürültü seviyesi, gün ve iş miktarına göre bulanık mantık (fuzzy logic) kullanarak alarm şiddeti ve müzik türü öneren bir alarm sistemi arayüzü sunar.

![Uyku Grafiği]([https://github.com/SametURAL/ProSlepper/blob/main/A.png?raw=true])


## Özellikler

- **Kullanıcı Girdileri:**  
  - Uyku süresi (saat)  
  - Uyanma süresi (dakika)  
  - Gürültü seviyesi (0-100)  
  - Gün seçimi (Hafta içi, Cumartesi, Pazar)  
  - İş miktarı (0-100)  

- **Çıktılar:**  
  - Alarm şiddeti (Düşük, Orta, Yüksek)  
  - Müzik türü (Rahatlatıcı, Orta, Canlandırıcı)  
  - Grafiksel gösterim (matplotlib ile)  
  - Alarm ve müzik türüne göre açıklamalar

---

## Kurulum ve Çalıştırma

1. Python 3.x yüklü olmalıdır.  
2. Gerekli kütüphaneleri yükleyin:  
   ```bash
   pip install matplotlib tkinter


