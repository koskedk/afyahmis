import datetime
from dataclasses import dataclass

from src.afyahmis.age_unit import AgeUnit


@dataclass
class Age:
    _value: int
    _unit: AgeUnit

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def __init__(self, dob: datetime.date, from_date=datetime.date.today()):
        if from_date < dob:
            raise Exception('from date is less than dob')

        years = from_date.year - dob.year - ((from_date.month, from_date.day) < (dob.month, dob.day))
        months = from_date.month - dob.month
        days = abs(from_date.day - dob.day)

        if years > 0:
            self._value = years
            self._unit = AgeUnit.YEARS
            return

        if months > 0:
            self._value = months
            self._unit = AgeUnit.MONTHS
            return

        self._value = days
        self._unit = AgeUnit.DAYS

    @classmethod
    def from_dob(cls, dob: datetime.date, from_date=datetime.date.today()):
        return cls(dob, from_date)

    def __str__(self):
        return f'{self._value} {self._unit.value}'
