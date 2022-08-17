from django.test import TestCase
from .models import Yield

class YieldTest(TestCase):
    """ Test module for Yield model """

    def setUp(self):
        Yield.objects.create(
            yr=1986, qty=3)
        Yield.objects.create(
            yr=2000, qty=6)

    def test_yield(self):
        yield_1986 = Yield.objects.get(yr=1986)
        yield_2000 = Yield.objects.get(yr=2000)
        self.assertEqual(
            yield_1986.get_qty(), 3)
        self.assertEqual(
            yield_2000.get_qty(), 6)