from informacion import Curso, Horario
import re
from util import Nombres_atributos, dias

def establecer_horario(tabla, curso: Curso) -> None:
    trs = tabla.find_all('tr', recursive=False)
    for i, tr in enumerate(trs[1:]):
        tds = tr.find_all('td', recursive=False)
        for j, td  in enumerate(tds[2:]):
            resultado = td.find_all('td', attrs={'bgcolor': True})
            if resultado:
                onmouse = resultado[0].get('onmouseover', '')
                catedra = re.findall(r'\bCátedra\b', onmouse, flags=re.IGNORECASE)
                if catedra:
                    dia = dias[j]
                    bloque = i*2 +1
                    sala = re.search(r'Sala (\w+)', resultado[0].text).group(1)
                    horario = Horario()
                    horario.sala = sala
                    horario.bloques = f"{dia}-{bloque}-{bloque+1}"
                    curso.horarios.append(horario)

def obtener_curso(tabla) -> Curso:
    curso = Curso()
    nombre_atributo = re.compile(f'.*{Nombres_atributos.campus}.*')
    atributo = tabla.find('td',string=nombre_atributo)
    aux_atributo = atributo.find_next_siblings('td', limit=2)
    curso.campus = (aux_atributo[-1].text).strip()

    nombre_atributo = re.compile(f'.*{Nombres_atributos.asignatura}.*')
    atributo = tabla.find('td',string=nombre_atributo)
    aux_atributo = atributo.find_next_siblings('td', limit=2)
    curso.asignatura = (aux_atributo[-1].text).strip()

    nombre_atributo = re.compile(f'.*{Nombres_atributos.paralelo}.*')
    atributo = tabla.find('td',string=nombre_atributo)
    aux_atributo = atributo.find_next_siblings('td', limit=2)
    curso.paralelo = re.search(r'^\D*(\d+)', aux_atributo[-1].text).group(1)

    nombre_atributo = re.compile(f'.*{Nombres_atributos.profesor}.*')
    atributo = tabla.find('td',string=nombre_atributo)
    aux_atributo = atributo.find_next_siblings('td', limit=2)
    curso.profesor = (aux_atributo[-1].text).strip()

    return curso


def crear_lista_cursos(cursos: list[Curso]):
    lista_cursos = []

    for curso in cursos:
        asignatura = curso.asignatura

        for lista in lista_cursos:
            if lista[0].asignatura == asignatura:
                lista.append(curso)
                break
        else:
            lista_cursos.append([curso])

    return lista_cursos