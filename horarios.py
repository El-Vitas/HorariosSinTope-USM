import os 

from bs4 import BeautifulSoup as bs
from informacion import Curso
from crear_horario import crear_horario
from crear_curso import obtener_curso, establecer_horario, crear_lista_cursos

final = []

def verificar_tope(cursos: list[Curso], curso_actual: Curso):
    for curso in cursos:
        if curso != 0:
            for horario in curso.horarios:
                for h in curso_actual.horarios:
                    if h.bloques == horario.bloques:
                        return True
    return False

def horarios_sin_tope(lista_cursos: list[list[Curso]], n: int, cursos: list[Curso], nivel: int):
    global final

    if nivel == n:
        final.append(list(cursos))
        return

    lista_curso = lista_cursos[nivel]

    for curso in lista_curso:
        if verificar_tope(cursos,curso):
            return
        cursos[nivel] = curso
        horarios_sin_tope(lista_cursos,n,cursos, nivel+1)
        cursos[nivel] = 0
    return 


def main():
    global final
    directorio_archivos = "archivos"
    nombres_archivos = os.listdir(directorio_archivos)
    cursos: list[Curso] = []

    for nombre_archivo in nombres_archivos:
        ruta_archivo = os.path.join(directorio_archivos, nombre_archivo)
        with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
            html = archivo.read()
        soup = bs(html, "lxml")
        tablas = soup.find_all('table')
        curso = obtener_curso(tablas[0])
        establecer_horario(tablas[1], curso)

        cursos.append(curso)

    lista_cursos = crear_lista_cursos(cursos)
    n = len(lista_cursos)
    pos = [0 for i in range(n)]
    horarios_sin_tope(lista_cursos,n,pos, 0)
    crear_horario(final)

if __name__ == "__main__":
    main()
