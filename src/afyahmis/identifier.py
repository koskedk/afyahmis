from dataclasses import dataclass

from src.afyahmis.identifier_type import IdentifierType


@dataclass
class Identifier:
    _type: IdentifierType
    _value: str

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    def __init__(self, id_type: IdentifierType, id_value):
        self._type = id_type
        self._value = id_value

    @classmethod
    def new(cls, id_type: IdentifierType, id_value):
        return cls(id_type, id_value)

    def __str__(self):
        return f'{self._type.value}: {self._value}'
