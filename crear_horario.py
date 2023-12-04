import os

from informacion import Curso
from util import cargar_html, guardar_html

def crear_horario(final: list[list[Curso]]):
    html = ""
    dias_semana = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
    if len(final) == 0:
        print("\nNo existen horarios que no provoquen tope para este caso.")
    else:
        for i,lista_curso in enumerate(final):
            html = cargar_html("estructura.html")
            bool_dia = {dia: False for dia in dias_semana}
            html = remplazar_bloques(lista_curso, bool_dia, html)
            html = rellenar_extras(dias_semana,bool_dia, html)
            ruta = os.path.join("resultado", f"horario{i}.html")
            guardar_html(ruta, html)
        print("\nHorarios creados con exito.")

def remplazar_bloques(lista_curso: list[Curso], bool_dia: list[bool], html: str) -> str:
    txt = "<tr><td align='center' bgcolor='#FF9900'><font color='#FFFFFF'>&nbsp;{ASIGNATURA} | Sala: {SALA} | Paralelo: {PARALELO} &nbsp;</font></td></tr>"
    for curso in lista_curso:
        for horario in curso.horarios:
            elementos = horario.bloques.split("-")
            asignatura = curso.asignatura.split("-")[0]
            dia = elementos[0].upper()
            texto = txt.format(ASIGNATURA=asignatura, SALA=horario.sala, PARALELO=curso.paralelo, PROFESOR = curso.profesor)
            cadena_busqueda = f"{{{{{dia}{elementos[1]}}}}}"
            html = html.replace(cadena_busqueda, texto)
            cadena_busqueda = f"{{{{{dia}{elementos[2]}}}}}"
            html = html.replace(cadena_busqueda, "")

            if not bool_dia[dia]:
                bool_dia[dia] = True
                cadena_busqueda = f"{{{{{dia}-INFO}}}}"
                texto = f"<h2>{dia}</h2>"
                html = html.replace(cadena_busqueda, texto)

            cadena_busqueda = f"{{{{DESCRIPCION-{elementos[0].upper()}{elementos[1]}-{elementos[2]}}}}}"
            texto = f'''
            <h3>&nbsp;&nbsp;&nbsp;&nbsp;Bloque: {elementos[1]}-{elementos[2]}</h3>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Asignatura: {curso.asignatura}, Sala: {horario.sala}, Profesor: {curso.profesor}</p>
            '''
            html = html.replace(cadena_busqueda, texto)
    return html

def rellenar_extras(dias_semana: list[str], bool_dia: list[bool], html: str) -> str:
    txt = "<tr><td align='center'>&nbsp;</td></tr>"
    for dia in dias_semana:
        for numero in range(1, 21,2):
            cadena_busqueda = f"{{{{{dia}{numero}}}}}"
            html = html.replace(cadena_busqueda, txt)

            cadena_busqueda = f"{{{{{dia}{numero+1}}}}}"
            html = html.replace(cadena_busqueda, txt)

            cadena_busqueda = f"{{{{DESCRIPCION-{dia}{numero}-{numero+1}}}}}"
            html = html.replace(cadena_busqueda, "")

        if not bool_dia[dia]:
            cadena_busqueda = f"{{{{{dia}-INFO}}}}"
            html = html.replace(cadena_busqueda, "")
    return html