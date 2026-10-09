"""Run from this folder. Default checks starter; --reference checks the worked answer."""
import importlib
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
module = importlib.import_module('practice_reference' if '--reference' in sys.argv else 'practice_starter')
if '--reference' in sys.argv: sys.argv.remove('--reference')
task = module.invoice_total

class PracticeChecks(unittest.TestCase):
    def test_total(self):
        self.assertEqual(task(2,'125.50'),'251.00')

    def test_zero_rate(self):
        self.assertEqual(task(2,'0'),'0.00')

    def test_quantity(self):
        with self.assertRaises(ValueError): task(0,'2')

    def test_nan(self):
        with self.assertRaises(ValueError): task(1,'NaN')

    def test_precision(self):
        with self.assertRaises(ValueError): task(1,'1.001')

if __name__ == '__main__':
    unittest.main(verbosity=2)
