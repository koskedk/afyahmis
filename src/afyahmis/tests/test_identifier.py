import logging
import sys
import unittest

from src.afyahmis.identifier import Identifier
from src.afyahmis.identifier_type import IdentifierType

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))


class TestIdentifier(unittest.TestCase):
    def test_new(self):
        patiend_id = Identifier.from_id(IdentifierType.SERVICE, "10000010")
        self.assertEqual(patiend_id.type, IdentifierType.SERVICE)
        self.assertEqual(patiend_id.value, "10000010")
        logging.debug(f'{patiend_id}')


if __name__ == '__main__':
    unittest.main()
