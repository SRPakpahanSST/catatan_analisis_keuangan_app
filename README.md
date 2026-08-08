# catatan_analisis_keuangan_app
Aplikasi ini menjawab tantangan UMKM dalam pengelolaan keuangan dengan menghadirkan solusi AI yang aplikatif, berdampak, dan solutif— sesuai dengan semangat kompetisi "Teman Cerdas, Solusi Tuntas".

File README.md ini mencakup semua informasi mulai dari deskripsi, struktur proyek, cara instalasi, hingga bagaimana karya ini memenuhi kriteria lomba APINDO AI Challenge 2026.

```markdown
# 📒 Aplikasi Catatan & Analisis Keuangan Interaktif (AI-Powered)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-black)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18.x-61DAFB)](https://reactjs.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-orange)](https://ai.google.dev/)

> **Tema Kompetisi:** "Teman Cerdas, Solusi Tuntas"  
> **Kategori:** Smart Analyst & Productivity Booster  
> **Target Pengguna:** Pelaku UMKM

Aplikasi ini adalah solusi inovatif berbasis **Artificial Intelligence** yang dirancang untuk membantu UMKM mengelola keuangan dengan mudah. Cukup dengan mengetik seperti sedang mengobrol (Natural Language Input), AI akan mencatat transaksi, menyajikan dashboard analitik, memprediksi arus kas, dan memberikan rekomendasi penghematan secara otomatis.

---

## ✨ Fitur Unggulan

- **📝 Pencatatan Cerdas (AI Chat Input)**
  - Cukup ketik "Hari ini jualan 500rb, beli bahan 200rb", AI akan otomatis memproses dan mengkategorikannya.
- **📊 Dashboard Interaktif**
  - Visualisasi saldo, total pemasukan, pengeluaran, dan breakdown kategori biaya secara real-time.
- **🔮 Prediksi Arus Kas (Regresi Linear)**
  - Prediksi pengeluaran 7 hari ke depan untuk membantu antisipasi modal kerja.
- **🤖 Rekomendasi AI**
  - Mendapatkan saran praktis untuk efisiensi biaya berdasarkan riwayat transaksi.
- **⚡️ Manajemen Data**
  - Tambah, cari, dan hapus catatan keuangan dengan antarmuka yang intuitif.

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi |
| :--- | :--- |
| **Backend API** | Python, Flask, Flask-CORS |
| **Frontend** | React.js, Vite, Bootstrap (CSS) |
| **Database** | JSON Lokal (Ringan & Portable) |
| **Kecerdasan Buatan** | Google Gemini API (NLP & Rekomendasi), NumPy (Prediksi) |

---

## 📁 Struktur Proyek

```

catatan_analisis_keuangan_app/
├── main.py                          # Server Flask utama & routing API
├── chatbot-app.py                   # Integrasi AI (Gemini)
├── requirements.txt                 # Dependensi Python
├── .env                             # API Key environment
├── data.json                        # Database transaksi (auto-generated)
│
├── keuangan/                        # Modul Backend
│   ├── init.py
│   ├── keuangan_real.py             # CRUD Transaksi
│   └── dahboard_keuangan_real.py    # Logika Analisis & Prediksi
│
└── catatan_pribadi/                 # Modul Frontend (React + Vite)
├── init.py
├── loader.py
├── main.py
├── index.html
├── vite.config.js
├── package.json
├── package-lock.json
├── netlify.toml
├── eslint.config.js
├── public/
│   ├── _redirects
│   └── vite.svg
└── src/
├── index.jsx
├── utils/
│   ├── index.js
│   ├── noteHelpers.js
│   ├── noteHelpers.jsx
│   └── api.js                 # Koneksi ke Backend Flask
├── styles/
│   ├── style.css
│   └── custom.css
└── components/
├── App.jsx
├── NoteInput.jsx
├── NoteItem.jsx
├── NoteSearch.jsx
├── NotesList.jsx
└── Dashboard.jsx          # Grafik & Analisis

```

---

## 🚀 Panduan Instalasi & Menjalankan Aplikasi

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di komputer lokal (Localhost).

### 1. Prasyarat
Pastikan Anda telah menginstal:
- **Python** (versi 3.9 atau lebih baru) - [Download](https://www.python.org/downloads/)
- **Node.js** (versi 18.x atau lebih baru) - [Download](https://nodejs.org/)
- **API Key** dari Google AI Studio - [Dapatkan di sini](https://aistudio.google.com/)

### 2. Clone / Siapkan Folder Proyek
Buka terminal dan masuk ke direktori proyek.

### 3. Setup Backend (Python & Flask)
1. Buat dan aktifkan *virtual environment* (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Mac/Linux
   venv\Scripts\activate     # Untuk Windows
```

2. Instal semua dependensi Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Buat file .env di root folder dan isi dengan API Key Gemini Anda:
   ```env
   GEMINI_API_KEY=masukkan_api_key_anda_disini
   ```

4. Setup Frontend (React & Vite)

1. Masuk ke direktori frontend:
   ```bash
   cd catatan_pribadi
   ```
2. Instal dependensi Node.js:
   ```bash
   npm install
   ```
3. Build proyek React menjadi file statis (agar bisa disajikan oleh Flask):
   ```bash
   npm run build
   ```
4. Kembali ke root folder:
   ```bash
   cd ..
   ```

5. Menjalankan Aplikasi

1. Jalankan server Flask dari root folder:
   ```bash
   python main.py
   ```
2. Buka browser dan akses alamat:
   ```
   http://localhost:5000
   ```

Catatan: Jika port 5000 sedang digunakan, ubah nilai PORT di main.py atau hentikan proses lain yang menggunakan port tersebut.

---

📡 Dokumentasi API (Backend)

Endpoint Method Deskripsi
/api/transactions GET Mendapatkan semua data transaksi
/api/transactions POST Menambah transaksi (manual atau via teks AI)
/api/transactions/<id> DELETE Menghapus transaksi berdasarkan ID
/api/dashboard GET Mendapatkan ringkasan, kategori, dan prediksi
/api/rekomendasi GET Mendapatkan saran penghematan dari AI

---

📝 Cara Mengirimkan Karya (Untuk Lomba)

Untuk memenuhi syarat kompetisi APINDO AI Challenge 2026, pastikan:

1. Link Web / Dokumentasi: Deploy aplikasi ini ke platform seperti Vercel, Netlify, atau Render, atau unggah dokumentasi berupa PDF yang menjelaskan alur aplikasi.
2. Video Demo: Rekam video berdurasi maksimal 7 menit (format MP4) yang menunjukkan:
   · Proses input transaksi menggunakan teks natural.
   · Tampilan Dashboard dan grafik.
   · Fitur prediksi dan rekomendasi AI.
3. Karya: Unggah tautan (link) aplikasi atau video demo melalui formulir resmi APINDO.

---

🤝 Kontribusi

Proyek ini dikembangkan sebagai bagian dari upaya inovasi untuk mendorong digitalisasi dan adopsi AI di kalangan UMKM Indonesia.

Jika Anda ingin berkontribusi, silakan lakukan fork dan ajukan pull request.

---

📧 Kontak & Informasi Lebih Lanjut

· Kompetisi APINDO: bit.ly/RegAIChallenge2026
· Modul AI Fluency: bit.ly/modulbelajarAI
· Social Media: @candranayalestari, @apindoumkm, @apindo.nasional

---

Selamat berinovasi dan semoga menjadi juara! 🏆

```
