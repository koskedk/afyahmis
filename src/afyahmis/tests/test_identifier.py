import datetime
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
        patiendId = Identifier.new(IdentifierType.SERVICE, "10000010")
        self.assertEqual(patiendId.type, IdentifierType.SERVICE)
        self.assertEqual(patiendId.value, "10000010")
        logging.debug(f'{patiendId}')


if __name__ == '__main__':
    unittest.main()
