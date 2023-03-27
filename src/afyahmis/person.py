import datetime

from src.afyahmis.age import Age
from src.afyahmis.gender import Gender
from src.afyahmis.person_name import PersonName


class Person:
    _name: PersonName
    _gender: Gender
    _dob: datetime.date
    _age: Age

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def dob(self):
        return self._dob

    @property
    def age(self):
        return self._age

    def __init__(self, name: PersonName, gender: Gender, dob: datetime.date):
        self._name = name
        self._gender = gender
        self._dob = dob
        self._age = Age.from_dob(dob)

    @classmethod
    def from_demographics(cls, first_name, last_name, gender, dob):
        name = PersonName.from_names(first_name, last_name)
        return cls(name, gender, dob)

    def __str__(self):
        return f'{self.name}, {self.gender.value} {self.age}'
