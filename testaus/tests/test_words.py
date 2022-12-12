import unittest
import words.words as words


def test_words(self):
    lause = "Tämä on testilause"
    expected_result = "Tämä ON esualitseT."
    result = words.reverse_words(lause)
    self.assertEqual(result, expected_result)

def test_words2(self):
    lause = "Tämä on testilause!"
    expected_result = "Tämä ON esualitseT!"
    result = words.reverse_words(lause)
    self.assertEqual(result, expected_result)

def test_words3(self):
    lause = "Tämä on testilause?"
    expected_result = "Tämä ON esualitseT?"
    result = words.reverse_words(lause)
    self.assertEqual(result, expected_result)

def test_words4(self):
    lause = "Tämä on testilause."
    expected_result = "Tämä ON esualitseT."
    result = words.reverse_words(lause)
    self.assertEqual(result, expected_result)

def test_words5(self):
    lause = "tämä on testilause."
    expected_result = "Tämä ON esualitseT."
    result = words.reverse_words(lause)
    self.assertEqual(result, expected_result)