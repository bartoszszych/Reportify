from PyQt5.QtCore import QObject, pyqtSignal, QCoreApplication

class ReportGenerator(QObject):
    report_generated = pyqtSignal(str)

    def __init__(self, ai, report):
        super().__init__()
        self.ai = ai
        self.report = report

    def run(self):
        if self.report.audio_file_path != None:
            self.report.audio_transcript = self.ai.transcribe_speech_to_text(self.report.audio_file_path)

        if self.report.image_file_path != None:
            self.report.image_description = self.ai.image_to_text(self.report.image_file_path)

        prompt = "Generate a professional report titled: {},  described: {},"\
        "with keywords: {}. Audio transcript: {}. Image description: {}".format(self.report.title, 
        self.report.description, self.report.keywords, self.report.audio_transcript, self.report.image_description)

        report_text = self.ai.generate_text_from_prompt(prompt)
        
        return self.report_generated.emit(report_text)
