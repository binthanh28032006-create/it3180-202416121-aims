import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class SearchByCategoryTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
        ]

    def test_search_by_category(self):
        results = search_by_category(self.items, "animation")
        self.assertEqual([dvd.title for dvd in results], ["The Lion King"])

    def test_empty_category_returns_all_items(self):
        self.assertEqual(search_by_category(self.items, ""), self.items)


if __name__ == "__main__":
    unittest.main()
