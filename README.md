# 💰 CashFlow - Aplikasi Kasir Desktop

## Deskripsi

**CashFlow** merupakan aplikasi kasir desktop berbasis **Python** menggunakan framework **PySide6** dan database **SQLite**. Aplikasi ini dirancang untuk membantu proses pengelolaan data produk, transaksi penjualan, serta pencatatan riwayat transaksi melalui antarmuka grafis (GUI) yang sederhana dan mudah digunakan.

Aplikasi menyediakan fitur Dashboard untuk menampilkan ringkasan informasi toko, Manajemen Produk, Transaksi Kasir, serta Riwayat Transaksi. Seluruh data disimpan secara lokal menggunakan SQLite sehingga aplikasi dapat digunakan tanpa memerlukan koneksi internet maupun server database tambahan.

---

# 👥 Anggota Kelompok

| Nama                | NIM           | Peran                                      |
| ------------------- | ------------- | ------------------------------------------ |
| Sultan Kusuma Jaya  | **(F1D02310139)** | Backend Developer & Database Engineer      |
| Hilya Fitri         | **(F1D02310009)** | Frontend Developer & UI Designer           |
| Muhammad Zia Ul Haq | **(F1D02410125)** | System Integration & Transaction Developer |

---

# ✨ Fitur Utama

* 📊 Dashboard Monitoring
* 📦 Manajemen Produk (CRUD)
* 🔍 Pencarian Produk
* 🛒 Sistem Kasir
* 💰 Perhitungan Total Pembayaran
* 💵 Perhitungan Kembalian Otomatis
* 📉 Pengurangan Stok Otomatis
* 📜 Riwayat Transaksi
* 🗄 Penyimpanan Database SQLite
* 🎨 Tampilan GUI Modern menggunakan PySide6 & QSS

---

# 📂 Struktur Project

```text
CashFlow/
│
├── assets/
│   └── style.qss
│
├── database/
│   ├── db.py
│   └── cashflow.db
│
├── models/
│   ├── product_model.py
│   └── transaction_model.py
│
├── reports/
│
├── ui/
│   ├── dashboard_page.py
│   ├── product_page.py
│   ├── cashier_page.py
│   ├── history_page.py
│   ├── main_window.py
│   └── dialogs/
│       └── product_dialog.py
│
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ▶ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/CashFlow.git
```

### 2. Masuk ke Folder Project

```bash
cd CashFlow
```

### 3. Membuat Virtual Environment

```bash
python -m venv venv
```

### 4. Aktifkan Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install Dependency

```bash
pip install -r requirements.txt
```

### 6. Jalankan Aplikasi

```bash
python main.py
```

---

# 🖼 Screenshot Aplikasi

## Dashboard

> <img width="1600" height="939" alt="image" src="https://github.com/user-attachments/assets/6b9239a7-bd2d-42da-8d9e-b8379789ceab" />


---

## Manajemen Produk

> <img width="1600" height="939" alt="image" src="https://github.com/user-attachments/assets/7ea41d73-40ba-418b-b962-df73dfd790df" />


---

## Dialog Tambah Produk

> <img width="1600" height="939" alt="image" src="https://github.com/user-attachments/assets/1f7b9c41-ad22-4641-b07c-d9b217f7bd90" />


---

## Halaman Kasir

> <img width="1600" height="941" alt="image" src="https://github.com/user-attachments/assets/267b1392-1ca4-4121-8b03-afbb3f19f5fc" />


---

## Riwayat Transaksi

> <img width="1600" height="941" alt="image" src="https://github.com/user-attachments/assets/a30e8242-0a01-4826-a41d-6022f8653984" />


---

# 👨‍💻 Pembagian Tugas

### Sultan Kusuma Jaya

* Mendesain database SQLite
* Membuat koneksi database
* Mengembangkan Product Model
* Mengembangkan Transaction Model
* Implementasi operasi CRUD
* Implementasi query Dashboard

**Berkas yang dikerjakan:**

* `database/db.py`
* `database/cashflow.db`
* `models/product_model.py`
* `models/transaction_model.py`

---

### Hilya Fitri

* Mendesain antarmuka aplikasi
* Membuat Dashboard
* Membuat Main Window
* Mengembangkan Halaman Produk
* Membuat Dialog Produk
* Styling menggunakan Qt Style Sheet (QSS)

**Berkas yang dikerjakan:**

* `assets/style.qss`
* `ui/main_window.py`
* `ui/dashboard_page.py`
* `ui/product_page.py`
* `ui/dialogs/product_dialog.py`

---

### Muhammad Zia Ul Haq

* Mengembangkan halaman Kasir
* Mengembangkan Riwayat Transaksi
* Integrasi antarhalaman
* Validasi transaksi
* Pengujian sistem

**Berkas yang dikerjakan:**

* `ui/cashier_page.py`
* `ui/history_page.py`
* `reports/`
* `utils/`
* `main.py`
* `requirements.txt`

---
