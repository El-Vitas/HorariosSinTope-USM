class Curso:
    def __init__(self) -> None:
        self.campus = ""
        self.asignatura = ""
        self.profesor = ""
        self.paralelo = ""
        self.horarios: list[Horario] = [] 

class Horario:
    def __init__(self) -> None:
        self.sala = ""
        self.bloques = ""