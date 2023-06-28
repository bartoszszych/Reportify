# This file contains Controller class which manages application logic
from PyQt5.QtCore import QThread
from Models.report_generator import ReportGenerator

class MainController():
    def __init__(self, report, view, ai):
        self.report = report
        self.view = view
        self.ai = ai
        
        self.thread = None
        self.report_generator = None
        self.is_request_in_progress = False

        self.view.generate_button.clicked.connect(self.generate_report)
        self.view.report_title_input.textChanged.connect(self.report_title_changed)
        self.view.description_input.textChanged.connect(self.description_changed)
        self.view.keywords_input.textChanged.connect(self.keywords_changed)
        self.view.audio_file_button.clicked.connect(self.audio_file_path_changed)
        self.view.image_file_button.clicked.connect(self.image_file_path_changed)

    def generate_report(self):
        if self.is_request_in_progress:
            return
        
        self.is_request_in_progress = True
        self.view.start_waiting_spinner()

        self.report_generator = ReportGenerator(self.ai, self.report)

        
        self.thread = QThread()
        self.report_generator.moveToThread(self.thread)
        self.thread.started.connect(self.report_generator.run)
        self.report_generator.report_generated.connect(self.update_report)
        self.report_generator.report_generated.connect(self.view.stop_waiting_spinner)
        self.report_generator.report_generated.connect(self.cleanup_thread)
        self.thread.start()

    def update_report(self, report):
        self.report.report = report
        self.view.set_report(report)

    def report_title_changed(self):
        self.report.title = self.view.get_report_title()

    def description_changed(self):
        self.report.description = self.view.get_description()

    def keywords_changed(self):
        self.report.keywords = self.view.get_keywords()

    def audio_file_path_changed(self):
        self.report.audio_file_path =  self.view.get_file_path()
        self.view.set_button_name(self.view.audio_file_button, self.report.audio_file_path)

    def image_file_path_changed(self):
        self.report.image_file_path = self.view.get_file_path()
        self.view.set_button_name(self.view.image_file_button, self.report.image_file_path)
        self.view.load_image(self.report.image_file_path)

    def cleanup_thread(self):
        if self.thread is not None:
            self.thread.quit()
            self.thread.wait()
            self.thread.deleteLater()
            self.thread = None
            self.report_generator = None
            self.is_request_in_progress = False
    
