import unittest
from src.gilded_rose import GildedRose, Item


class GenericItemTest(unittest.TestCase):

    def test_should_reduce_quality_by_0_when_quality_starts_at_0(self):
        items = [Item("Generic Item", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_should_reduce_quality_by_2_when_quality_starts_at_2(self):
        items = [Item("Generic Item", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_should_reduce_quality_by_1_when_quality_starts_at_1(self):
        items = [Item("Generic Item", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_should_reduce_quality_by_2_when_quality_starts_at_20(self):
        items = [Item("Generic Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)