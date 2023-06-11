"""
Module that provides translate functions
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate from English to French
    """
    translated = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return translated

def french_to_english(french_text):
    """
    Translate from French to English
    """
    translated = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return translated
