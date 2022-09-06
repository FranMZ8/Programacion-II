//Estudiante: Franco Agustin Muñoz Cartagena
//Proyecto Final BLACKJACK
//Mail: franmu8484@gmail.com

#include <iostream>
#include <string>
#include <ctime>

using namespace std;

//Prototipo de Funciones

//Funcion que muestra el menu principal al entrar al programa
void menuPrincipal();
//Funcion que muestra las reglas del juego
void reglas();
//Funcion para pedir una carta para el Usuario
int pedirCarta();
//Funcion que le da una carta al Crupier
int pedirCartaCrupier();
//Funcion que le da a una carta el tipo del cual es (ej carta de diamantes)
string formaCarta();

int main()
{
    srand(time(0));
    int opcion = 0;
    while (opcion!=3)
    {
        int record = 0;
        int cantVidas = 3;//Para cambiar la cantidad de vidas solo cambiar esta variable
        menuPrincipal();
        do
        {
            cin >> opcion;
            cout << "\n";
            system("cls");
            
            //REGLAS
            if (opcion == 1)
            {
                reglas();
            }
            
            //JUGAR
            else if (opcion == 2)
            {
                //Variables
                    //Usuario
                int valorTotalUsuario = 0;
                int valorDeCartaUsuario;
                int cantCartasUsuario = 0;
                    //Programa
                int quiereCarta=4;
                int quiereJugar = 4;
                    //Crupier
                int valorDeCartaCrupier;
                int valorTotalCrupier=0;

                cout << "\nEMPIEZA EL JUEGO\n" << endl;
                system("pause");
                cout << "\n";
                while (true)
                {            
                    //Le da una carta a el usuario
                    valorDeCartaUsuario = pedirCarta();
                    cantCartasUsuario++;         
                    
                    //Le da una carta a el Crupier
                    //está obligado a pedir carta siempre que su puntuación sume 16 o menos, y 
                    //obligado a plantarse si suma 17 o más
                    while (valorTotalCrupier <= 16)
                    {
                        valorDeCartaCrupier = pedirCartaCrupier();
                        //los Ases valen 11 mientras no se pase de 21, y 1 en caso contrario
                        if ((valorDeCartaCrupier==11) && (valorDeCartaCrupier + valorTotalCrupier > 21))
                        {
                            valorDeCartaCrupier = 1;
                        }
                        valorTotalCrupier = valorTotalCrupier + valorDeCartaCrupier;
                    }

                    //Hace que el usuario elija el valor del As
                    if (valorDeCartaUsuario == 11)
                    {
                        cout << "Elija que valor quiere que tome su As (1 o 11): ";
                        //Verifica que el usuario ingrese correctamente el valor del As (1 o 11) 
                        do
                        {
                            cin >> valorDeCartaUsuario;
                            switch (valorDeCartaUsuario)
                            {
                            case 1: cout << "Elegiste que el As tome el valor 1" << endl; break;
                            case 11: cout << "Elegiste que el As tome el valor 11" << endl; break;
                            default: cout << "El valor ingresado es incorrecto, elija nuevamente" << endl;
                            }
                        } while (valorDeCartaUsuario != 1 && valorDeCartaUsuario != 11);

                    }

                    cout << "El valor de tu carta es " << valorDeCartaUsuario << endl;
                    valorTotalUsuario = valorDeCartaUsuario + valorTotalUsuario;
                    cout << "El valor total de tus cartas es " << valorTotalUsuario <<"\n"<< endl;
                   
                    if (cantCartasUsuario>=2)
                    {
                        //Pregunta si el usuario quiere plantarse con el valor que tiene o pedir otra carta
                        if ((quiereCarta != 0) && (valorTotalUsuario!=21) && (valorTotalUsuario<21))
                        {
                            cout << "¿Quiere pedir otra carta o plantarse? (0=Plantarse, 1=Pedir) ";
                            do
                            {
                                cin >> quiereCarta;
                                if ((quiereCarta > 1) || (quiereCarta < 0))
                                {
                                    cout << "Ingrese nuevamente el numero (0=Plantarse, 1=Pedir): " << endl;
                                }

                            } while ((quiereCarta > 1) || (quiereCarta < 0));
                        }
                        
                        //Entra a este if si el juego termina (valor total >=21 o se planto)
                        if ((quiereCarta == 0) || (valorTotalUsuario >= 21))
                        {
                            //Ve si el valor total del usuario se paso de 21
                            if (valorTotalUsuario > 21)
                            {                          
                                cout << "Se termino el juego... PERDISTE" << endl;
                                cout << "Te pasaste de 21\n" << endl;
                                cantVidas--;                              
                            }
                            //Si llega a 21
                            else if (valorTotalUsuario == 21)
                            {
                                cout << "Se termino el juego... GANASTE" << endl;
                                cout << "Juntaste 21\n" << endl;
                                record++;
                            }
                            //Compara el valor del usuario y del Crupier
                            else if (quiereCarta == 0)
                            {                               
                                cout << "El valor de cartas del Crupier es " << valorTotalCrupier << endl;
                                cout << "Tu valor de cartas es " << valorTotalUsuario << endl;
                                //VALOR DE USUARIO MAYOR A CRUPIER
                                if (valorTotalUsuario > valorTotalCrupier)
                                {
                                    cout << "Se termino el juego... GANASTE\n" << endl;
                                    record++;                                   
                                }
                                //VALOR DE CRUPIER MAYOR A USUARIO
                                else if (valorTotalUsuario < valorTotalCrupier)
                                {
                                    if (valorTotalCrupier < 22)
                                    {
                                        cout << "Se termino el juego... PERDISTE\n" << endl;
                                        cantVidas--;
                                    }
                                    else
                                    {
                                        cout << "Se termino el juego... GANASTE" << endl;
                                        cout << "El Crupier se paso de 21\n" << endl;
                                        record++;
                                    }
                                }
                                //EMPATE no se puede empatar con 21
                                else
                                {
                                    cout << "Se termino el juego... EMPATASTE CON EL CRUPIER\n" << endl;
                                }
                            }
                            
                            //Pregunta si quiere jugar otra vez
                            if (cantVidas > 0)
                            {
                                cout << "Tu cantidad de vidas es: " << cantVidas << endl;
                                cout << "Tu record es: " << record << endl;
                                cout << "Quiere jugar otra vez?" << endl;
                                cout<<"(0=Salir Al Menu Principal, 1=Jugar Otra Vez): ";
                                //Verifica que quiereJugar sea 0 o 1
                                do
                                {
                                    cin >> quiereJugar;
                                    cout << "\n";
                                    if ((quiereJugar > 1) || (quiereJugar < 0))
                                    {
                                        cout << "Ingrese nuevamente la opcion (0=Salir Al Menu Principal, 1=Jugar Otra Vez): " << endl;
                                    }
                                } while ((quiereJugar > 1) || (quiereJugar < 0));
                                //Volver Al Menu Principal
                                if (quiereJugar == 0)
                                {
                                    system("cls");
                                    break;
                                }
                                //Jugar Otra Vez
                                else if (quiereJugar == 1)
                                {
                                    //Restaura todas las variables de jugar a su inicio 
                                    valorTotalUsuario = 0;
                                    valorDeCartaUsuario=0;
                                    cantCartasUsuario = 0;
                                    quiereCarta = 4;
                                    quiereJugar = 4;
                                    valorDeCartaCrupier=0;
                                    valorTotalCrupier = 0;
                                    system("cls");
                                }
                            }
                            //Se quedo sin vidas
                            else
                            {
                                cout << "Te quedaste sin Vidas\n" << endl;
                                system("pause");
                                system("cls");
                                break;
                            }
                        }                                                                                      
                    }
                }//termina while true
            }
            
            //SALIR DEL PROGRAMA
            else if (opcion == 3)
            {
                cout << "\nGracias por Jugar" << endl;
            }
            
            //OPCION INCORRECTA
            else 
            {
                cout << "\nLa opcion es incorrecta, Ingresela nuevamente (1.Reglas 2.Jugar 3.Salir) \n" << endl;
            }
        } while ((opcion != 1) && (opcion != 2) && (opcion != 3));
    }
}

