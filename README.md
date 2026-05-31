#  Bitki Hastalık Tespit Sistemi (Plant Disease Detection)              Efe Yılmaz 22370031038

##  Proje Amacı
Bu proje, yaprak görüntülerinden bitki türü ve hastalık tespiti yapabilen bir derin öğrenme (CNN) tabanlı web uygulamasıdır. Amaç, tarım alanında hastalıkların hızlı ve otomatik şekilde tespit edilmesini sağlamaktır.

Proje, Streamlit kullanılarak web tabanlı bir arayüze dönüştürülmüştür.

---

##  Model Performansı

- Dataset içi doğruluk: **%98.41**
- Gerçek dünya (Google görselleri): **%94.58**

---

##  Sistem Özellikleri

-  Kullanıcıdan yaprak fotoğrafı yükleme
-  Dataset içerisinden rastgele test görüntüsü seçme
-  Bitki türü tespiti
-  Hastalık sınıflandırması
-  Güven (confidence) oranı gösterimi
-  Web tabanlı Streamlit arayüzü

---
##  Model Dosyası

Model dosyası GitHub limitinden dolayı ayrı paylaşılmıştır.

İndirme linki:
https://drive.google.com/file/d/1_yVu54pDItvENHs8misDOyW44rEQLXu8/view?usp=drive_link

---
##  Kullanılan Teknolojiler

- Python 
- TensorFlow / Keras 
- Convolutional Neural Networks (CNN)
- Streamlit 
- NumPy
- Pillow (PIL)

---

##  Sistem Görselleri

<img width="1919" height="1026" alt="Ekran görüntüsü 2026-05-14 154021" src="https://github.com/user-attachments/assets/77fa9138-b06f-4265-9f30-a6f11efabad6" />

<img width="1919" height="1032" alt="Ekran görüntüsü 2026-05-14 153824" src="https://github.com/user-attachments/assets/9a21aff6-503d-439e-b741-da9cabadf7b0" />

###  Model Eğitim Süreci
<img width="1024" height="107" alt="Ekran görüntüsü 2026-05-14 210236" src="https://github.com/user-attachments/assets/13fb0001-11c6-40b1-8f40-8bb1708dd1bb" />

---

##  Kurulum ve Çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
