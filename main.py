from PyQt5.QtWidgets import QApplication
from Views.main_view import MainView
from Models.report import Report
from Controllers.main_controller import MainController
from API.ai import AI
import Supporting.config as config

if __name__ == "__main__":
    app = QApplication([])
    
    openai_api_key = config.openai_api_key
    replicate_api_token = config.replicate_api_token

    view = MainView()
    report_data = Report()
    ai = AI(openai_api_key,replicate_api_token)
    
    controller = MainController(report_data, view, ai)
    
    view.show()
    app.exec_()

