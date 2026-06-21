from src.simulation import jalankan_skenario_cp, jalankan_skenario_ap

def main():
    print("=== SIMULASI SEDERHANA TEOREMA CAP ===")
    
    # Menjalankan simulasi Consistency (CP)
    jalankan_skenario_cp()
    
    print("\n\n" + "="*55 + "\n\n")
    
    # Menjalankan simulasi Availability (AP)
    jalankan_skenario_ap()

if __name__ == "__main__":
    main()