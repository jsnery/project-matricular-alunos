cursos = {
    'ads': {
        'informatica': {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0
        }
    }
}


class Person:
    def __init__(self, name, lastname, birthdate) -> None:
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate


class Studant(Person):
    def __init__(self, name, lastname, birthdate, cpf, curso) -> None:
        super().__init__(name, lastname, birthdate)
        self.cpf = cpf
        self.curso = curso
        self.assessments = curso

    @property
    def assessments(self):
        return self._assessments

    @assessments.setter
    def assessments(self, value: str):
        self._assessments = cursos[value]


if __name__ == '__main__':
    aluno = Studant('Richard', 'Neri', '28/12/1999', '08323217530', 'ads')
    print(aluno.assessments)
