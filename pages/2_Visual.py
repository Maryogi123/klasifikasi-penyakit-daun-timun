import streamlit as st
from PIL import Image

st.set_page_config(page_title="Visualisasi Performa Model", layout="centered")

st.title("Klasifikasi Penyakit Daun Tanaman Timun Berbasis Convolutional Neural Network (CNN)")
st.title("Visual")

st.markdown("""
Halaman ini menyajikan hasil evaluasi dari model CNN berbasis arsitektur **VGG16** yang telah dilatih untuk mengenali 5 kategori penyakit pada daun timun. Visualisasi ini membantu memahami **sejauh mana model mampu mengenali pola** dari gambar input berdasarkan data validasi.
""")

# Confusion Matrix
st.subheader("🧩 Confusion Matrix")
image_cm = Image.open("confusion_matrix_timun.png")
st.image(image_cm, caption="Confusion Matrix – Akurasi Prediksi per Kelas", use_container_width=True)

st.markdown("""
**Confusion Matrix** digunakan untuk melihat distribusi prediksi model terhadap kelas sebenarnya.

- **Baris** menunjukkan label sebenarnya (ground truth)
- **Kolom** menunjukkan hasil prediksi model
- Nilai diagonal menunjukkan jumlah prediksi yang benar

Semakin besar nilai diagonal, semakin baik model dalam mengenali kelas tersebut.
""")

# Classification Report - Tabel asli
st.subheader("📄 Classification Report Lengkap")
image_table = Image.open("classification_report.PNG")
st.image(image_table, caption="Tabel Classification Report dari Google Colab", use_container_width=True)

st.markdown("""
Tabel ini merupakan output asli evaluasi model yang menampilkan metrik:
- **Precision, Recall, F1-Score** untuk tiap kelas
- **Support** (jumlah sampel validasi per kelas)
- **Akurasi total**, serta **average weighted metrics**

Laporan ini berguna untuk validasi performa keseluruhan model.
""")

# Classification Report Chart
st.subheader("📊 Grafik Precision, Recall, dan F1-Score per Kelas")
image_cr = Image.open("visualisasi_classification_report.png")
st.image(image_cr, caption="Visualisasi Evaluasi Metrik per Kelas", use_container_width=True)

st.markdown("""
Grafik ini membantu membandingkan performa antar kelas dalam hal:

- **Precision**: Kemampuan model untuk tidak salah dalam memprediksi suatu kelas
- **Recall**: Kemampuan model untuk mengenali seluruh sampel yang benar
- **F1-Score**: Keseimbangan antara precision dan recall

Kombinasi tabel dan grafik memberikan gambaran lengkap tentang kekuatan dan kelemahan model klasifikasi.
""")

st.success("📍 Halaman ini merupakan bagian dari 4 halaman utama aplikasi: Beranda, Klasifikasi, Tentang, dan Visualisasi.")
