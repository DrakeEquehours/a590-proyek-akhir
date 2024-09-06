# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut menyadari bahwa tingginya jumlah siswa yang tidak menyelesaikan pendidikan atau dropout merupakan tantangan serius bagi institusi. Oleh karena itu, mereka memahami pentingnya deteksi dini terhadap siswa yang berpotensi melakukan dropout agar dapat memberikan intervensi dan bimbingan khusus sesuai kebutuhan. Dengan fokus pada pemahaman bisnis ini, Jaya Jaya Institut berusaha mengembangkan strategi dan sistem pendeteksian dini guna meminimalkan angka dropout dan meningkatkan tingkat kelulusan institusi mereka.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi beberapa permasalahan bisnis yang perlu diatasi terkait tingginya tingkat dropout di antara siswanya. Pertama, perlu diidentifikasi faktor-faktor yang menyebabkan siswa cenderung keluar dari institusi, termasuk masalah akademis, keuangan, atau sosial. Selanjutnya, diperlukan pengembangan model prediksi yang dapat memproses data historis siswa dan menghasilkan prediksi akurat terkait risiko dropout. Model ini diharapkan dapat memberikan indikasi sejak dini terhadap siswa yang berpotensi melakukan dropout, memungkinkan institusi untuk memberikan bimbingan dan dukungan yang sesuai guna mencegah keputusan keluar dari pendidikan.

### Cakupan Proyek

Cakupan proyek ini mencakup dua aspek utama: pertama, pembuatan model prediksi untuk menentukan risiko siswa melakukan dropout. Proses ini melibatkan analisis data historis siswa, termasuk data akademis, keuangan, dan sosial, untuk mengidentifikasi pola atau faktor-faktor yang berkorelasi dengan kecenderungan dropout. Model prediksi ini akan memungkinkan institusi untuk melakukan deteksi dini dan memberikan intervensi tepat waktu. Kedua, proyek ini juga melibatkan pengembangan dashboard insight data yang memberikan visualisasi informasi kritis terkait tingkat dropout, tren, dan faktor-faktor kontributor. Dashboard ini akan membantu pihak terkait, seperti staf akademis dan manajemen, untuk memantau kinerja institusi secara keseluruhan dan merancang strategi intervensi yang lebih efektif.

### Persiapan

Sumber data: [students performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import joblib
```

## Business Dashboard

Analisis distribusi skor antara siswa yang lulus (graduated) dan siswa yang dropout di dashboard mengungkapkan pola yang signifikan. Siswa yang lulus cenderung memiliki skor tertinggi di sekitar nilai 13 dan kecenderungan untuk memperoleh skor lebih tinggi. Sebaliknya, siswa yang dropout memiliki skor terbanyak di sekitar nilai 12 dan menunjukkan kecenderungan untuk mendapatkan skor lebih rendah. Perbedaan distribusi ini dapat memberikan wawasan berharga terkait karakteristik akademis yang membedakan kedua kelompok tersebut. Informasi ini dapat menjadi dasar untuk merancang strategi intervensi yang sesuai, seperti memberikan dukungan tambahan kepada siswa dengan skor rendah atau mengidentifikasi faktor penyebab dropout yang berkaitan dengan nilai akademis. 

Dashboard dapat di akses pada link [berikut](https://lookerstudio.google.com/reporting/a2fbdbd2-c034-42b3-97ef-0ce93b52160f)

## Menjalankan Sistem Machine Learning
Untuk menjalankan sistem machine learning menggunakan streamlit secara luring dapat menggunakan code berikut

```
streamlit run app.py
```
Secara daring, sistem dapat diakses menggunakan link [berikut](https://a590-proyek-akhir-ahmad.streamlit.app/)

## Conclusion
Berdasarkan hasil proyek, dapat disimpulkan bahwa terdapat pola yang signifikan dalam distribusi skor antara siswa yang lulus dan siswa yang dropout di Jaya Jaya Institut. Siswa yang lulus cenderung memiliki distribusi skor tertinggi di sekitar nilai 13 dan menunjukkan kecenderungan untuk memperoleh skor lebih tinggi, sementara siswa yang dropout memiliki skor terbanyak di sekitar nilai 12 dan menunjukkan kecenderungan untuk mendapatkan skor lebih rendah. Temuan ini memberikan pemahaman yang lebih baik terkait faktor-faktor akademis yang mempengaruhi keputusan siswa untuk menyelesaikan atau meninggalkan pendidikan. 

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Program Pendampingan Akademis

Implementasikan program pendampingan akademis yang bersifat proaktif untuk siswa dengan skor rendah. Dengan memahami bahwa siswa yang lulus memiliki kecenderungan memiliki skor lebih tinggi, institusi dapat menargetkan siswa dengan skor rendah dan memberikan dukungan tambahan melalui tutor atau mentor akademis. Program ini dapat membantu meningkatkan pemahaman materi pelajaran, memberikan bimbingan dalam tugas-tugas, dan memberikan motivasi kepada siswa untuk meningkatkan kinerja akademis mereka.

- Program Konseling dan Dukungan Psikososial

Sertakan program konseling dan dukungan psikososial sebagai bagian integral dari strategi pencegahan dropout. Siswa mungkin menghadapi tantangan pribadi atau sosial yang dapat memengaruhi kinerja akademis mereka. Dengan menyediakan layanan konseling yang terjangkau dan mudah diakses, institusi dapat membantu siswa mengelola stres, kecemasan, atau masalah pribadi lainnya yang dapat menjadi faktor utama dalam keputusan untuk melakukan dropout. Dukungan psikososial ini dapat membantu menciptakan lingkungan belajar yang lebih seimbang dan mendukung perkembangan siswa secara menyeluruh.

