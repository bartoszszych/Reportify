# This file contains Report class which represents the report data

class Report:
    DEFAULT_TITLE = ""
    DEFAULT_DESCRIPTION = ""
    DEFAULT_KEYWORDS = ""
    DEFAULT_AUDIO_TRANSCRIPT = ""
    DEFAULT_IMAGE_DESCRIPTION = ""
    DEFAULT_REPORT = ""
    DEFAULT_AUDIO_FILE_PATH = None
    DEFAULT_IMAGE_FILE_PATH = None

    def __init__(self) -> None:
        self._title: str = Report.DEFAULT_TITLE
        self._description: str = Report.DEFAULT_DESCRIPTION
        self._keywords: str = Report.DEFAULT_KEYWORDS
        self._audio_transcript: str = Report.DEFAULT_AUDIO_TRANSCRIPT
        self._image_description: str = Report.DEFAULT_IMAGE_DESCRIPTION
        self._report: str = Report.DEFAULT_REPORT
        self._audio_file_path: str = Report.DEFAULT_AUDIO_FILE_PATH
        self._image_file_path: str = Report.DEFAULT_IMAGE_FILE_PATH

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        self._title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        self._description = value

    @property
    def keywords(self) -> str:
        return self._keywords

    @keywords.setter
    def keywords(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Keywords must be a string")
        self._keywords = value

    @property
    def audio_transcript(self) -> str:
        return self._audio_transcript

    @audio_transcript.setter
    def audio_transcript(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Audio transcript must be a string")
        self._audio_transcript = value

    @property
    def image_description(self) -> str:
        return self._image_description

    @image_description.setter
    def image_description(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Image transcript must be a string")
        self._image_description = value

    @property
    def report(self) -> str:
        return self._report

    @report.setter
    def report(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Report must be a string")
        self._report = value

    @property
    def audio_file_path(self) -> str:
        return self._audio_file_path
    
    @audio_file_path.setter
    def audio_file_path(self, value: str) -> None:
        self._audio_file_path = value
        
    @property
    def image_file_path(self) -> str:
        return self._image_file_path
    
    @image_file_path.setter
    def image_file_path(self, value: str) -> None:
        self._image_file_path = value