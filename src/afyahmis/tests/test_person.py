import logging
import sys
import unittest
from datetime import datetime

from src.afyahmis.gender import Gender
from src.afyahmis.person import Person

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))


class TestPerson(unittest.TestCase):
    def test_new(self):
        person = Person.from_demographics('John', 'Wick', Gender.MALE, datetime(1983, 4, 7).date())
        self.assertEqual(person.name.first_name, 'John')
        self.assertEqual(person.name.last_name, 'WICK')
        self.assertEqual(person.gender, Gender.MALE)
        self.assertEqual(person.dob, datetime(1983, 4, 7).date())
        logging.debug(f'{person}')


if __name__ == '__main__':
    unittest.main()
