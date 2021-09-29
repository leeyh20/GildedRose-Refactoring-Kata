import unittest
from src.gilded_rose import GildedRose, Item


class SulfurasTest(unittest.TestCase):

    def test_should_leave_quality_unchanged_when_quality_more_than_1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)

    def test_should_leave_quality_unchanged_when_quality_starts_at_0(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_should_leave_quality_unchanged_when_quality_starts_at_1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_should_leave_quality_unchanged_when_quality_is_less_than_zero(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].quality)

    def test_should_leave_sell_in_unchanged_when_sell_in_starts_at_1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_should_leave_sell_in_unchanged_when_sell_in_less_than_zero(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    def test_should_leave_sell_in_unchanged_when_sell_in_more_than_1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 80, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].sell_in)