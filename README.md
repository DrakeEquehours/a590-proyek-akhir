# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut menyadari bahwa nilai akademis siswa, terutama pada semester awal, merupakan indikator penting dalam mendeteksi risiko dropout. Berdasarkan berbagai literatur akademisi nilai menjadi pokok pengaruh dari perilaku dropout siswa [[1]](https://www.tandfonline.com/doi/pdf/10.1080/00220671.1997.10544591), [[2]](https://www.researchgate.net/profile/Azkananda-Widiasani/publication/310773130_Handbook_of_Student_Engagement/links/5836a0dd08aed45931c772b7/Handbook-of-Student-Engagement.pdf#page=502), [[3]](https://onlinelibrary.wiley.com/doi/pdf/10.1002/pits.10046) ditambah dengan eksplorasi data, nilai semester 1 dan 2 memiliki pengaruh signifikan terhadap keputusan siswa untuk melanjutkan pendidikan atau dropout. Oleh karena itu, institusi berupaya untuk memanfaatkan data nilai semester awal sebagai bagian dari strategi deteksi dini guna meminimalkan angka dropout.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tantangan dalam mengidentifikasi siswa yang berpotensi dropout berdasarkan kinerja akademis awal mereka. Dalam hal ini, diperlukan pengembangan model prediksi yang fokus pada data nilai semester 1 dan 2 untuk menghasilkan prediksi akurat terkait risiko dropout. Dengan demikian, institusi dapat memberikan intervensi dini yang tepat untuk mendukung siswa yang membutuhkan.

### Cakupan Proyek

Proyek ini akan fokus pada dua aspek utama:

#### Pengembangan Model Prediksi Dropout Berdasarkan Nilai Akademis
Proses ini akan mengutamakan analisis data nilai semester 1 dan 2 untuk menentukan risiko dropout siswa. Analisis akan difokuskan pada identifikasi pola dan tren yang muncul dari kinerja akademis siswa pada semester awal.
#### Dashboard Insight
Pengembangan dashboard yang menampilkan visualisasi terkait tingkat dropout berdasarkan kinerja akademis pada semester awal. Dashboard ini akan membantu institusi dalam memantau siswa berisiko dan merancang intervensi yang efektif.

### Persiapan
#### Persiapan Data
Untuk mereplikasi proyek ini maka diperlukan data yang sama dan dapat diunduh pada tautan berikut

Sumber data: [students performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
#### Persiapan Lingkungan Pengembangan
Untuk dapat menjalankan notebook yang ada, berbagai library/framework perlu dipasang pada lingkungan pengembangan. Contoh persiapannya dapat menggunakan kode berikut
Setup environment:
```
python -m pip install -r requirements.txt
```

## Business Dashboard

Analisis distribusi skor antara siswa yang lulus (graduated) dan siswa yang dropout di dashboard mengungkapkan pola yang signifikan. Siswa yang lulus cenderung memiliki skor tertinggi di sekitar nilai 13 dan kecenderungan untuk memperoleh skor lebih tinggi. Sebaliknya, siswa yang dropout memiliki skor terbanyak di sekitar nilai 12 dan menunjukkan kecenderungan untuk mendapatkan skor lebih rendah. Perbedaan distribusi ini dapat memberikan wawasan berharga terkait karakteristik akademis yang membedakan kedua kelompok tersebut. Informasi ini dapat menjadi dasar untuk merancang strategi intervensi yang sesuai, seperti memberikan dukungan tambahan kepada siswa dengan skor rendah atau mengidentifikasi faktor penyebab dropout yang berkaitan dengan nilai akademis. 

Dashboard dapat di akses pada link [berikut](https://lookerstudio.google.com/reporting/a2fbdbd2-c034-42b3-97ef-0ce93b52160f)

## Menjalankan Sistem Machine Learning
Untuk menjalankan sistem machine learning menggunakan streamlit secara luring dapat menggunakan code berikut

```
streamlit run app.py
```
Secara daring, sistem dapat diakses menggunakan link [berikut](https://drakeequehours-a590-proyek-akhir-app-ost14q.streamlit.app/)

## Conclusion
Dari visualisasi data yang disajikan, terlihat bahwa terdapat tren yang signifikan terkait nilai akademis siswa dan kecenderungan mereka untuk dropout di Jaya Jaya Institut. Pada semester pertama, siswa yang dropout mayoritas memiliki nilai rendah, sementara pada semester kedua, distribusi nilai siswa yang dropout lebih beragam namun masih menunjukkan angka yang cukup tinggi pada rentang nilai lebih rendah. Ini menunjukkan bahwa kinerja awal yang buruk bisa menjadi indikator kuat risiko dropout. Data ini juga menyoroti pentingnya intervensi awal untuk mendukung siswa yang berjuang secara akademis, melalui pendekatan seperti pendampingan akademis yang lebih intensif dan program mentoring. Institusi perlu mempertimbangkan implementasi strategi-strategi yang bertujuan memperkuat dukungan akademis dan emosional bagi siswa, sehingga dapat meningkatkan tingkat kelulusan dan mengurangi angka dropout. Implementasi kebijakan ini juga harus diikuti dengan pemantauan dan evaluasi yang berkelanjutan untuk menilai efektivitas dari intervensi yang diberikan dan melakukan penyesuaian jika diperlukan.

### Rekomendasi Action Items
Beberapa rekomendasi action items yang dapat dilakukan Jaya Jaya Institut guna menyelesaikan permasalahan dropout siswa adalah sebagai berikut.

- Pendampingan Akademis yang Lebih Intensif

Untuk mengatasi masalah tingginya angka dropout yang sering dikaitkan dengan prestasi akademis rendah, Jaya Jaya Institut dapat mengimplementasikan program pendampingan akademis yang lebih intensif. Program ini harus dirancang untuk memberikan dukungan ekstra kepada siswa yang mengalami kesulitan dalam pelajaran tertentu. Melalui pendekatan ini, siswa dapat menerima bimbingan secara individu atau dalam kelompok kecil yang memungkinkan perhatian lebih terfokus pada kebutuhan spesifik mereka. Selain sesi tutorial reguler, program ini bisa mencakup sesi belajar tambahan, workshop pemecahan masalah, dan sesi ulasan materi sebelum ujian. Fokus utamanya adalah membantu siswa membangun kepercayaan diri dalam kemampuan akademis mereka dan mengembangkan strategi belajar yang efektif untuk memperbaiki dan mempertahankan performa akademis mereka.

- Program Mentoring

Program mentoring bisa menjadi strategi efektif lain untuk mengurangi tingkat dropout dengan memberikan dukungan emosional dan akademik. Program ini harus melibatkan senior atau alumni yang telah menunjukkan keberhasilan dalam studi mereka untuk bertindak sebagai mentor bagi siswa yang berisiko. Mentor dapat memberikan panduan, motivasi, dan saran praktis berdasarkan pengalaman mereka sendiri, membantu mentee mereka mengatasi hambatan dalam studi serta memandu mereka dalam mengembangkan keterampilan pengelolaan waktu dan studi yang lebih baik. Kegiatan mentoring bisa dilakukan melalui pertemuan rutin, baik secara tatap muka maupun virtual, memastikan bahwa siswa mendapatkan bimbingan kontinu yang mereka butuhkan untuk sukses. Dengan demikian, mentor tidak hanya berperan sebagai pembimbing akademis, tapi juga sebagai role model dan pendukung moral yang dapat mempengaruhi positif keseluruhan pengalaman belajar siswa.

