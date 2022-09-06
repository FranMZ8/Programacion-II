import random
import os

def menuPrincipal():
    print("\nBienvenido a la Travesia del Pirata")
    print("Elija una opcion")
    print("1. Empezar Juego")
    print("2. Salir del Juego\n")

def introduccion():
    print("Estas en una carcel encerrado hace algunos meses debido a la traicion de tu antiguo compañero Barbanegra")
    print("Fuera de la celda escuchas unos pasos acercandose")
    print("Ves que un guardia abre tu celda y lanza una persona dentro")
    print("Se va el guardia y empiezas a dialogar con el, te cuenta que se llama William y que era miembro de una tripulacion pirata")
    usuario = input("Le decis que te llamas: ")
    print("Y que estas planeando escapar de la prision al dia siguiente, por lo que le pedis ayuda")
    return usuario

#Da de forma aleatoria una criatura a la pelea con criatura(Trayecto Corto)
def criaturaFantasiosa():
    criaturas = ["Kraken","Sirenas","Leviatan"]
    num = random.randint(0,2)
    return criaturas[num]

#Decision del camino de las sirenas (Trayecto Corto)
def sirenas():
    print("\nVes una pequeña isla con un barco encallado que podria tener tesoros.")
    accion1 = int(input("Tienes que tomar la decision. 1. Te acercas a la isla 2. Pasas de largo\n"))
    while accion1!=1 and accion1!=2:
        accion1 = int(input("Ingrese nuevamente la opcion: "))
        if accion1!=1 and accion1!=2:
            print("Opcion Erronea")
    #Te acercas a la isla
    if accion1==1:
        print("\nDecides acercarte a la isla y empiezas a sentirte relajado.")
        print("Ves a varios de tus compañeros saltando por la borda en direccion a la isla.")
        print("Y empiezas a escuchar un canto tan bello que te fuerza a seguirlo")
        print("Momentos antes de caer al agua ves a bellas mujeres y te das cuenta que eran sirenas...\n")
        print("Terminas hechizado por las Sirenas sin poder lograr tu venganza")
        print("FINAL MALO")
    #Pasas de largo
    elif accion1==2:
        print("\nMientras te alejas de la isla ves que cerca de ella se encontraban unas sirenas que hubieran sido un problema")
        print("Tal vez por suerte o intuicion te libraste de un mal destino")
    return accion1

#Da de forma aleatoria una cantidad de oro (Trayecto Corto)
def tesoro():
    aleatorio = random.randint(1,10)
    if aleatorio<=3:
        return 200
    elif aleatorio>=4 and aleatorio<=7:
        return 350
    elif aleatorio==10:
        return 500
    else:
        return 0

#Da de forma aleatoria una trampa en el templo (Trayecto largo)
def trampa():
    aleatorio = random.randint(1,10)
    if aleatorio<=2:
        print()
        return 1,"Aplastado"
    elif aleatorio>=3 and aleatorio<=7:
        return 2,"Caida con pinchos"
    elif aleatorio>7:
        return 3,"Flechas envenenadas"

#Da de forma aleatoria un monstruo en el templo (Trayecto largo)
def monstruosTemplo():
    criaturas = ["Momias","Esqueletos","Fantasmas"]
    num = random.randint(0,2)
    return criaturas[num]

