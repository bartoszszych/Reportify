from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QLineEdit,
    QLabel, QVBoxLayout, QGridLayout, QTextEdit,
    QFileDialog
)
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt
import os
from pyqtspinner import WaitingSpinner

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reportify")
        self.set_dimensions()
        self.set_font()
        self.set_palette()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(20)
        self.create_top_widget()
        self.create_bottom_widget()
        self.create_waiting_spinner()

    def set_dimensions(self):
        self.setMinimumSize(600, 800)
        self.setMaximumSize(800, 1000)

    def set_font(self):
        font = QFont()
        font.setPointSize(12)
        self.font = font

    def set_palette(self):
        palette = self.palette()
        palette.setColor(palette.Window, QColor(30, 30, 30))
        palette.setColor(palette.WindowText, Qt.white)
        palette.setColor(palette.Base, QColor(40, 40, 40))
        palette.setColor(palette.AlternateBase, QColor(50, 50, 50))
        palette.setColor(palette.ToolTipBase, Qt.white)
        palette.setColor(palette.ToolTipText, Qt.white)
        palette.setColor(palette.Text, Qt.white)
        palette.setColor(palette.Button, QColor(60, 60, 60))
        palette.setColor(palette.ButtonText, Qt.white)
        palette.setColor(palette.Disabled, palette.Text, Qt.white)
        self.setPalette(palette)

    def create_top_widget(self):
        self.top_widget = QWidget(self.central_widget)
        self.layout.addWidget(self.top_widget)
        self.top_widget_layout = QGridLayout(self.top_widget)
        self.top_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.top_widget_layout.setVerticalSpacing(10)
        self.top_widget_layout.setHorizontalSpacing(20)
        self.create_report_title_input()
        self.create_description_input()
        self.create_keywords_input()
        self.create_audio_file_button()
        self.create_image_file_button()
        self.create_generate_button()
        self.create_image_label()

    def create_report_title_input(self):
        self.report_title_label = QLabel("Title")
        self.report_title_label.setFont(self.font)
        self.report_title_input = QLineEdit()
        self.report_title_input.setPlaceholderText("Enter report title...")
        self.report_title_input.setStyleSheet(
            "QLineEdit { border: 2px solid #6A5ACD; border-radius: 10px; padding: 5px; background-color: #2F4F4F; color: white }"
        )
        self.top_widget_layout.addWidget(self.report_title_label, 0, 0)
        self.top_widget_layout.addWidget(self.report_title_input, 0, 1)

    def create_description_input(self):
        self.description_label = QLabel("Description")
        self.description_label.setFont(self.font)
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Enter description...")
        self.description_input.setStyleSheet(
            "QTextEdit { border: 2px solid #6A5ACD; border-radius: 10px; padding: 5px; background-color: #2F4F4F; color: white }"
        )
        self.top_widget_layout.addWidget(self.description_label, 1, 0)
        self.top_widget_layout.addWidget(self.description_input, 1, 1)

    def create_keywords_input(self):
        self.keywords_label = QLabel("Keywords")
        self.keywords_label.setFont(self.font)
        self.keywords_input = QLineEdit()
        self.keywords_input.setPlaceholderText("Enter keywords, separated by commas...")
        self.keywords_input.setStyleSheet(
            "QLineEdit { border: 2px solid #6A5ACD; border-radius: 10px; padding: 5px; background-color: #2F4F4F; color: white }"
        )
        self.top_widget_layout.addWidget(self.keywords_label, 2, 0)
        self.top_widget_layout.addWidget(self.keywords_input, 2, 1)

    def create_audio_file_button(self):
        self.audio_file_button = QPushButton(f"Audio file")
        self.audio_file_button.setStyleSheet(
            "QPushButton { background-color: #6A5ACD; color: white; border: none; border-radius: 5px; padding: 5px }"
            "QPushButton:hover { background-color: #7B68EE }"
            "QPushButton:pressed { background-color: #483D8B }"
        )
        self.top_widget_layout.addWidget(self.audio_file_button, 3, 0, 1, 2)

    def create_image_file_button(self):
        self.image_file_button = QPushButton("Image file")
        self.image_file_button.setStyleSheet(
            "QPushButton { background-color: #6A5ACD; color: white; border: none; border-radius: 5px; padding: 5px }"
            "QPushButton:hover { background-color: #7B68EE }"
            "QPushButton:pressed { background-color: #483D8B }"
        )
        self.top_widget_layout.addWidget(self.image_file_button, 4, 0, 1, 2)

    def create_generate_button(self):
        self.generate_button = QPushButton("Generate report")
        self.generate_button.setStyleSheet(
            "QPushButton { background-color: #6A5ACD; color: white; border: none; border-radius: 5px; padding: 5px }"
            "QPushButton:hover { background-color: #7B68EE }"
            "QPushButton:pressed { background-color: #483D8B }"
        )
        self.top_widget_layout.addWidget(self.generate_button, 5, 0, 1, 2)

    def create_image_label(self):
        self.image_label = QLabel("Image")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet(
            "QLabel { border: 2px solid #6A5ACD; border-radius: 10px; padding: 5px; background-color: #2F4F4F; color: white }"
        )
        self.image_label.setMinimumSize(200, 200)
        self.top_widget_layout.addWidget(self.image_label, 6, 0, 1, 2)

    def create_bottom_widget(self):
        self.bottom_widget = QWidget(self.central_widget)
        self.layout.addWidget(self.bottom_widget)
        self.bottom_widget_layout = QGridLayout(self.bottom_widget)
        self.bottom_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_widget_layout.setSpacing(20)
        self.create_report_output()

    def create_report_output(self):
        self.report_label = QLabel("Report")
        self.report_label.setFont(self.font)
        self.report_label.setAlignment(Qt.AlignCenter)
        self.report_text_edit = QTextEdit()
        self.report_text_edit.setPlaceholderText("Your generated report will appear here...")
        self.report_text_edit.setStyleSheet(
            "QTextEdit { border: 2px solid #6A5ACD; border-radius: 10px; padding: 5px; background-color: #2F4F4F; color: white }"
        )
        self.bottom_widget_layout.addWidget(self.report_label)
        self.bottom_widget_layout.addWidget(self.report_text_edit)

    def load_image(self, path):
        if path:
            pixmap = QPixmap(path)
            label_size = self.image_label.size()
            pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(False)
            self.image_label.setMinimumSize(pixmap.width(), pixmap.height())
        else:
            return

    def create_waiting_spinner(self):
        self.waiting_spinner = WaitingSpinner(self, color='white', roundness=50, line_width=5, line_length=15, lines=13, radius=15)

    def start_waiting_spinner(self):
        self.waiting_spinner.start()

    def stop_waiting_spinner(self):
        self.waiting_spinner.stop()

    # Get and set methods for text elements
    def get_report(self): 
        return self.report_text_edit.toPlainText()

    def set_report(self, text): 
        self.report_text_edit.setText(text)       

    def get_report_title(self):
        return self.report_title_input.text()

    def set_report_title(self, text):
        self.report_title_input.setText(text)

    def get_description(self):
        return self.description_input.toPlainText()

    def set_description(self, text):
        self.description_input.setText(text)

    def get_keywords(self):
        return self.keywords_input.text()

    def set_keywords(self, text):
        self.keywords_input.setText(text)

    def set_button_name(self, button, path):
        if path:
            name = os.path.basename(path)
            button.setText(name)
        else:
            return
    
    def get_file_path(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select file")
        if file_path:
            return file_path
