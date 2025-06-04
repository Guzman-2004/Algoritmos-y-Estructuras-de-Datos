import random

def Menu():
    print("~~~~~~~~~~~~~~~~~~~~~~TRIVIAL~~~~~~~~~~~~~~~~~~~~~~")
    print("""
        
        Bienvenidos al trivial, las instrucciones son las siguientes:

        -Se lanzará un dado con un número aleatorio 
        -Se generara dependiendo del numero una pregunta sobre distintas tematicas
        -Si se aciertan 3 preguntas correctamente de una misma tematica, se obtiene gana un quesito de esa categoría
        -El jugador que obtenga todo los quesos gana
        -TIENES QUE RESPONDER A LAS PREGUNTAS True or False""")
    

def Opcion():
    opc = int(input("Número de jugadores: "))
    return opc

def TirarDado():
    n = random.randint(1,4)
    if n == 1:
        categoria = "Historia"

    if n == 2:
        categoria = "Ciencias Naturales"

    if n == 3:
        categoria = "Deportes"

    if n == 4:
        categoria = "Geografía"

    print(f"""{n} """)
    return categoria