//Funcion que muestra el menu principal al entrar al programa
void menuPrincipal()
{
    cout << "Bienvenido al BlackJack\n";
    cout << "Elija una opcion\n";
    cout << "1. Reglas" << endl;
    cout << "2. Jugar" << endl;
    cout << "3. Salir del Juego\n" << endl;
}

//Funcion que muestra las reglas del juego
void reglas()
{
    cout << "REGLAS" << endl;
    cout <<"-El Blackjack es un juego de cartas que consiste en sumar un valor lo mas proximo a 21"<<endl;
    cout <<"-Se reparten dos cartas a el jugador" << endl;
    cout <<"-Las cartas numericas suman su valor, el As vale 11 o 1(a eleccion) y las figuras valen 10"<< endl;
    cout <<"-Usted puede elegir si pedir carta o plantarse, gana el que este mas cerca de 21" << endl;
    cout << "-Una pista, el Crupier si o si tiene que sumar mas de 16" << endl;
    cout <<"-A lo largo del juego se ira contando la cantidad de veces que gana para poner su record"<< endl;
    cout <<"-Tendra una cantidad de 3 oportunidades para perder y seguir intentando alargar su record\n" << endl;
    system("pause");
    system("cls");
}
   
//Funcion para pedir una carta para el Usuario
int pedirCarta()
{
    int aleatorio1=0;
    //Genera el numero aleatorio entre 1 y 13
    aleatorio1 = rand() % 13 + 1;
    
    int valorCarta=0;
    //13 cartas distintas
    // numAleatorio = carta
    //1 = 2 / 2 = 3 / 3=4 / 4=5 / 5=6 / 6=7 / 7=8 / 8=9 / 9=10 
    // 10 = j / 11=Q / 12=K / 13=A
    switch (aleatorio1)
    {
    case 1: cout << "Tu carta es el 2 de " << formaCarta() << endl; valorCarta = 2; break;
    case 2:cout << "Tu carta es el 3 de " << formaCarta() << endl; valorCarta = 3; break;
    case 3: cout << "Tu carta es el 4 de " << formaCarta() << endl; valorCarta = 4; break;
    case 4: cout << "Tu carta es el 5 de " << formaCarta() << endl; valorCarta = 5; break;
    case 5: cout << "Tu carta es el 6 de " << formaCarta() << endl; valorCarta = 6; break;
    case 6: cout << "Tu carta es el 7 de " << formaCarta() << endl; valorCarta = 7; break;
    case 7: cout << "Tu carta es el 8 de " << formaCarta() << endl; valorCarta = 8; break;
    case 8: cout << "Tu carta es el 9 de " << formaCarta() << endl; valorCarta = 9; break;
    case 9: cout << "Tu carta es el 10 de " << formaCarta() << endl; valorCarta = 10; break;
    case 10: cout << "Tu carta es el Rey(K) de " << formaCarta() << endl; valorCarta = 10; break;
    case 11: cout << "Tu carta es la Jota(J) de " << formaCarta() << endl; valorCarta = 10; break;
    case 12: cout << "Tu carta es la Reina(Q) de " << formaCarta() << endl; valorCarta = 10; break;
    case 13: cout << "Tu carta es el As(A) de " << formaCarta() << endl; valorCarta = 11; break;
    }
    return valorCarta;
}

