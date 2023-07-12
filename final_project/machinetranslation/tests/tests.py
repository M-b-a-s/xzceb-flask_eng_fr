import unittest
from translator import english_to_french, french_to_english

def test_english_to_french():
    english_text = "Hello"
    expected_french_text = "Bonjour"
    assert english_to_french(english_text) == expected_french_text

    english_text = "How are you?"
    expected_french_text = "Comment ça va ?"
    assert english_to_french(english_text) == expected_french_text

    english_text = "I love cats"
    expected_french_text = "J'adore les chats"
    assert english_to_french(english_text) == expected_french_text

def test_french_to_english():
    french_text = "Bonjour"
    expected_english_text = "Hello"
    assert french_to_english(french_text) == expected_english_text

    french_text = "Comment ça va ?"
    expected_english_text = "How are you?"
    assert french_to_english(french_text) == expected_english_text

    french_text = "J'adore les chats"
    expected_english_text = "I love cats"
    assert french_to_english(french_text) == expected_english_text


unittest.main()