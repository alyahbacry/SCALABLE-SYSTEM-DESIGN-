from src.cluster import Cluster

def jalankan_skenario_cp():
    print("\n=======================================================")
    print("      SKENARIO 1: MODE CP (CONSISTENCY SELECTED)       ")
    print("=======================================================")
    
    kluster = Cluster()
    kluster.cetak_status()
    
    # 1. Tulis data saat kondisi normal
    kluster.write_CP('A', 'Data_Versi_2')
    kluster.cetak_status()
    
    # 2. Terjadi partisi jaringan
    kluster.create_partition()
    
    # 3. Tulis data baru saat terjadi partisi
    kluster.write_CP('A', 'Data_Versi_3')
    
    # 4. Cek status (Data harus tetap Versi 2 karena request ditolak)
    kluster.cetak_status()
    print("\n💡 Penjelasan CP: Sistem menolak data baru agar tidak terjadi perbedaan data antar server.")

def jalankan_skenario_ap():
    print("\n=======================================================")
    print("      SKENARIO 2: MODE AP (AVAILABILITY SELECTED)      ")
    print("=======================================================")
    
    kluster = Cluster()
    kluster.cetak_status()
    
    # 1. Terjadi partisi jaringan
    kluster.create_partition()
    
    # 2. Tulis data ke Node A (A & B terupdate)
    kluster.write_AP('A', 'Data_Baru_A_B')
    
    # 3. Tulis data ke Node C (Hanya C terupdate)
    kluster.write_AP('C', 'Data_Spesial_C')
    
    # 4. Cek status (Data akan berbeda/inkonsisten, tetapi semua request berhasil)
    kluster.cetak_status()
    print("\n💡 Penjelasan AP: Sistem selalu menerima kiriman data (Available), namun dampaknya data antar server menjadi berbeda (Tidak Konsisten).")