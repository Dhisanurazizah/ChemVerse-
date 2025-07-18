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

    /* Sidebar background image and text style */
    [data-testid="stSidebar"] {
        background-image: url("https://png.pngtree.com/element_our/20200610/ourmid/pngtree-chemical-icon-image_2249324.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        color: black;
    }

    /* Optional: add overlay to improve text contrast */
    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(255, 215, 0, 0.6);  /* violet overlay */
        z-index: 0;
    }

    /* Ensure sidebar content appears above overlay */
    [data-testid="stSidebar"] > div:first-child {
        position: relative;
        z-index: 1;
        font-family: "Times New Roman", Times, serif;
        font-weight: bold;
    }

    /* Sidebar selectbox label & item text */
    [data-testid="stSidebar"] .css-1cpxqw2,  /* label */
    [data-testid="stSidebar"] .css-1d391kg {  /* menu item */
        color: black !important;
        font-weight: bold;
        font-family: "Times New Roman", Times, serif !important;
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

# ------------------ Judul Aplikasi ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")
st.markdown(
    """
    <style>
    /* Import font dari Google Fonts */
   https://www.creativefabrica.com/wp-content/uploads/2023/03/19/Aesthetic-Fonts-64760718-1.jpg

    /* Ganti style judul aplikasi */
    .judul-aesthetic {
        font-family: 'Pacifico', cursive;
        font-size: 48px;
        color: #ffffff;
        text-align: center;
        padding-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Sidebar Navigasi ------------------
menu = st.sidebar.selectbox(
    "📘 Menu Navigasi",
    [
        "Beranda",
        "Tentang Kami",
        "Tentang Aplikasi",
        "Hitung Mol",
        "Hitung pH",
        "Pengenceran Larutan",
        "Persentase Konsentrasi"
    ]
)

# ------------------ Halaman Beranda ------------------
if menu == "Beranda":
    st.header("Selamat datang di ChemVerse - Aplikasi Kimia Pintar 🎉")
    st.image("https://img.freepik.com/vektor-gratis/latar-belakang-kimia-digambar-tangan_23-2148164901.jpg", use_column_width=True)
    st.markdown("""
    Bersama aplikasi ini, mari wujudkan perhitungan kimia yang cepat, cerdas, dan praktis.  
    Saatnya mahasiswa bergerak lebih digital di era Revolusi 4.0!  
    Aplikasi ini dirancang untuk mendukung aktivitas perkuliahan, praktikum, dan penelitian kimiamu dengan pendekatan teknologi yang efisien dan akurat.  
    **ChemVerse** menggabungkan teknologi dan pendidikan untuk membawamu ke level baru dalam memahami dunia kimia.  
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikummu.  
    **Semua perhitungan kimia kini bisa kamu lakukan dalam satu aplikasi.**
    """)

# ------------------ Tentang Kami ------------------
elif menu == "Tentang Kami":
    st.subheader("👥 Tentang Kami")
    st.markdown("""
    **TIM PENYUSUN**  
    *Kelompok 3 - 1 D*  
    1. Andrian Prayugo (2460324)  
    2. Dhisa Nur Azizah (2460358)  
    3. Marcelino David Mangatur (2460411)  
    4. Nabil Syafiq Suhendar (2460446)  
    5. Sefina Zahra Pangestika (2460515)
    """)

# ------------------ Tentang Aplikasi ------------------
elif menu == "Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi")
    st.markdown("""
    🧪 ChemVerse  
    *“Your Chemistry Universe in One App”*

    **📌 Deskripsi Singkat**  
    ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas. Dirancang untuk mempermudah perhitungan kimia sekaligus menjadi ruang eksplorasi konsep kimia dalam satu ekosistem terintegrasi.

    **🔍 Latar Belakang**  
    Di era Revolusi Industri 4.0, integrasi teknologi dalam pendidikan dan industri kimia menjadi sebuah keharusan. ChemVerse hadir untuk menjawab tantangan tersebut dengan menghadirkan solusi perhitungan kimia yang cepat, akurat, dan berbasis teknologi digital. 

    **🎯 Tujuan Aplikasi**  
    Aplikasi ini dibuat untuk :
    1. Mempermudah proses perhitungan kimia dasar.
    2. Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi.
    3. Menghemat waktu dalam kegiatan laboratorium.
    4. Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa.
    5. Mendukung pelajar, mahasiswa, dosen, dan profesional industri dalam memahami dan mengaplikasikan konsep kimia secara efisien dan intuitif.

    **⚙️ Fitur Unggulan ChemVerse**  
    1. Perhitungan Molaritas  
    2. Perhitungan pH  
    3. Pengenceran Larutan  
    4. Perhitungan Persentase Konsentrasi 

    **🎯 Manfaat Aplikasi**  
    1. Membantu proses belajar dan praktikum secara mandiri maupun kelompok.  
    2. Menurunkan tingkat kesalahan hitung manual.  
    3. Menghemat waktu dalam analisis kimia.  
    4. Mendorong adaptasi teknologi digital di dunia pendidikan dan industri kimia.
    """)

# ------------------ Hitung Mol ------------------
elif menu == "Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("Rumus: `mol = massa / Mr`")
    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.0)
    if massa > 0 and mr > 0:
        mol = massa / mr
        st.success(f"Jumlah mol = {mol:.4f} mol")

# ------------------ Hitung pH ------------------
elif menu == "Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("Rumus: `pH = -log[H⁺]`")
    h_concentration = st.number_input("Masukkan konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")
    if h_concentration > 0:
        ph = -math.log10(h_concentration)
        st.success(f"pH = {ph:.2f}")

# ------------------ Pengenceran Larutan ------------------
elif menu == "Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("Rumus: `M₁V₁ = M₂V₂`")
    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.0)
    if m1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.success(f"Volume akhir (V₂) = {v2:.2f} mL")

# ------------------ Persentase Konsentrasi ------------------
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

# ------------------ SMART QUIZIZ ------------------
elif menu == "Smart Quiziz":
    st.header("🧪 SMART QUIZIZ")
    st.markdown("Uji pemahamanmu tentang konsep dasar kimia melalui kuis singkat berikut!")

    score = 0  # Nilai awal

    # Question 1
    st.subheader("1. Apa satuan dari molaritas?")
    q1 = st.radio("Pilih jawaban:", ["mol", "mol/L", "gram", "L/mol"], key="q1")
    if q1 == "mol/L":
        score += 1

    # Question 2
    st.subheader("2. Seseorang melarutkan 10 gram NaCl (Mr = 58,5 g/mol) ke dalam air hingga larut sempurna. Berapakah jumlah mol NaCl yang terlarut?...")
    q2 = st.radio("Pilih jawaban:", ["0,15 mol", "0,17 mol", "0,18 mol", "0,20 mol"], key="q2")
    if q2 == "0.17 mol":
        score += 1

    # Question 3
    st.subheader("3. Rumus pengenceran larutan adalah...")
    q3 = st.radio("Pilih jawaban:", ["M1 + M2 = V", "M1V1 = M2V2", "M = mol × V", "M1V2 = M2V1"], key="q3")
    if q3 == "M1V1 = M2V2":
        score += 1

    # Question 4
    st.subheader("4. Jika H⁺ = 1 × 10⁻³ mol/L, maka pH-nya adalah...")
    q4 = st.radio("Pilih jawaban:", ["3", "4", "7", "10"], key="q4")
    if q4 == "3":
        score += 1

    # Question 5
    st.subheader("5. Massa molar dari H₂O adalah...")
    q5 = st.radio("Pilih jawaban:", ["16 g/mol", "18 g/mol", "20 g/mol", "10 g/mol"], key="q5")
    if q5 == "18 g/mol":
        score += 1

    # Tombol untuk submit jawaban
    if st.button("Lihat Skor"):
        st.success(f"Skor kamu: {score} dari 5 soal")

        if score == 5:
            st.balloons()
            st.success("🎉 Hebat! Kamu menguasai dasar-dasar kimia dengan sangat baik.")
        elif score >= 3:
            st.info("👍 Lumayan! Tingkatkan lagi pemahamanmu ya.")
        else:
            st.warning("📚 Yuk, belajar lagi. Jangan menyerah!")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat untuk Pembelajaran</div>",
    unsafe_allow_html=True
)
