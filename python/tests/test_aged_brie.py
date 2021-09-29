import unittest
from src.gilded_rose import GildedRose, Item


class AgedBrieTest(unittest.TestCase):

    def test_should_increase_quality_by_1_when_sell_in_date_is_more_than_zero(self):
        items = [Item("Aged Brie", 2, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_should_increase_quality_by_2_when_sell_in_date_is_zero(self):
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_sell_in_date_is_zero(self):
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_zero(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_quality_more_than_zero_and_sell_in_date_is_less_than_zero(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_sell_in_date_is_less_than_zero(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_less_than_zero(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)