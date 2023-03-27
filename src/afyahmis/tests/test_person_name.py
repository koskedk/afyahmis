import logging
import sys
import unittest

from src.afyahmis.person_name import PersonName

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))


class TestPersonName(unittest.TestCase):
    def test_new(self):
        name = PersonName.from_names('John', 'Wick')
        self.assertEqual(name.first_name, 'John')
        self.assertEqual(name.last_name, 'WICK')
        logging.debug(f'{name}')


if __name__ == '__main__':
    unittest.main()
