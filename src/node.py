class Node:
    def __init__(self, name):
        self.name = name
        self.data = "Data_Awal"  # Data default saat node pertama kali menyala

    def update_data(self, new_value):
        self.data = new_value

    def __str__(self):
        return f"Node {self.name}: {self.data}"