# Reportify - Report Generation App

Reportify is a desktop application built using Python and PyQt5 that allows users to generate professional reports by providing inputs in the form of text, audio recordings, and images. This app uses the OpenAI and Replicate APIs to generate the report content.

## Main Features

- Supports adding a report title, description, keywords, audio recordings, and images
- Generates a report by combining user inputs and additional details
- Uses OpenAI ChatCompletion model for generating text from prompt
- Transcribes speech to text using OpenAI Audio API
- Extracts information about images using Replicate API
- Multi-threaded implementation for better performance

## Folder Structure

- **Reportify**: Main folder
- **Controllers**: Contains the `main_controller.py` file with the application's main controller logic
- **Models**: Contains `report_generator.py` and `report.py` files defining the report generation and report data classes respectively
- **Views**: Contains the `main_view.py` file defining the main application window's GUI
- **API**: Contains the `ai.py` file defining the AI class that interacts with the OpenAI and Replicate APIs
- **Supporting**: Contains the `config.py` file that stores API keys and tokens

## Dependencies

To run the application, you will need to install the following dependencies:

- PyQt5: Used for the application's GUI
- pyqtspinner: Used for displaying a waiting spinner during report generation
- OpenAI: Used for the OpenAI API integration
- Replicate: Used for the Replicate API integration

### Installation

To install the dependencies, you can use pip:

```
pip install -r requirements.txt
```

## Usage

To start the Reportify application, run the `main.py` file located in the Reportify folder. Make sure you have entered your API keys and tokens in the `config.py` file located in the `supporting` folder.

```python
openai_api_key = "ENTER YOUR OPENAI API KEY HERE"
replicate_api_token = "ENTER YOUR REPLICATE API TOKEN HERE"
```

Once the application starts, you can enter the report details such as title, description, and keywords. You can also add an audio recording or an image by clicking on the respective file buttons.

After entering the details, click on the "Generate" button to start the report generation process. A waiting spinner will be displayed during the generation process. Once the report is generated, it will be displayed in the application window.

## Disclaimer

Reportify is a learning project and the usage of OpenAI and Replicate APIs is subject to their respective terms and conditions. Please ensure you have the necessary permissions and comply with the API providers' policies when using this application.

This project aims to showace Python programming skills, including GUI development, API integration, and multi-threaded implementation. 

## Support

For any issues or questions regarding the Reportify application, please feel free to contact me.
