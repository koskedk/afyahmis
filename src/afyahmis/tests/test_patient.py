import logging
import sys
import unittest
from datetime import datetime

from src.afyahmis.gender import Gender
from src.afyahmis.identifier_type import IdentifierType
from src.afyahmis.patient import Patient

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))


class TestPatient(unittest.TestCase):
    def test_new(self):
        patient = Patient.from_details('John', 'Wick', Gender.MALE, datetime(1983, 4, 7).date(),
                                       IdentifierType.NATIONAL,
                                       'HLS-9910-KE')
        self.assertEqual(patient.name.first_name, 'John')
        self.assertEqual(patient.name.last_name, 'WICK')
        self.assertEqual(patient.gender, Gender.MALE)
        self.assertEqual(patient.dob, datetime(1983, 4, 7).date())
        logging.debug(f'{patient}')


if __name__ == '__main__':
    unittest.main()
