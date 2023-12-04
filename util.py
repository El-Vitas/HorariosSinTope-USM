class Nombres_atributos:
    campus =  "Campus/Sede"
    asignatura = "Asignatura"
    profesor = "Profesor"
    paralelo = "Paralelo"

dias = {
    0: 'lunes',
    1: 'martes',
    2: 'miercoles',
    3: 'jueves',
    4: 'viernes',
    5: 'sabado',
    6: 'domingo'
}


def cargar_html(ruta) -> str:
    with open(ruta, 'r', encoding='latin-1') as archivo:
        return archivo.read()

def guardar_html(ruta,html) -> None:
    with open(ruta, 'w', encoding='latin-1') as archivo:
        archivo.write(html)