"""Run from this folder. Default checks starter; --reference checks the worked answer."""
import importlib
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
module = importlib.import_module('practice_reference' if '--reference' in sys.argv else 'practice_starter')
if '--reference' in sys.argv: sys.argv.remove('--reference')
task = module.money

class PracticeChecks(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(task('2.50'),Decimal('2.50'))
        self.assertIsInstance(task('2.50'),Decimal)

    def test_normalize(self):
        self.assertEqual(str(task('2')),'2.00')

    def test_precision(self):
        with self.assertRaises(ValueError): task('2.501')

    def test_nan(self):
        with self.assertRaises(ValueError): task('NaN')

    def test_negative(self):
        with self.assertRaises(ValueError): task('-1')

if __name__ == '__main__':
    unittest.main(verbosity=2)