//Funcion que le da una carta al Crupier
int pedirCartaCrupier()
{
    int aleatorio1 = 0;
    //Genera el numero aleatorio entre 1 y 13
    aleatorio1 = rand() % 13 + 1;

    int valorCarta = 0;
    //13 cartas distintas
    // numAleatorio = carta
    //1 = 2 / 2 = 3 / 3=4 / 4=5 / 5=6 / 6=7 / 7=8 / 8=9 / 9=10 
    // 10 = j / 11=Q / 12=K / 13=A
    switch (aleatorio1)
    {
    case 1: valorCarta = 2; break;
    case 2:valorCarta = 3; break;
    case 3: valorCarta = 4; break;
    case 4: valorCarta = 5; break;
    case 5: valorCarta = 6; break;
    case 6: valorCarta = 7; break;
    case 7: valorCarta = 8; break;
    case 8: valorCarta = 9; break;
    case 9: valorCarta = 10; break;
    case 10: valorCarta = 10; break;
    case 11: valorCarta = 10; break;
    case 12: valorCarta = 10; break;
    case 13: valorCarta = 11; break;
    }
    return valorCarta;
}

//Funcion que le da a una carta el tipo del cual es (ej carta de diamantes)
string formaCarta()
{
    int aleatorio2=0;
    //Genera el numero aleatorio entre 1 y 4
    aleatorio2 = rand()%4+1;
    
    string cartaEs[4] = {"Corazones", "Treboles", "Picas", "Diamantes"};
    //Verifica que tipo de carta es segun el numero aleatorio
    switch (aleatorio2)
    {
    case 1: return cartaEs[0]; break;
    case 2: return cartaEs[1]; break;
    case 3: return cartaEs[2]; break;
    case 4: return cartaEs[3]; break;
    }
}
