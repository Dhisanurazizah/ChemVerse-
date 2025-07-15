import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                          url("https://static.vecteezy.com/system/resources/previews/001/987/697/non_2x/abstract-hexagon-pattern-dark-blue-background-medical-and-science-concept-molecular-structures-free-vector.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }

    .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background-image: linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%);
        color: black;
    }

    .stNumberInput > div > div {
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    ul {
        margin-left: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Judul ------------------
st.title("🧪 Kalkulator Kimia Interaktif")

# ------------------ Menu di Sidebar ------------------
menu = st.sidebar.selectbox(
    "📘 Menu Navigasi",
    [
        "Tentang Aplikasi",
        "Tujuan Aplikasi",
        "Hitung Mol",
        "Hitung pH",
        "Pengenceran Larutan",
        "Persentase Konsentrasi"
    ]
)

# ------------------ Tampilan Berdasarkan Menu ------------------
if menu == "Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini membantu siswa dan mahasiswa dalam melakukan perhitungan kimia dasar secara cepat dan interaktif.

    **Materi yang Dihitung:**
    - **Mol:** Menghitung jumlah mol berdasarkan massa dan Mr  
    - **pH:** Menghitung tingkat keasaman larutan dari [H⁺]  
    - **Pengenceran Larutan:** Menggunakan rumus M₁V₁ = M₂V₂  
    - **Persentase Konsentrasi:** Menghitung kadar zat terlarut dalam larutan
    """)

elif menu == "Tujuan Aplikasi":
    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat untuk:
    - Mempermudah proses perhitungan kimia dasar  
    - Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi  
    - Menghemat waktu dalam kegiatan laboratorium  
    - Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa
    """)

elif menu == "Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("Rumus: `mol = massa / Mr`")
    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.0)
    if massa > 0 and mr > 0:
        mol = massa / mr
        st.success(f"Jumlah mol = {mol:.4f} mol")

elif menu == "Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("Rumus: `pH = -log[H⁺]`")
    h_concentration = st.number_input("Masukkan konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")
    if h_concentration > 0:
        ph = -math.log10(h_concentration)
        st.success(f"pH = {ph:.2f}")

elif menu == "Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("Rumus: `M₁V₁ = M₂V₂`")
    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.0)
    if m1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.success(f"Volume akhir (V₂) = {v2:.2f} mL")

elif menu == "Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("Rumus: `(massa zat / massa larutan) × 100%`")
    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0)
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.0)
    if massa_zat > 0 and massa_larutan > 0:
        if massa_zat <= massa_larutan:
            persen = (massa_zat / massa_larutan) * 100
            st.success(f"Persentase Konsentrasi = {persen:.2f}%")
        else:
            st.error("❌ Massa zat tidak boleh lebih besar dari massa larutan.")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 Kalkulator Kimia | Dibuat untuk Pembelajaran</div>",
    unsafe_allow_html=True
)
