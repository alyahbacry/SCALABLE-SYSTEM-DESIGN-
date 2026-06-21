from src.node import Node

class Cluster:
    def __init__(self):
        # Inisialisasi 3 node: A, B, dan C
        self.nodes = {
            'A': Node('A'),
            'B': Node('B'),
            'C': Node('C')
        }
        # False berarti jaringan normal (semua terhubung)
        # True berarti terjadi partisi (Node C terisolasi)
        self.network_partition = False 

    def create_partition(self):
        """Mensimulasikan Node C terisolasi dari Node A dan B"""
        self.network_partition = True
        print("\n⚠️  JARINGAN RUSAK: Node C terisolasi dari Node A dan B! ⚠️")

    def fix_partition(self):
        """Memulihkan jaringan sehingga semua node terhubung kembali"""
        self.network_partition = False
        print("\n✅ JARINGAN PULIH: Semua node kembali terhubung.")

    def write_CP(self, target_node_name, new_value):
        """Implementasi Mode CP (Consistency + Partition Tolerance)"""
        print(f"\n--- Mencoba menulis '{new_value}' ke Node {target_node_name} (Mode CP) ---")
        
        if self.network_partition:
            # Jika mencoba menulis ke node yang terisolasi (C)
            if target_node_name == 'C':
                print(f"❌ Gagal: Node C terisolasi. Request ditolak demi KONSISTENSI.")
                return False
            else:
                # Jika menulis ke A atau B, mereka mencoba broadcast ke C tapi gagal
                print(f"-> Node {target_node_name} menerima data baru...")
                print(f"-> Mencoba sinkronisasi ke Node C...")
                print(f"❌ Gagal: Node C tidak merespon. Transaksi DIBATALKAN di semua Node demi KONSISTENSI.")
                return False
        else:
            # Jaringan normal, semua node berhasil diperbarui secara konsisten
            for node in self.nodes.values():
                node.update_data(new_value)
            print(f"✅ Sukses: Data '{new_value}' ditulis dan disinkronkan ke seluruh node.")
            return True

    def write_AP(self, target_node_name, new_value):
        """Implementasi Mode AP (Availability + Partition Tolerance)"""
        print(f"\n--- Mencoba menulis '{new_value}' ke Node {target_node_name} (Mode AP) ---")
        
        if self.network_partition:
            if target_node_name in ['A', 'B']:
                # Hanya kelompok A & B yang menerima data baru
                self.nodes['A'].update_data(new_value)
                self.nodes['B'].update_data(new_value)
                print(f"✅ Sukses (Available): Data tertulis di Node A & B. Node C dilewati karena terisolasi.")
            elif target_node_name == 'C':
                # Hanya kelompok C yang menerima data baru
                self.nodes['C'].update_data(new_value)
                print(f"✅ Sukses (Available): Data tertulis di Node C saja. Node A & B tidak terjangkau.")
        else:
            # Jaringan normal, semua node diperbarui
            for node in self.nodes.values():
                node.update_data(new_value)
            print(f"✅ Sukses: Data '{new_value}' disinkronkan ke seluruh node.")

    def cetak_status(self):
        """Menampilkan data saat ini di masing-masing node"""
        print("\n📊 STATUS DATA SAAT INI:")
        for node in self.nodes.values():
            print(f"   {node}")