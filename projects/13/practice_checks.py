"""Run from this folder. Default checks starter; --reference checks the worked answer."""
import importlib
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
module = importlib.import_module('practice_reference' if '--reference' in sys.argv else 'practice_starter')
if '--reference' in sys.argv: sys.argv.remove('--reference')
task = module.validate_book

class PracticeChecks(unittest.TestCase):
    def test_normalized(self):
        self.assertEqual(task({'title':' Demo ','author':' Ada ','price':'12.5'})['price'],'12.50')

    def test_negative(self):
        with self.assertRaises(ValueError): task({'title':'D','author':'A','price':'-1'})

    def test_blank(self):
        with self.assertRaises(ValueError): task({'title':' ','author':'A','price':'1'})

    def test_extra(self):
        with self.assertRaises(ValueError): task({'title':'D','author':'A','price':'1','id':1})

    def test_false(self):
        self.assertFalse(task({'title':'D','author':'A','price':'1','available':False})['available'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
