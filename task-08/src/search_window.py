
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
import os
import requests
from inventory import pokeInventory

class PokemonInfoDialog(QDialog):
    def __init__(self, name, types, image_url):
        super().__init__()

        self.setWindowTitle("Pokemon Information")
        self.setGeometry(100, 100, 600, 400)
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout()

        info_label = QLabel(f"Name: {name}\nTypes: {', '.join(types)}")
        image_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info_label)
        layout.addWidget(image_label)
        self.setLayout(layout)

    def capture_pokemon(self):
        # Implementation of capturing and saving the image
        pass

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = None
        self.image_url = None  # Initialize image_url as None

    def initUI(self):
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search_pokemon)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)  # Connect the button click to the capture function

        inventory_button = QPushButton("Inventory", self)
        inventory_button.setGeometry(50, 400, 160, 43)
        inventory_button.clicked.connect(self.inventory_pokemon)

                
    def search_pokemon(self):
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        pokemon_name = self.textbox.text().strip()
        response = requests.get(f"{base_url}{pokemon_name.lower()}")

        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data["name"]
            types = [type_data["type"]["name"] for type_data in pokemon_data["types"]]
            image_url = pokemon_data["sprites"]["front_default"]

            # Set the image URL in the SearchWindow instance
            self.image_url = image_url

            # Create and show the Pokemon information dialog
            pokemon_info_dialog = PokemonInfoDialog(name, types, image_url)
            pokemon_info_dialog.exec_()
        else:
            QMessageBox.warning(self, "Error", "Pokemon not found or API request failed.")

    def capture_pokemon(self):
        if self.image_url:
            image_data = requests.get(self.image_url).content
            folder_path = "pokemon_list"  # Change to your actual folder path

            # Create the directory if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            captured_pokemon_name = f"captured_pokemon_{len(os.listdir(folder_path)) + 1}.jpg"
            save_path = os.path.join(folder_path, captured_pokemon_name)


            with open(save_path, "wb") as image_file:
                image_file.write(image_data)

            QMessageBox.information(self, "Capture", "Pokemon captured!")
        else:
            QMessageBox.warning(self, "Error", "Pokemon not found or API request failed.")
            
    def inventory_pokemon(self):
        if self.w is None:
            # Create an instance of the pokeInventory class and show it
            self.w = pokeInventory(image_folder="pokemon_list")
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())