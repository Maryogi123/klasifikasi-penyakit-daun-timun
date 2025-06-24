import streamlit as st

st.set_page_config(page_title="Tentang Model", layout="centered")

st.title("Klasifikasi Penyakit Daun Tanaman Timun Berbasis Convolutional Neural Network (CNN)")
st.title("Tentang")

st.markdown("""
Aplikasi ini dikembangkan untuk mengklasifikasikan **penyakit pada daun timun** berdasarkan gambar menggunakan metode **Convolutional Neural Network (CNN)** dengan arsitektur **VGG16**.

Model ini dirancang dan dilatih untuk mengenali **5 kategori penyakit daun timun**, berdasarkan dataset yang dikumpulkan secara manual dan diproses untuk kebutuhan training.
""")

st.subheader("📊 Dataset")
st.markdown("""
- Total gambar: **2.000**
- Dibagi menjadi tiga bagian:
  - **80%** untuk pelatihan (**training**)
  - **10%** untuk pengujian (**testing**)
  - **10%** untuk validasi (**validation**)
""")

st.subheader("⚙️ Arsitektur Model")
st.markdown("""
Model ini menggunakan **VGG16** sebagai backbone, yaitu arsitektur CNN yang telah terbukti efektif dalam berbagai tugas klasifikasi citra. VGG16 memiliki 16 lapisan (13 convolutional, 3 fully connected) dan dilengkapi dengan bobot awal pre-trained dari ImageNet untuk meningkatkan performa pelatihan awal (transfer learning).

Beberapa tahapan utama:
- Resize gambar ke ukuran **224x224 piksel**
- **Preprocessing** sesuai standar VGG16 (`preprocess_input`)
- **Fine-tuning** layer akhir
- **Augmentasi** gambar pada training set
""")

st.subheader("🎯 Performa Model")
st.markdown("""
Model yang telah dilatih menunjukkan performa sebagai berikut:

- **Akurasi pada dataset validasi**: **76,50%**
- **Akurasi pada dataset test**: **76,50%**

Evaluasi dilakukan menggunakan metrik:
- **Confusion Matrix**
- **Classification Report** (Precision, Recall, F1-score per kelas)
""")

st.info("Model ini masih dapat dikembangkan lebih lanjut dengan data tambahan, fine-tuning lanjutan, atau teknik augmentasi yang lebih beragam.")

