from dataclasses import dataclass


@dataclass
class PersonName:
    _first_name: str
    _last_name: str

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name.upper()

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @classmethod
    def new(cls, first_name, last_name):
        return cls(first_name, last_name)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
