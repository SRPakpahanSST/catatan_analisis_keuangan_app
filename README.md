# 📒 Aplikasi Catatan & Analisis Keuangan Interaktif (AI-Powered)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-black)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18.x-61DAFB)](https://reactjs.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-orange)](https://ai.google.dev/)

> **Kompetisi:** APINDO AI Challenge 2026  
> **Tema:** "Teman Cerdas, Solusi Tuntas"  
> **Kategori:** Smart Analyst & Productivity Booster  
> **Target:** Pelaku UMKM

Aplikasi ini adalah solusi inovatif berbasis **Artificial Intelligence** untuk membantu UMKM mengelola keuangan dengan mudah. Cukup ketik seperti mengobrol, AI akan mencatat transaksi, menyajikan dashboard analitik, memprediksi arus kas, dan memberi rekomendasi penghematan.

Alamat URL link aplikasi: https://catatan-analisis-keuangan-app-5j81.vercel.app/

---

## ✨ Fitur Unggulan

- **📝 Pencatatan Cerdas (AI Chat Input)**  
  Ketik "jualan 500rb, beli bahan 200rb" → AI langsung mencatat & mengkategorikan.

- **📊 Dashboard Interaktif**  
  Visualisasi saldo, pemasukan, pengeluaran, dan breakdown kategori biaya.

- **🔮 Prediksi Arus Kas**  
  Prediksi pengeluaran 7 hari ke depan dengan metode Regresi Linear.

- **🤖 Rekomendasi AI**  
  Saran praktis efisiensi biaya berdasarkan riwayat transaksi.

- **⚡️ Manajemen Data**  
  Tambah, cari, dan hapus catatan keuangan dengan mudah.

---

## 🛠️ Teknologi

| Komponen | Teknologi |
|----------|-----------|
| Backend | Python, Flask, Flask-CORS |
| Frontend | React.js, Vite, Bootstrap |
| Database | JSON Lokal (ringan) |
| AI | Google Gemini API, NumPy |

---

## 📁 Struktur Proyek

catatan_analisis_keuangan_app/
├── main.py                     # Server Flask utama
├── chatbot-app.py              # Integrasi AI Gemini
├── requirements.txt            # Dependensi Python
├── .env                        # API Key (jangan di-commit)
├── .gitignore                  # File yang diabaikan Git
├── README.md                   # Dokumentasi
├── data.json                   # Database transaksi (auto-generated)
│
├── keuangan/                   # Backend
│   ├── init.py
│   ├── keuangan_real.py        # CRUD transaksi
│   └── dahboard_keuangan_real.py # Analisis & prediksi
│
└── catatan/                    # Frontend React
├── src/
│   ├── components/         # Komponen React
│   ├── utils/api.js        # Koneksi ke backend
│   └── styles/             # CSS
├── public/
├── package.json
└── vite.config.js

```

---

## 🚀 Instalasi & Menjalankan Aplikasi

### 1. Prasyarat
- Python 3.9+
- Node.js 18+
- API Key dari [Google AI Studio](https://aistudio.google.com/)

### 2. Setup Backend
```bash
# Buat virtual environment (opsional)
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Install dependensi
pip install -r requirements.txt

# Buat file .env dan isi API Key
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

3. Setup Frontend

```bash
cd catatan
npm install
npm run build
cd ..
```

4. Jalankan Aplikasi

```bash
python main.py
```

Buka browser di http://localhost:5000

---

📡 API Endpoint

Endpoint Method Deskripsi
/api/transactions GET Ambil semua transaksi
/api/transactions POST Tambah transaksi (manual atau via AI)
/api/transactions/<id> DELETE Hapus transaksi
/api/dashboard GET Ringkasan, kategori, prediksi
/api/rekomendasi GET Saran penghematan dari AI

---