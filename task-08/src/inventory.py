import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
import requests
import pokemon_list

    
class pokeInventory(QMainWindow):
    def __init__(self, image_folder):
        super().__init__()
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpeg", ".jpg","png"))]
        self.current_index = 0
        self.setFixedSize(850, 500)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.show_previous_image)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.show_next_image)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.image_label)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
        self.load_image(self.current_index)
        self.update_image_list()

    def update_image_list(self):
        self.image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith((".jpeg", ".jpg", "png"))]
    
    def load_image(self, index):
        if 0 <= index < len(self.image_files):
            image_path = os.path.join(self.image_folder, self.image_files[index])
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_image(self.current_index)

    def show_next_image(self):
        if self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.load_image(self.current_index)        


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = pokeInventory()
    window.show()
    sys.exit(app.exec())
