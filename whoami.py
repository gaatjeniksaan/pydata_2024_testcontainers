class Hydrogeologist:
    def __init__(self, name: str, university: str) -> None:
        self.name = name
        self.university = university


class DataSoftwareDude:
    def __init__(self, hydrogeologist: Hydrogeologist):
        self.name = hydrogeologist.name
        self.university = hydrogeologist.university
    
    def __str__(self) -> str:
        return f"Hello data/software dude {self.name}!"


oude_barend = Hydrogeologist(name="Barend Linders", university="Utrecht University")
barend = DataSoftwareDude(oude_barend)

print(barend)

