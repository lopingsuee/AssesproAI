import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Saya",
    page_icon="Assespro.jpg",
    layout="wide"
)

# Buat 2 kolom: kiri untuk logo, kanan untuk judul
col_logo, col_title = st.columns([1, 9])

with col_logo:
    st.image("Assespro.jpg", width=100)  # tampilkan logo

with col_title:
    st.title("Dashboard Analitik")
    st.write("Selamat datang di dashboard interaktif berbasis Streamlit!")

# Contoh metrik
col1, col2, col3 = st.columns(3)
col1.metric("Total Pengguna", "1,245", "+15%")
col2.metric("Pendapatan", "Rp 84.500.000", "+5%")
col3.metric("Retensi", "92%", "-2%")

# Data contoh
data = pd.DataFrame(np.random.randn(50, 3), columns=["Produk A", "Produk B", "Produk C"])

# Grafik dan tabel
st.subheader("Tren Penjualan Mingguan")
st.line_chart(data)

st.subheader("Data Penjualan Terbaru")
st.dataframe(data.head(10))
