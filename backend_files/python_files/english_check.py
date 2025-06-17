from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

#functia care verifica daca textul este in engleza
def check_english(text):
  if len(text.strip()) < 20:
    raise ValueError("Text is too short to reliably detect the language")
  try:
      language = detect(text)
      if language != 'en':
          raise ValueError("The language of the input text is not english.")
      return True
  except LangDetectException:
      raise ValueError("Text is undetectable or unclear.")