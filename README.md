# Simulasi Sederhana Teorema CAP (Sistem Terdistribusi)

Aplikasi berbasis CLI Python ini mendemonstrasikan bagaimana sebuah Kluster Sistem Terdistribusi berperilaku ketika mengalami **Network Partition (P)**, dan bagaimana ia harus memilih antara **Consistency (CP)** atau **Availability (AP)**.

## Struktur Project
* `src/node.py` - Representasi server/node.
* `src/cluster.py` - Aturan kluster dan simulasi jaringan terputus.
* `src/simulation.py` - Alur jalannya skenario simulasi CP dan AP.
* `main.py` - File utama untuk menjalankan simulasi.

## Cara Menjalankan
Pastikan Anda sudah menginstal Python di komputer Anda. Buka terminal/command prompt di direktori project ini, lalu ketik:

```bash
python main.py