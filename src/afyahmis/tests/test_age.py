import datetime
import logging
import sys
import unittest

from src.afyahmis.age import Age
from src.afyahmis.age_unit import AgeUnit

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))


class TestAge(unittest.TestCase):
    def test_years(self):
        dob = datetime.date(1983, 4, 7)
        age = Age.from_dob(dob)
        self.assertEqual(age.unit, AgeUnit.YEARS)
        self.assertTrue(age.value > 1)
        logging.debug(f'Age in years:{age}')

    def test_years_from_date(self):
        from_date = datetime.date(1983, 4, 7)
        dob = datetime.date(1982, 4, 7)
        age = Age.from_dob(dob, from_date)
        self.assertEqual(age.unit, AgeUnit.YEARS)
        self.assertEqual(age.value, 1)
        logging.debug(f'Age in years:{age}')

    def test_months_from_date(self):
        from_date = datetime.date(1983, 4, 7)
        dob = datetime.date(1983, 1, 7)
        age = Age.from_dob(dob, from_date)
        self.assertEqual(age.unit, AgeUnit.MONTHS)
        self.assertEqual(age.value, 3)
        logging.debug(f'Age in months:{age}')

    def test_days_from_date(self):
        from_date = datetime.date(1983, 4, 7)
        dob = datetime.date(1983, 4, 1)
        age = Age.from_dob(dob, from_date)
        self.assertEqual(age.unit, AgeUnit.DAYS)
        self.assertEqual(age.value, 6)
        logging.debug(f'Age in days:{age}')

    def test_days_from_date(self):
        from_date = datetime.date(1983, 4, 1)
        dob = datetime.date(1983, 4, 1)
        age = Age.from_dob(dob, from_date)
        self.assertEqual(age.unit, AgeUnit.DAYS)
        self.assertEqual(age.value, 0)
        logging.debug(f'Age in days:{age}')


if __name__ == '__main__':
    unittest.main()
