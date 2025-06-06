import streamlit as st
import pandas as pd
import pickle

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# --- Fungsi untuk Memuat Model ---
# Menggunakan cache agar model tidak di-load ulang setiap kali ada interaksi
@st.cache_resource
def load_model():
    """Fungsi untuk memuat model dan label encoder dari file pickle."""
    try:
        with open('model.pkl', 'rb') as f_model:
            model = pickle.load(f_model)
        with open('label_encoder.pkl', 'rb') as f_le:
            le = pickle.load(f_le)
        return model, le
    except FileNotFoundError:
        st.error("File model atau label encoder tidak ditemukan. Pastikan 'model.pkl' dan 'label_encoder.pkl' ada di folder yang sama.")
        return None, None

# Memuat model di awal
model, le = load_model()

# --- Judul dan Deskripsi Aplikasi ---
st.title("🎓 Prediksi Status Kelulusan Mahasiswa")
st.write(
    "Aplikasi ini menggunakan model Machine Learning untuk memprediksi apakah seorang mahasiswa "
    "berpotensi **Lulus (Graduate)** atau **Dropout**. Masukkan data mahasiswa di bawah ini untuk melihat prediksinya."
)
st.markdown("---")


# --- Memastikan Model Terload Sebelum Menampilkan Input ---
if model is not None and le is not None:
    # --- Membuat Kolom untuk Input ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Masukkan Data Mahasiswa")

        # Membuat expander untuk mengelompokkan input
        with st.expander("📊 Data Demografi & Pribadi"):
            # Menggunakan kolom agar tampilan lebih rapi
            c1, c2, c3 = st.columns(3)
            with c1:
                Marital_status = c1.selectbox('Status Pernikahan', [1, 2, 3, 4, 5, 6], format_func=lambda x: {1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto Union', 6: 'Legally Seperated'}[x])
                Gender = c1.selectbox('Jenis Kelamin', [0, 1], format_func=lambda x: {1: 'Pria', 0: 'Wanita'}[x])
            with c2:
                Nacionality = c2.selectbox('Kewarganegaraan', [1] + list(range(2, 22)), help="1 untuk Portuguese")
                International = c2.selectbox('Mahasiswa Internasional?', [0, 1], format_func=lambda x: {0: 'Tidak', 1: 'Ya'}[x])
            with c3:
                Age_at_enrollment = c3.number_input('Usia saat Pendaftaran', min_value=17, max_value=70, value=20)
                Displaced = c3.selectbox('Mahasiswa Pindahan?', [0, 1], format_func=lambda x: {0: 'Tidak', 1: 'Ya'}[x])

        with st.expander("📚 Data Pendaftaran & Kualifikasi Sebelumnya"):
            c1, c2, c3 = st.columns(3)
            with c1:
                Application_mode = c1.number_input('Mode Pendaftaran', min_value=1, max_value=50, value=17)
                Application_order = c1.number_input('Urutan Pilihan Jurusan', min_value=0, max_value=10, value=1)
                Course = c1.number_input('Kode Jurusan', min_value=1, max_value=9999, value=9254)
                Previous_qualification = c1.number_input('Kualifikasi Sebelumnya', min_value=1, max_value=50, value=1)
            with c2:
                Mothers_qualification = c2.number_input('Kualifikasi Ibu', min_value=1, max_value=50, value=19)
                Fathers_qualification = c2.number_input('Kualifikasi Ayah', min_value=1, max_value=50, value=12)
                Mothers_occupation = c2.number_input('Pekerjaan Ibu', min_value=0, max_value=20, value=5)
                Fathers_occupation = c2.number_input('Pekerjaan Ayah', min_value=0, max_value=20, value=9)
            with c3:
                Admission_grade = c3.number_input('Nilai Pendaftaran', min_value=0.0, max_value=200.0, value=127.3, step=0.1)
                Previous_qualification_grade = c3.number_input('Nilai Kualifikasi Sebelumnya', min_value=0.0, max_value=200.0, value=122.0, step=0.1)
                Daytime_evening_attendance = c3.selectbox('Waktu Kuliah', [0, 1], format_func=lambda x: {1: 'Siang', 0: 'Malam'}[x])
        
        with st.expander("💰 Data Finansial & Kebutuhan Khusus"):
            c1, c2, c3 = st.columns(3)
            with c1:
                 Debtor = c1.selectbox('Memiliki Hutang?', [0, 1], format_func=lambda x: {0: 'Tidak', 1: 'Ya'}[x])
            with c2:
                Tuition_fees_up_to_date = c2.selectbox('SPP Lancar?', [0, 1], format_func=lambda x: {1: 'Ya', 0: 'Tidak'}[x])
            with c3:
                Scholarship_holder = c3.selectbox('Penerima Beasiswa?', [0, 1], format_func=lambda x: {0: 'Tidak', 1: 'Ya'}[x])
                Educational_special_needs = c3.selectbox('Kebutuhan Khusus?', [0, 1], format_func=lambda x: {0: 'Tidak', 1: 'Ya'}[x])

        with st.expander("📈 Data Akademik Semester 1"):
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                Curricular_units_1st_sem_credited = c1.number_input('SKS Diakui (Sem 1)', min_value=0, max_value=30, value=0)
                Curricular_units_1st_sem_enrolled = c1.number_input('SKS Diambil (Sem 1)', min_value=0, max_value=30, value=6)
            with c2:
                Curricular_units_1st_sem_evaluations = c2.number_input('Jumlah Ujian (Sem 1)', min_value=0, max_value=50, value=8)
                Curricular_units_1st_sem_approved = c2.number_input('SKS Lulus (Sem 1)', min_value=0, max_value=30, value=6)
            with c3:
                Curricular_units_1st_sem_grade = c3.number_input('Rata-rata Nilai (Sem 1)', min_value=0.0, max_value=20.0, value=14.0, step=0.1)
            with c4:
                Curricular_units_1st_sem_without_evaluations = c4.number_input('SKS Tanpa Ujian (Sem 1)', min_value=0, max_value=20, value=0)

        with st.expander("📉 Data Akademik Semester 2"):
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                Curricular_units_2nd_sem_credited = c1.number_input('SKS Diakui (Sem 2)', min_value=0, max_value=30, value=0)
                Curricular_units_2nd_sem_enrolled = c1.number_input('SKS Diambil (Sem 2)', min_value=0, max_value=30, value=6)
            with c2:
                Curricular_units_2nd_sem_evaluations = c2.number_input('Jumlah Ujian (Sem 2)', min_value=0, max_value=50, value=8)
                Curricular_units_2nd_sem_approved = c2.number_input('SKS Lulus (Sem 2)', min_value=0, max_value=30, value=6)
            with c3:
                Curricular_units_2nd_sem_grade = c3.number_input('Rata-rata Nilai (Sem 2)', min_value=0.0, max_value=20.0, value=13.5, step=0.1)
            with c4:
                Curricular_units_2nd_sem_without_evaluations = c4.number_input('SKS Tanpa Ujian (Sem 2)', min_value=0, max_value=20, value=0)

        with st.expander("🌍 Data Ekonomi Makro"):
            c1, c2, c3 = st.columns(3)
            with c1:
                Unemployment_rate = c1.number_input('Tingkat Pengangguran', min_value=-5.0, max_value=20.0, value=12.4, step=0.1)
            with c2:
                Inflation_rate = c2.number_input('Tingkat Inflasi', min_value=-5.0, max_value=5.0, value=1.2, step=0.1)
            with c3:
                GDP = c3.number_input('GDP', min_value=-5.0, max_value=5.0, value=0.32, step=0.01)


    # --- Tombol Prediksi dan Logika ---
    with col2:
        st.header("Hasil Prediksi")
        
        # Tombol untuk memicu prediksi
        if st.button('Cek Prediksi Status', type="primary", use_container_width=True):
            # Mengumpulkan semua input menjadi satu dictionary
            input_data = {
                'Marital_status': Marital_status,
                'Application_mode': Application_mode,
                'Application_order': Application_order,
                'Course': Course,
                'Daytime_evening_attendance': Daytime_evening_attendance,
                'Previous_qualification': Previous_qualification,
                'Previous_qualification_grade': Previous_qualification_grade,
                'Nacionality': Nacionality,
                'Mothers_qualification': Mothers_qualification,
                'Fathers_qualification': Fathers_qualification,
                'Mothers_occupation': Mothers_occupation,
                'Fathers_occupation': Fathers_occupation,
                'Admission_grade': Admission_grade,
                'Displaced': Displaced,
                'Educational_special_needs': Educational_special_needs,
                'Debtor': Debtor,
                'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
                'Gender': Gender,
                'Scholarship_holder': Scholarship_holder,
                'Age_at_enrollment': Age_at_enrollment,
                'International': International,
                'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
                'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
                'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
                'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
                'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
                'Curricular_units_1st_sem_without_evaluations': Curricular_units_1st_sem_without_evaluations,
                'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
                'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
                'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
                'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
                'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
                'Curricular_units_2nd_sem_without_evaluations': Curricular_units_2nd_sem_without_evaluations,
                'Unemployment_rate': Unemployment_rate,
                'Inflation_rate': Inflation_rate,
                'GDP': GDP
            }

            # Membuat DataFrame dari dictionary
            input_df = pd.DataFrame([input_data])
            
            # Melakukan prediksi
            prediction_num = model.predict(input_df)[0]
            prediction_label = le.inverse_transform([prediction_num])[0]
            prediction_proba = model.predict_proba(input_df)[0]
            
            # Mendapatkan tingkat kepercayaan
            confidence = prediction_proba[prediction_num]
            
            # Menampilkan hasil
            if prediction_label == 'Graduate':
                st.success(f"Mahasiswa diprediksi akan **{prediction_label.upper()}**")
                st.metric(label="Tingkat Kepercayaan", value=f"{confidence:.2%}")
                st.balloons()
            else: # Dropout
                st.error(f"Mahasiswa diprediksi akan **{prediction_label.upper()}**")
                st.metric(label="Tingkat Kepercayaan", value=f"{confidence:.2%}")

            st.write("Probabilitas untuk setiap kelas:")
            st.write(pd.DataFrame([prediction_proba], columns=le.classes_, index=["Probabilitas"]))


else:
    st.warning("Model belum berhasil dimuat. Silakan periksa file model.")
