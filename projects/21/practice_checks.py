"""Run from this folder. Default checks starter; --reference checks the worked answer."""
import importlib
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
module = importlib.import_module('practice_reference' if '--reference' in sys.argv else 'practice_starter')
if '--reference' in sys.argv: sys.argv.remove('--reference')
task = module.validate_profile

class PracticeChecks(unittest.TestCase):
    def test_valid(self):
        d={'name':'A','headline':'D','about':'Demo','projects':[]}; self.assertEqual(task(d),d)

    def test_missing(self):
        with self.assertRaises(ValueError): task({'headline':'D','about':'Demo','projects':[]})

    def test_list(self):
        with self.assertRaises(ValueError): task({'name':'A','headline':'D','about':'Demo','projects':{}})

    def test_unsafe(self):
        with self.assertRaises(ValueError): task({'name':'A','headline':'D','about':'Demo','projects':[{'title':'T','description':'D','url':'javascript:alert(1)'}]})

    def test_link(self):
        self.assertEqual(len(task({'name':'A','headline':'D','about':'Demo','projects':[{'title':'T','description':'D','url':'https://example.test/a'}]})['projects']),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
