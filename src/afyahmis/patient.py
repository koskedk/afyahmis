from src.afyahmis.identifier import Identifier
from src.afyahmis.identifier_type import IdentifierType
from src.afyahmis.person import Person
from src.afyahmis.person_name import PersonName


class Patient(Person):
    _identifier: Identifier

    @property
    def identifier(self):
        return self._identifier

    def __init__(self, name, gender, dob, identifier):
        Person.__init__(name, gender, dob)
        self._identifier = identifier

    @classmethod
    def new(cls, first_name, last_name, gender, dob, id_type: IdentifierType, id_value):
        name = PersonName.new(first_name, last_name)
        identifier = Identifier.new(id_type, id_value)
        return cls(name, gender, dob, identifier)

    def __str__(self):
        return f'{self.name}, {self.gender} {self.age} [{self.identifier}]'
