import streamlit as st
import numpy as np
import os
import random
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# =========================
# MODEL
# =========================
model = load_model("bitki_hastalik_modeli.h5")

veri_yolu = "PlantVillage"
sinif_isimleri = sorted(os.listdir(veri_yolu))

# =========================
# TÜRKÇE ÇEVİRİLER
# =========================
bitki_ceviri = {
    "Tomato": "Domates",
    "Potato": "Patates",
    "Pepper": "Biber",
    "Apple": "Elma",
    "Grape": "Üzüm",
    "Orange": "Portakal",
    "Cherry": "Kiraz",
    "Peach": "Şeftali"
}

hastalik_ceviri = {
    "Early_blight": "Erken yanıklık",
    "Late_blight": "Geç yanıklık",
    "healthy": "Sağlıklı",
    "Bacterial_spot": "Bakteriyel leke",
    "Leaf_Mold": "Yaprak küfü",
    "Septoria_leaf_spot": "Septorya yaprak lekesi",
    "Spider_mites_Two_spotted_spider_mite": "Örümcek akarı",
    "Target_Spot": "Hedef leke",
    "Tomato_YellowLeaf_Curl_Virus": "Sarı yaprak kıvırcık virüsü",
    "Tomato_mosaic_virus": "Mozaik virüsü"
}

# =========================
# FONKSİYON
# =========================
def parse_label(label):
    label = label.replace("__", "_")
    parts = label.split("_")

    bitki = parts[0]
    hastalik = "_".join(parts[1:])

    return bitki, hastalik

# =========================
# ARAYÜZ
# =========================
st.title("🌿 Bitki Hastalık Tespit Sistemi")

mod = st.radio(
    "Mod seç:",
    ("📤 Kendi Fotoğrafımı Yükle", "🎲 Dataset'ten Rastgele Seç")
)

# =========================
# 1. KENDİ FOTO
# =========================
if mod == "📤 Kendi Fotoğrafımı Yükle":

    uploaded_file = st.file_uploader("Fotoğraf yükle", type=["jpg","png","jpeg"])

    if uploaded_file is not None:

        st.image(uploaded_file, caption="Yüklenen Foto")

        img = image.load_img(uploaded_file, target_size=(224,224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        tahmin = model.predict(img_array)
        index = np.argmax(tahmin)
        sinif = sinif_isimleri[index]

        bitki, hastalik = parse_label(sinif)

        bitki_tr = bitki_ceviri.get(bitki, bitki)
        hastalik_tr = hastalik_ceviri.get(hastalik, hastalik)

        st.subheader("🔎 Sonuç")

        st.code(sinif)  # ORİJİNAL LABEL

        st.success(f"🌿 Bitki: {bitki_tr}")
        st.warning(f"🦠 Hastalık: {hastalik_tr}")

        st.info(f"📊 Güven: %{np.max(tahmin)*100:.2f}")

# =========================
# 2. DATASET RANDOM
# =========================
if mod == "🎲 Dataset'ten Rastgele Seç":

    if st.button("🎲 Rastgele Foto Getir"):

        sinif = random.choice(sinif_isimleri)
        klasor = os.path.join(veri_yolu, sinif)

        resim = random.choice(os.listdir(klasor))
        resim_yolu = os.path.join(klasor, resim)

        img = Image.open(resim_yolu)
        st.image(img, caption=f"Gerçek: {sinif}")

        img = img.resize((224,224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        tahmin = model.predict(img_array)
        index = np.argmax(tahmin)
        sinif_tahmin = sinif_isimleri[index]

        bitki, hastalik = parse_label(sinif_tahmin)

        bitki_tr = bitki_ceviri.get(bitki, bitki)
        hastalik_tr = hastalik_ceviri.get(hastalik, hastalik)

        st.subheader("🔎 Tahmin")

        st.code(sinif_tahmin)

        st.success(f"🌿 Bitki: {bitki_tr}")
        st.warning(f"🦠 Hastalık: {hastalik_tr}")

        st.info(f"📊 Güven: %{np.max(tahmin)*100:.2f}")