while(True):
    
    #Variables
    opcion = 0
    tripulantes = 20
    barco = 100
    oro = 0
    menuPrincipal()
    #Ingresa y verifica que la opcion sea 1 o 2
    while opcion!=1 and opcion!=2:
        opcion = int(input("Ingrese una opcion: "))
        if opcion!=1 and opcion!=2:
            print("Opcion Erronea\n")
    
    #JUGAR
    if opcion == 1:
        
        #INICIO DEL JUEGO
        os.system("cls")
        usuario = introduccion()
        print("Al dia siguiente, William inicia una pelea en el patio con otros prisioneros mientras vos terminas de excavar el tunel.\n")
        print("Acabas de terminar de excavar, te escapas ahora mismo dejando a William atras o esperas a la noche para irte con el")
        opcion1 = int(input("1. Escapar y abandonar a William // 2. Esperar a la noche\n"))
        #Verifica la opcion
        while opcion1!=1 and opcion1!=2:
            opcion1 = int(input("Ingrese nuevamente la opcion: "))
            if opcion1!=1 and opcion1!=2:
                print("Opcion Erronea")
        
        #Opcion William abandonado
        if opcion1==1:
            print("")
            print("Decides abandonar a William a su suerte. Luego de correr un rato llegas al barco en el que tu tripulacion te esta esperando")
        
        #Opcion Escapar con William
        elif opcion1==2:
            print("")
            print("Decides esperar a la noche. Escapas a la noche en silencio con William y llegas al barco en el que tu tripulacion te esta esperando")
            tripulantes=tripulantes+1

        print("Al llegar al barco tu tripulacion te da la bienvenida y decides que rumbo tomar hacia tu enemigo")
        rumbo=int(input("Elegis 1. El Trayecto Corto pero mas peligro 2. El Trayecto Largo pero mas tranquilo\n"))
        #Verifica la opcion
        while rumbo!=1 and rumbo!=2:
            rumbo = int(input("Ingrese nuevamente la opcion: "))
            if rumbo!=1 and rumbo!=2:
                print("Opcion Erronea")
        print("")
        
        #Trayecto Corto
        if rumbo==1:
            print("Elegiste el Trayecto Corto pero tambien el mas PELIGROSO")
            print("Despues de unos dias de viaje, se encuentran con una tormenta que no parece normal")
            print("En la lejania se logra ver algo pero no con claridad. Decides acercarte para averiguar que es.")
            monstruo=criaturaFantasiosa()

            #Kraken
            if monstruo=="Kraken":
                print("")
                print("Te acercas con curiosidad y ves unos tentaculos gigantes en el mar... ES EL KRAKEN")
                print("Le ordenas a tu tripulacion que preparen los cañones")
                accion1 = int(input("1. Esperas a que se acerque 2. Disparas desde lejos\n"))
                #Verifica la opcion
                while accion1!=1 and accion1!=2:
                    accion1 = int(input("Ingrese nuevamente la opcion: "))
                    if accion1!=1 and accion1!=2:
                        print("Opcion Erronea")
                print("")
                
                #Esperar1
                if accion1==1:
                    print("Decidiste esperar a que se acerque, este sacude el barco y los cañones logran golpearlo haciendo que este se aleje malherido")
                    barco=barco-20
                
                #Disparar1
                elif accion1==2:
                    print("Elegiste disparar desde lejos, pero fallas!!")
                    print("El Kraken golpea el barco y caen varios de tus tripulantes al mar")
                    barco = barco-20
                    tripulantes = tripulantes-4
                    accion2=int(input("El Kraken se esta acercando, 1. Disparar 2. Esperar\n"))
                    #Verifica la opcion
                    while accion2!=1 and accion2!=2:
                        accion2 = int(input("Ingrese nuevamente la opcion: "))
                        if accion2!=1 and accion2!=2:
                            print("Opcion Erronea")
                    print("")
                    
                    #Disparar2
                    if accion2==1:                        
                        print("Esperas y el Kraken golpea el barco pero con los cañones le das de lleno y este se retira")
                        barco = barco-30
                    
                    #Esperar2
                    elif accion2==2:
                        print("Decides seguir esperando a que el temible Kraken se acerque mientras tus compañeros estan listos para disparar")
                        accion3 = int(input("El Kraken va a atacar, 1. Disparar 2. Esperar\n"))
                        #Verifica la opcion
                        while accion3!=1 and accion3!=2:
                            accion3 = int(input("Ingrese nuevamente la opcion: "))
                            if accion3!=1 and accion3!=2:
                                print("Opcion Erronea")
                        print("")
                        
                        #Disparar3
                        if accion3==1:
                            print("Ordenas disparar pero el kraken golpea a varios miembros de tu tripulacion y son comidos por el.") 
                            print("Por suerte las balas del cañon logran darle, debido a el daño Kraken se retira")
                            tripulantes = tripulantes-4
                        
                        #Esperar3
                        elif accion3==2:
                            print("Decides esperar...")
                            accion4 = int(input(f"Tu tripulacion esta lista para disparar y el kraken se esta acercando. Que haces Capitan {usuario}?, 1. Disparar 2. Esperar"))
                            #Verifica la opcion
                            while accion4!=1 and accion4!=2:
                                accion4 = int(input("Ingrese nuevamente la opcion: "))
                                if accion4!=1 and accion4!=2:
                                    print("Opcion Erronea")
                            print("")
                            
                            #Disparar4
                            if accion4==1:
                                print("Das la orden de disparar al Kraken y este golpea la popa del barco, llevandose parte de este junto a varios miembros de tu tripulacion")
                                barco = barco-40
                                tripulantes=tripulantes-4
                            
                            #Esperar4
                            if accion4==2:
                                print(f"Decides seguir esperando apesar de que tus compañeros te estan gritando, Capitan {usuario} dé la orden\n")
                                print("Mueres a causa del Kraken sin poder terminar tu venganza")
                                print("FINAL MALO")
                                os.system("pause")
                                os.system("cls")
                                continue
           
            #Leviatan
            elif monstruo=="Leviatan":
                print("")
                print("Te acercas con curiosidad y ves una especide de serpiente en el mar... ES EL LEVIATAN")
                print("Le ordenas a tu tripulacion que preparen los cañones")
                accion1 = int(input("1. Disparas desde lejos 2. Llamar su atencion\n"))
                #Verifica la opcion
                while accion1!=1 and accion1!=2:
                    accion1 = int(input("Ingrese nuevamente la opcion: "))
                    if accion1!=1 and accion1!=2:
                        print("Opcion Erronea")
                print("")
                
                #Disparar1
                if accion1==1:
                    print("Decidiste disparar desde lejos tomando al Leviatan por sorpresa")
                    print("El gran monstruo a causa de la furia arremente en linea recta y los cañones aprovechan para dispararle.")
                    print("Despues de cada impacto el Leaviatan se ve mas debil para al final terminar descendiendo a las profundidades del mar")                 
                
                #Llamar Atencion1
                elif accion1==2:
                    print("Elegiste llamar la atencion del Leviatan, este se empieza a acercar rapidamente")                   
                    accion2=int(input("El Leviatan se esta acercando, 1. Disparar 2. Esperar\n"))
                    #Verifica la opcion
                    while accion2!=1 and accion2!=2:
                        accion2 = int(input("Ingrese nuevamente la opcion: "))
                        if accion2!=1 and accion2!=2:
                            print("Opcion Erronea")
                    print("")
                    
                    #Esperar2
                    if accion2==2:                        
                        print("Esperas, con un movimiento de su cuerpo el Leviatan crea una gran ola sacuediendo el barco")
                        print("Ves que algunos de tus tripulantes caen al mar y decides huir dejandolos a manos del Leviatan")
                        tripulantes = tripulantes-4
                    
                    #Disparar2
                    elif accion2==1:
                        print("Decides disparar a el temible Leviatan, logras darle pero no es suficiente")
                        accion3 = int(input(f"El Leviatan va a atacar!! que eliges Capitan {usuario}, 1. Esperar 2. Disparar\n"))
                        #Verifica la opcion
                        while accion3!=1 and accion3!=2:
                            accion3 = int(input("Ingrese nuevamente la opcion: "))
                            if accion3!=1 and accion3!=2:
                                print("Opcion Erronea")
                        print("")
                        
                        #Disparar3
                        if accion3==2:
                            print("Ordenas disparar, pero el Leviatan golpea al barco y a varios miembros de tu tripulacion son comidos por el.") 
                            print("Por suerte las balas del cañon logran darle, debido a el daño Leviatan se retira")
                            tripulantes = tripulantes-6
                            barco = barco-30
                        
                        #Esperar3
                        elif accion3==1:
                            print("Decides esperar...")
                            accion4 = int(input(f"Tu tripulacion esta esperando ordenes y el Leviatan se esta acercando. Que haces Capitan {usuario}?, 1. Derribarlo 2. Intentar Huir\n"))
                            #Verifica la opcion
                            while accion4!=1 and accion4!=2:
                                accion4 = int(input("Ingrese nuevamente la opcion: "))
                                if accion4!=1 and accion4!=2:
                                    print("Opcion Erronea")
                            print("")
                            
                            #Disparar4
                            if accion4==1:
                                print("El Leviatan golpea el barco de lleno llevandose parte de este junto a varios miembros de tu tripulacion")
                                print("Das la orden de derribarlo y ves como lentamente se hunde en el fondo del mar")
                                barco = barco-30
                                tripulantes=tripulantes-8
                            
                            #Intentar Huir4
                            if accion4==2:
                                print("A causa del miedo provocado por el Leviatan, das la orden de retirada")
                                print("Pero ya es muy tarde. El monstruo se lleva por delante la mitad del barco\n")
                                print("Mueres a causa del Leviatan sin poder terminar tu venganza")
                                print("FINAL MALO")
                                os.system("pause")
                                os.system("cls")
                                continue
            
            #Sirena
            else:
                aux=sirenas()              
                #En caso de FINAL MALO
                if aux==1:
                    os.system("pause")
                    os.system("cls")
                    continue
            
            #Arreglar barco
            if barco<100:
                print("\nDespues del encuentro con el monstruo, la tripulacion pregunta si deberian de reparar el barco.")
                print("Estando en el medio del mar solo es posible repararlo un poco")
                arreglar = int(input("1. Reparar el barco 2. Seguir la travesia\n"))
                #Verifica la opcion
                while arreglar!=1 and arreglar!=2:
                    arreglar = int(input("Ingrese nuevamente la opcion: "))
                    if arreglar!=1 and arreglar!=2:
                        print("Opcion Erronea")
                
                if arreglar==1:
                    barco=barco+20
                  
            #Pelea con otro barco pirata
            print("\nLuego de un tiempo navegando escuchas a un tripulante decir")
            print(f"Capitan {usuario} barco pirata a la vista\n")
            
            #Final Malo//40 de vida//no reparar//barco enemigo
            if barco<50:
                    print("Debido al daño recibido durante el combate con el monstruo y no haber reparado el barco.")
                    print("Los piratas enemigos logran acercarse lo suficiente para atacar y hundir el barco\n")
                    print("Terminas con el barco hundido y sin poder realizar tu venganza")
                    print("FINAL MALO")
                    os.system("pause")
                    os.system("cls")
                    continue
            
            #Es otro barco
            if opcion1==2:
                print("Ordenas a tu tripulacion que se preparen para el combate")
                print("Ya que durante el combate con el monstruo salio bien, estan en condiciones de pelear contra los piratas.")
                barco = barco-10
                tripulantes = tripulantes-2
                oro = tesoro()
                print(f"Das la orden de atacarlos y una vez concluye el combate van a reclamar la recompensa del enemigo. El enemigo tenia {oro} monedas de oro")
                print("En todo el combate pierdes dos de tus hombres")
            
            #Es William
            elif opcion1==1:
                print("Mientas ordenas a tu tripulacion que se preparen para el combate te das cuenta que su capitan es William, aquel pirata que abandonaste a su suerte")
                print("Ya que durante el combate con el monstruo salio bien, estan en condiciones de pelear contra los piratas.")
                oro = tesoro()
                print("Das la orden de atacarlos, mientras tu triupulacion aborda el barco de William este te maldice por haberlo traicionado y haber atacado su barco.")
                print("En todo el combate pierdes dos de tus hombres")
                print(f"Una vez concluye el combate van a reclamar la recompensa del enemigo. William tenia {oro} monedas de oro")
                tripulantes=tripulantes-2
                barco = barco-10

        #Trayecto Largo
        elif rumbo==2:
            print("Elegiste el Trayecto Largo y mas tranquilo")
            print("Despues de unos dias de viaje debido a una fuerte tormenta te desvias un poco de tu camino y encuentras una isla")
            decisionIsla = int(input("Tienes que decidir si acercarte o no 1. Pasas de largo 2. Investigas la isla\n"))
            #Verifica la opcion
            while decisionIsla!=1 and decisionIsla!=2:
                decisionIsla = int(input("Ingrese nuevamente la opcion: "))
                if decisionIsla!=1 and decisionIsla!=2:
                    print("Opcion Erronea")
            
            #Pasar de largo
            if decisionIsla==1:
                print(f"\nElegiste ignorar la isla, tu tripulacion no esta de acuerdo y te amenazan para que cambies tu decision, Que haces capitan {usuario}?")
                decisionIsla2 = int(input("1. No hacer caso a la tripulacion 2. Cambiar tu decision e ir a la isla\n"))
                #Verifica la opcion
                while decisionIsla2!=1 and decisionIsla2!=2:
                    decisionIsla2 = int(input("Ingrese nuevamente la opcion: "))
                    if decisionIsla2!=1 and decisionIsla2!=2:
                        print("Opcion Erronea")               
                
                #No hacer caso a la tripulacion//Final Malo
                if decisionIsla2==1:
                    print("\nDecides ignorar a tu tripulacion y seguir el rumbo")
                    print("Tu tripulacion se pone en contra tuya y te tiran por la borda\n")
                    print("Mueres ahogado sin poder realizar tu venganza")
                    print("FINAL MALO")
                    os.system("pause")
                    os.system("cls")
                    continue
            
            #Investigar Isla
            print("\nAl final decidiste acercarte a la isla y investigarla")
            print("Encuentras un templo en la isla el cual puede contener tesoros y decides explorarlo")
            accion1 = int(input("Al entrar al templo te encuentras con dos caminos 1. Derecha 2. Izquierda\n"))
            #Verifica la opcion
            print("")
            while accion1!=1 and accion1!=2:
                accion1 = int(input("Ingrese nuevamente la opcion: "))
                if accion1!=1 and accion1!=2:
                    print("Opcion Erronea")
            
            #Derecha1
            if accion1==1:
                print("Elegiste el camino de la derecha")
                #el aux son los tripulantes muertos
                aux,trampaTemplo = trampa()
                tripulantes = tripulantes-aux
                
                #Aplastado
                if trampaTemplo=="Aplastado":
                    print(f"Te topaste con una trampa, {aux} tripulante muere {trampaTemplo}")
                
                #Caida con pinchos
                elif trampaTemplo=="Caida con pinchos":
                    print(F"Te topaste con una trampa, {aux} tripulantes mueren por una {trampaTemplo}")
                
                #Flechas envenenadas
                else:
                    print(f"Te topaste con una trampa, {aux} tripulantes mueren por {trampaTemplo}")
                
                accion2 = int(input("Te encontraste con otra bifurcacion, que camino elegis? 1. Derecha 2. Izquierda\n"))
                #Verifica la opcion
                while accion2!=1 and accion2!=2:
                    accion2 = int(input("Ingrese nuevamente la opcion: "))
                    if accion2!=1 and accion2!=2:
                        print("Opcion Erronea")
                print("")
                
                #Derecha2
                if accion2==1:
                    print("Elegiste el camino de la derecha, vas directamente a la ultima sala del templo en la que se encuentra el tesoro y enemigos")
                
                #Izquierda2
                elif accion2==2:
                    print("Elegiste el camino de la izquierda")
                    #el aux son los tripulantes muertos
                    aux,trampaTemplo = trampa()
                    tripulantes = tripulantes-aux

                    #Aplastado
                    if trampaTemplo=="Aplastado":
                        print(f"Te topaste con una trampa, {aux} tripulante muere {trampaTemplo}")

                    #Caida con pinchos
                    elif trampaTemplo=="Caida con pinchos":
                        print(F"Te topaste con una trampa, {aux} tripulantes mueren por una {trampaTemplo}")

                    #Flechas envenenadas
                    else:
                        print(f"Te topaste con una trampa, {aux} tripulantes mueren por {trampaTemplo}")

            #Izquierda1
            elif accion1==2:
                print("Elegiste el camino de la izquierda")
                print("Este camino te lleva a la ultima sala del templo en la que se encuentra el tesoro y enemigos")

            #Sala final del templo
            monstruo=monstruosTemplo()
            print(f"Llegaste a la sala final del templo y te encuentras con un grupo de {monstruo}")
            print(f"Capitan {usuario}, que debemos hacer?")
            accion3 = int(input("1. Rodearlos  2. Pelear Separados  3. Pelear Juntos\n"))
            #Verifica la opcion
            while accion3!=1 and accion3!=2 and accion3!=3: 
                accion3 = int(input("Ingrese nuevamente la opcion: "))
                if accion3!=1 and accion3!=2 and accion3!=3:
                    print("Opcion Erronea")
            print("")

            #Rodearlos
            if accion3==1:
                print(f"Decidiste rodear a los {monstruo}, no fue una buena idea, 4 de tus tripulantes mueren pero terminan con ellos")
                tripulantes=tripulantes-4

            #Pelear Separados
            elif accion3==2:
                print(f"Decidiste pelar separados contra los {monstruo}, no fue una buena idea, 2 de tus tripulantes mueren pero terminan con ellos")
                tripulantes=tripulantes-2

            #Pelear Juntos
            elif accion3==3:
                print(f"Decidiste pelear juntos contra los {monstruo}, debido a esta buena decision logran terminar con ellos sin heridas")
            print(f"Luego de derrotar a los {monstruo} van a reclamar el cofre del tesoro, en este habia 600 monedas de oro")
            oro = 600
            print("Despues de este evento tu tripulacion y vos se dirigen hacia el barco para retomar su camino\n")
            
            #Ciudad//Pelea con guardias
            print("Varios dias despues llegas a una ciudad para recolectar informacion sobre el paradero de Barbanegra")
            print("Mientras la tripulacion reabastecia el barco de suministros, escuchaste conversaciones sobre lo fuerte que se convirtio Barbanegra en los ultimos meses")
            print("Vas a preguntarles si saben sobre su paradero y te responden que se habia dirigido hacia la isla pirata")
            print("Con esta informacion te diriges hacia el barco pero de fondo escuchas como la guardia real te empieza a perseguir")
            print("Logras llegar a tu barco, pero un navio de la guardia se interpone en tu camino")
            accion4 = int(input(f"Que decides Capitan {usuario}  1. Combatir  2. Huir\n"))
            #Verifica la opcion
            while accion4!=1 and accion4!=2:
                accion4 = int(input("Ingrese nuevamente la opcion: "))
                if accion4!=1 and accion4!=2:
                    print("Opcion Erronea")
            print("")

            #Combatir
            if accion4==1:
                print("Decidiste Combatir a la Guardia Real, debido a esto varios de tus tripulantes son capturados y tu barco recibe un gran daño.")
                tripulantes=tripulantes-2
                barco=barco-40
            
            #Huir
            elif accion4==2:
                print("Decidiste Huir, por esta eleccion tu barco recibe mucho daño pero no hay bajas.")
                barco=barco-50
            
            print("Lograste escapar de la Guardia Real y ahora te diriges hacia la isla pirata\n")

        #Se juntan los trayectos
        print("\nLuego de dias navegando, llegaste a la ciudad pirata.")
        print("Debido a los eventos pasados tienes que decidir en que priorizar el oro")
        print(f"Tienes {tripulantes} tripulantes")
        print(f"Tu barco esta al {barco}% de vida")
        print(f"Tienes {oro} de oro")
        print("En esta ciudad se arregla un 10% de vida del barco por 100 de oro y 50 de oro por cada tripulante")
        accion5 = int(input("1. Arreglar el barco  2. Contratar tripulantes 3.Sin Oro\n"))
        #Verifica la opcion
        while accion5!=1 and accion5!=2:
            accion4 = int(input("Ingrese nuevamente la opcion: "))
            if accion5!=1 and accion5!=2:
                print("Opcion Erronea")
        print("")
                
        #Arreglar Barco
        if accion5==1:
            if oro==0:
                print("No tenes oro")
            else:
                print("Se utilizo tu oro para reparar el barco y lo que sobro lo usaste para contratar nuevos tripulantes")
                while barco<100 and oro>0:
                    barco = barco + 10
                    oro = oro - 100
                while oro>0 and tripulantes<20:
                    tripulantes = tripulantes + 1
                    oro = oro - 50

        #Contratar tripulantes
        elif accion5==2:
            if oro==0:
                print("No tenes oro")
            else:
                print("Se utilizo tu oro para contratar nuevos tripulantes y lo que sobro lo usaste para reparar el barco")
                while oro>0 and tripulantes<20:
                    tripulantes = tripulantes + 1
                    oro = oro - 50
                while barco<100 and oro>0:
                    barco = barco + 10
                    oro = oro - 100

        print(f"Con tu decision tu barco tiene {barco}% de vida y tienes {tripulantes} tripulantes")
        print("Una vez con el oro gastado, te dispones a perseguir a barbanegra que ya partio de la isla\n")
        print("Un dia mas tarde logras alcanzar el barco de Barbanegra para intentar tu esperada venganza")
        accion6 = int(input("Tienes que tomar tu decision, 1. Disparar con los cañones de lejos  2. Acercarte a abordarlo\n"))
        #Verifica la opcion
        while accion6!=1 and accion6!=2:
            accion4 = int(input("Ingrese nuevamente la opcion: "))
            if accion6!=1 and accion6!=2:
                print("Opcion Erronea")
        print("")

        #Disparar con los cañones desde lejos}
        if accion6==1:
            print("Decidiste disparar con los cañones le das pero Barbanegra contraataca, recibes daño en el barco")
            barco = barco-20
            accion7 = int(input("Tienes que tomar tu decision, 1. Disparar al casco del barco  2. Disparar a las velas\n"))
            #Verifica la opcion
            while accion7!=1 and accion7!=2:
                accion7 = int(input("Ingrese nuevamente la opcion: "))
                if accion7!=1 and accion7!=2:
                    print("Opcion Erronea")
            print("")

            #Disparar al casco
            if accion7==1:
                print("Decidiste disparar al casco del barco, ves como el barco de Barbanegra empieza a estar dañado")

            #Disparar a las velas
            elif accion7==2:
                print("Decidiste disparar a las velas del barco, si bien le haces daño no es tan grave como te gustaria")
                print("Barbanegra te contraataca dañando tu barco")
                barco=barco-10

        #Abordar su barco
        elif accion6==2:
            print("Decidiste acercarte para abordarlo y se libra una feroz batalla")
            tripulantes = tripulantes-2
            accion7 = int(input("Tienes que tomar tu decision, 1. Explotar un barril de polvora  2. Dividirse en grupos\n"))
            #Verifica la opcion
            while accion7!=1 and accion7!=2:
                accion7 = int(input("Ingrese nuevamente la opcion: "))
                if accion7!=1 and accion7!=2:
                    print("Opcion Erronea")
            print("")

            #Explotar barril
            if accion7==1:
                print("Decidiste explotar un barril de polvora, ves como el barco de Barbanegra empieza a estar dañado pero esto te juega en contra")
                print("Varios de tus tripulantes son heridos")
                tripulantes=tripulantes-4

            #Dividirse en grupos
            elif accion7==2:
                print("Decidiste dividirte en grupos, varios de tus tripulantes agarran armas de fuego mientras que otros cargan contra los enemigos")

        #FINALES
        print("")
        #Pocos tripulantes
        if tripulantes<7:
            print("Luego de una batalla con los miembros de Barbanegra, tus fuerzas empiezan a debilitarse.")
            print("Sus fuerzas ganan terreno y logran atraparte, te hacen caminar por la borda para acabar en el fondo del mar...\n")
            print("Terminaste muerto a las puertas de tu vengaza")
            print("FINAL MALO")
            os.system("pause")
            os.system("cls")
            continue

        #Poca vida del barco
        elif barco<50:
            print("Mientras tus tripulantes estan en combate, Barbanegra aprovecha la oportunidad para destruir tu barco y empiezas a hundirte con el...\n")
            print("Terminaste hundido en el fondo del mar a las puertas de tu venganza")
            print("FINAL MALO")
            os.system("pause")
            os.system("cls")
            continue
            
        #Barco con vida y Bastantes tripulantes
        else: #tripulantes>6//barco>40
            print("Empiezas el combate con gran fuerza, los piratas de barbanegra empiezan a debilitarse poco a poco")
            print("Tu barco con gran resistencia logra soportar los potentes cañonasos del enemigo, mientras ves como tus enemigos se van reduciendo en numero")
            print("Entonces decides que es hora de ir terminando el combate")
            print("Cargando contra los piratas enemigos te deshaces de varios de ellos hasta encontrarte cara a cara con el traidor")
            print("El objetivo de tu aventura y antiguo compañero Barbanegra\n")
            #William vivo con tu tripulacion
            if opcion1==2:
                print("La pelea empieza con intensos golpes de sus espadas, cuando al fin logras arrinconarlo este pide piedad y con un momento de duda")
                print("Barbanegra aprovecha para sacar una pistola y disparar. Sientes un empujon en tu cuerpo pero no del arma, es William moviendote del camino recibiendo el daño por vos.")
                print("Con la escena de recien, ahora sin duda alguna arremetes con tu espada contra barbanegra, cumpliendo con tu venganza\n")
                print("Terminas tu venganza pero a que precio")
                print("VENGANZA FINALIZADA: MUERTE DE WILLIAM")
            
            #Sin William
            elif opcion1==1:
                print("La pelea empieza con intensos golpes de sus espadas, cuando al fin logras arrinconarlo este pide piedad pero luego de toda tu aventura, tenes que ponerle fin de una vez por todas eliminando a barbanegra")
                print("Este cae al piso por tu espada y asi cumpliendo con tu venganza\n")
                print("Terminas tu venganza al fin despues de tanto tiempo")
                print("VENGANZA FINALIZADA")
            
            print("Gracias por Jugar")#Solo aparece en los finales buenos
            os.system("pause")
            os.system("cls")
            continue
             
    #SALIR DEL JUEGO
    elif opcion == 2:            
        exit()