import unittest
from string_utils import StringUtils


class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_capitalize(self):
        # Позитивные тесты
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitalize("тест"), "Тест")

        # Негативные тесты
        self.assertEqual(self.utils.capitalize(""), "")
        self.assertEqual(self.utils.capitalize(" "), " ")
        self.assertEqual(self.utils.capitalize(None), None)

    def test_trim(self):
        # Позитивные тесты
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("   тест   "), "тест   ")

        # Негативные тесты
        self.assertEqual(self.utils.trim(""), "")
        self.assertEqual(self.utils.trim(" "), " ")
        self.assertEqual(self.utils.trim(None), None)

    def test_contains(self):
        # Позитивные тесты
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertTrue(self.utils.contains("Тест", "т"))

        # Негативные тесты
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertFalse(self.utils.contains("", "S"))
        self.assertFalse(self.utils.contains(" ", "S"))
        self.assertFalse(self.utils.contains(None, "S"))

    def test_delete_symbol(self):
        # Позитивные тесты
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")

        # Негативные тесты
        self.assertEqual(self.utils.delete_symbol("", "k"), "")
        self.assertEqual(self.utils.delete_symbol(" ", "k"), " ")
        self.assertEqual(self.utils.delete_symbol(None, "k"), None)
        self.assertEqual(self.utils.delete_symbol("SkyPro", ""), "SkyPro")


if __name__ == "__main__":
    unittest.main()
