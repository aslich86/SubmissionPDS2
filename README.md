# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi fiktif yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi yang baik dan telah menghasilkan banyak lulusan berkualitas, institusi ini menghadapi tantangan signifikan terkait tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya atau *dropout*. Tingginya angka *dropout* tidak hanya berdampak pada reputasi institusi, tetapi juga pada stabilitas finansial dan efisiensi operasional. Oleh karena itu, pihak manajemen ingin menerapkan solusi berbasis data untuk mengatasi masalah ini.

### Permasalahan Bisnis
Berdasarkan latar belakang tersebut, permasalahan utama yang dihadapi oleh Jaya Jaya Institut adalah:
1.  **Tingkat *dropout* mahasiswa yang tinggi**, yang dapat merusak citra dan keberlanjutan institusi.
2.  **Kesulitan dalam mengidentifikasi mahasiswa yang berisiko *dropout* secara dini**, sehingga intervensi yang diberikan seringkali terlambat.
3.  **Belum adanya sistem pemantauan performa mahasiswa yang terpusat dan mudah diakses** oleh pihak manajemen atau pembimbing akademik untuk pengambilan keputusan yang proaktif.

### Cakupan Proyek
Proyek data science ini bertujuan untuk membangun sistem yang dapat membantu Jaya Jaya Institut dalam memprediksi dan memonitor mahasiswa yang berpotensi *dropout*. Cakupan proyek ini meliputi:
- **Analisis Data Eksploratif (EDA)** untuk menemukan pola dan faktor-faktor yang mempengaruhi status kelulusan mahasiswa.
- **Pengembangan model machine learning** klasifikasi yang mampu memprediksi status akhir mahasiswa (Lulus atau Dropout) dengan tingkat akurasi yang baik.
- **Pembuatan business dashboard interaktif** menggunakan Looker Studio untuk memvisualisasikan data dan memonitor performa mahasiswa secara keseluruhan.
- **Pembuatan prototipe sistem machine learning** dalam bentuk aplikasi web menggunakan Streamlit yang dapat digunakan oleh staf untuk melakukan prediksi secara individual.

### Persiapan

**Sumber data:**
Dataset yang digunakan dalam proyek ini adalah "Predict students' dropout and academic success" yang bersumber dari UCI Machine Learning Repository dan dapat diakses melalui link berikut:
[https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

**Setup environment:**
Lingkungan kerja untuk proyek ini dapat diatur dengan mengikuti langkah-langkah berikut. Pastikan Anda memiliki Python 3.10+ ter-install.

```
# 1. Clone repositori (jika diperlukan)
git clone [(https://github.com/aslich86/SubmissionPDS2.git)]


# 2. Buat virtual environment
python3 -m venv venv

# 3. Aktifkan virtual environment
# Untuk macOS/Linux:
source venv/bin/activate
# Untuk Windows:
venv\Scripts\activate

# 4. Install semua library yang dibutuhkan
pip install -r requirements.txt
```

## Business Dashboard
Sebuah dashboard interaktif telah dikembangkan menggunakan Looker Studio untuk membantu pihak manajemen Jaya Jaya Institut dalam memantau tren dan metrik kunci terkait performa mahasiswa. Dashboard ini menyajikan data secara visual sehingga lebih mudah dipahami.

Beberapa informasi utama yang ditampilkan pada dashboard:

Metrik Kunci: Total mahasiswa, tingkat dropout keseluruhan.
Visualisasi Komparatif: Perbandingan jumlah mahasiswa dropout vs. lulus berdasarkan jurusan, jenis kelamin, dan status beasiswa.
Filter Interaktif: Pengguna dapat memfilter data berdasarkan jurusan, jenis kelamin, dan status beasiswa untuk analisis yang lebih mendalam.
Dashboard ini dapat diakses secara publik melalui link berikut:

Link Dashboard: [(https://lookerstudio.google.com/reporting/0bc31fc7-8ee3-49cd-a0fa-391635508cae)]

## Menjalankan Sistem Machine Learning
Sebuah prototipe sistem machine learning telah dikembangkan dalam bentuk aplikasi web interaktif menggunakan Streamlit. Aplikasi ini memungkinkan pengguna (staf atau pembimbing akademik) untuk memasukkan data seorang mahasiswa dan mendapatkan prediksi real-time mengenai status kelulusan mereka.

Aplikasi ini dapat diakses secara online melalui link berikut:

Link Aplikasi Prediksi: [(https://submissionpds2git-afxspsmyrw2iwfvwb2pj7b.streamlit.app/)]

Untuk menjalankan aplikasi ini secara lokal di komputer Anda, ikuti langkah-langkah pada bagian Setup environment di atas, lalu jalankan perintah berikut di terminal:

```
# Pastikan virtual environment sudah aktif
streamlit run app.py
```
## Conclusion

Proyek ini berhasil mengembangkan solusi data-driven untuk mengatasi permasalahan dropout di Jaya Jaya Institut. Model machine learning yang dibangun menggunakan algoritma RandomForestClassifier mampu memprediksi status kelulusan mahasiswa dengan akurasi sekitar 91.46% pada data uji. Analisis menunjukkan bahwa faktor-faktor akademik, seperti jumlah SKS yang diambil dan lulus serta nilai rata-rata pada semester pertama dan kedua, merupakan prediktor kuat terhadap status akhir mahasiswa.

Dengan adanya dashboard dan aplikasi prediksi, institusi kini memiliki perangkat yang kuat untuk:

Memantau kondisi performa mahasiswa secara makro.
Mengidentifikasi mahasiswa yang berisiko dropout secara dini dan individual.
Mengambil keputusan yang lebih tepat sasaran dalam memberikan bimbingan dan dukungan.

## Rekomendasi Action Items
Berdasarkan hasil analisis dan model yang telah dikembangkan, berikut adalah beberapa rekomendasi tindakan yang dapat diambil oleh Jaya Jaya Institut:

- Implementasi Sistem Peringatan Dini (Early Warning System). Gunakan aplikasi prediksi Streamlit pada akhir setiap semester (terutama semester pertama) untuk menyaring mahasiswa yang teridentifikasi berisiko tinggi dropout. Mahasiswa yang masuk dalam kategori ini harus segera dihubungi oleh pembimbing akademik untuk sesi konseling khusus.

- Alokasi Sumber Daya Bimbingan Berdasarkan Data Dashboard. Fokuskan sumber daya bimbingan, lokakarya tambahan, atau program mentorship pada jurusan-jurusan yang, berdasarkan data di dashboard, secara konsisten menunjukkan tingkat dropout tertinggi.

- Program Pemantauan Berkelanjutan untuk Penerima Beasiswa. Meskipun beasiswa bertujuan membantu, dashboard menunjukkan bahwa status beasiswa tidak menjamin kelulusan, sehingga perlu ada pemantauan tambahan bagi penerima beasiswa yang performa akademiknya mulai menurun untuk memastikan bantuan yang diberikan benar-benar efektif.

- Iterasi dan Peningkatan Model Secara Berkala. Model yang ada saat ini adalah fondasi yang kuat. Institusi disarankan untuk terus mengumpulkan data mahasiswa setiap tahunnya dan melatih ulang (retrain) model secara berkala (misalnya, setiap 1-2 tahun) untuk meningkatkan akurasi dan adaptasinya terhadap perubahan pola perilaku mahasiswa.
