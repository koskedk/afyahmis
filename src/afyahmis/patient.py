import datetime

from src.afyahmis.gender import Gender
from src.afyahmis.identifier import Identifier
from src.afyahmis.identifier_type import IdentifierType
from src.afyahmis.person import Person
from src.afyahmis.person_name import PersonName


class Patient(Person):
    _identifier: Identifier

    @property
    def identifier(self):
        return self._identifier

    def __init__(self, name: PersonName, gender: Gender, dob: datetime.date, identifier: Identifier):
        self._identifier = identifier
        Person.__init__(self, name, gender, dob)

    @classmethod
    def from_details(cls, first_name, last_name, gender, dob, id_type: IdentifierType, id_value):
        name = PersonName.from_names(first_name, last_name)
        identifier = Identifier.from_id(id_type, id_value)
        return cls(name, gender, dob, identifier)

    def __str__(self):
        return f'{self.name}, {self.gender} {self.age} [{self.identifier}]'
