import sys
import json


class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__(self):
        return f"Auto: {self.znacka} / {self.model} / {self.barva}"
    
    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata1)
        for value in ("znacka", "model", "barva"):
            if value not in data:
                raise ValueError(f"Invalid data: missing '{value}'")
        return cls(data["znacka"], data["model"], data["barva"])
    

if __name__ == "__main__":

    jdata1 = '{"znacka": "bmw", "model": "x5", "barva": "cerna"}'
    jdata2 = '{"znacka": "toyota", "model": "corrola", "barva": "modra"}'

    data = json.loads(jdata1)

    auto1 = Car.parse(jdata1)
    