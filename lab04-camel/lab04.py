import random

def Introduccion():
    print('¡Bienvenido a Camello!'
        '\nHas robado un camello para atravesar el desierto de Mobi.'
        '\n¡Los nativos quieren recuperar su camello y te están persiguiendo!'
        '\nSobrevive en el desierto y escapa de los nativos.')

def BeberCantimplora(c):
    while(c != 0):
        return c-1, 0
    else:
        print('\nError de cantimploras\n')
        exit()

def AvanzarDespacio(a, b, c, d):
    a += random.randint(5, 12)
    print('\nHas recorrido', a, 'millas\n')

    return a, b+1, c+1, d+random.randint(7, 14)

def AvanzarRapido(a, b, c, d):
    a += random.randint(10, 20)
    print('\nHas recorrido', a, 'millas\n')

    return a, b+1, c+random.randint(1, 3), d+random.randint(7, 14)

def Descansar(d):
    print('\nEl camello esta contento\n')

    return 0, d+random.randint(7, 14)

def ComprobarEstado(a, b, c):
    print('\nHas recorrido', a, 'millas'
        '\nTienes', b, 'cantimploras'
        '\nLos nativos estan a', a-c, 'millas de ti\n')

def Salir():
    print('\nHas salido del juego\n')
    return True

def Oasis():
    print('\nHas entrado en el Oasis'
        '\nse restablecen cantimplora, sed y cansancio\n')
    return 3, 0, 0

def ComprobarCansancio(c):
    if(c < 5): return False
    elif(c >= 5 and c < 8):
        print('El camello se está cansando\n')
        return False
    else:
        print('\nEl camello esta muerto'
            '\nFin del juego\n\n')
        return True

def ComprobarDistancia(a, b):
    if(a > b): return False
    elif(a > b and a-b < 15):
        print('\n¡Los nativos se estan acercando!\n')
        return False
    else:
        print('\nLos nativos te han pillado'
            '\nFin del juego\n\n')
        return True

def ComprobarSed(s):
    if(s < 4): return False
    elif(s >= 4 and s < 6):
        print('\nTienes sed\n')
        return False
    else:
        print('\nTe has muerto de sed'
            '\nFin del juego\n\n')
        return True

def GanarJuego(c, a, b, s):
    if(c < 8 and a > b and a >= 200 and s < 6):
        print('\nHas hecho', a, 'millas'
            '\nHas ganado!!!'
            '\nFin del juego\n\n') 
        return True
    else: return False        

def Menu():
    millas_jugador = 0
    millas_nativos = -20
    cantimploras = 3
    sed = 0
    cansancio_camellos = 0
    done = False

    while(done == False):
        #menu
        print('\nA. Beber de la cantimplora.'
            '\nB. Avanzar despacio'
            '\nC. Avanzar rapido.'
            '\nD. Descansar.'
            '\nE. Comprobar estado.'
            '\nQ. Salir del juego.')

        op = input('Elija opcion: ')

        if(op == 'A'):
            cantimploras, sed = BeberCantimplora(cantimploras)
        elif(op == 'B'):
            millas_jugador, sed, cansancio_camellos, millas_nativos = AvanzarDespacio(millas_jugador, sed, cansancio_camellos, millas_nativos)
        elif(op == 'C'):
            millas_jugador, sed, cansancio_camellos, millas_nativos = AvanzarRapido(millas_jugador, sed, cansancio_camellos, millas_nativos)
        elif(op == 'D'):
            cansancio_camellos, millas_nativos = Descansar(millas_nativos)
        elif(op == 'E'):
            ComprobarEstado(millas_jugador, cantimploras, millas_nativos)
        elif(op == 'Q'):
            done = Salir()

        #oasis
        rand = random.randint(1, 20)
        if(rand == 12):  #'12' por ejemplo, puede ser otro num entre 1 y 20 ya que tienen probabilidad de 1/20
            cantimplora, sed, cansancio_camellos = Oasis()

        #progreso del juego        
        done = ComprobarCansancio(cansancio_camellos)
        if(done): exit()
        else:
            done = ComprobarDistancia(millas_jugador, millas_nativos)
            if(done): exit()
            else:
                done = ComprobarSed(sed)
                if(done): exit()
                else:
                    done = GanarJuego(cansancio_camellos, millas_jugador, millas_nativos, sed)

Introduccion()
Menu()