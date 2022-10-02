'''
| Practica 9 |
Fundamentos de Programacion | Sección 6
Equipo 2 
CERVANTES CERVERA OSCAR JAVIER
CORONA SOLTERO DAVID DE JESUS
DE ALBA VELARDE CHRISTIAN MOISES
ESPINOSA ESPINOZA AXEL ANTONIO
GARCIA GARCIA YOLANDA ESTEFANIA
'''

def na(coor2):
    import os;
    import msvcrt;
    from colorama import Cursor, Back, init;
    import grafico;
    init();
    grafico.grafico()
    print(Cursor.POS(coor2[0],coor2[1]),"¿Quieres crear un archivo nuevo");
    
    opc=["Enter = Continuar","Esc = Regresar"]
    
    print(Cursor.POS(coor2[0],coor2[1]+1)+opc[0]);
    print(Cursor.POS(coor2[0],coor2[1]+2)+opc[1]);

    while True:
        bot=msvcrt.getch();
        os.system("cls")
        if bot == b'\r':
            con(coor2)
        elif bot == b'\x1b':
            menu();

def volver():
    import os;
    import msvcrt;
    from colorama import Cursor, Back, init;
    init();
    coor3=[3,3]
    print(Cursor.POS(coor3[0],coor3[1]),"Presione ESC para regresar ");
    while True:
        bot=msvcrt.getch();
        os.system("cls")
        if bot == b'\x1b':
            menu();
        else:
            print(Cursor.POS(coor3[0],coor3[1]),"tecla no valida")

def con(coor2):
    import os;
    import msvcrt;
    from colorama import Cursor, init, Back;
    import grafico;
    init();
    grafico.grafico()
    print(Cursor.POS(coor2[0], coor2[1]),"|==Archivo nuevo==|");
    print(Cursor.POS(coor2[0], coor2[1]+1),"|= ¿Que nombre le quieres poner al archivo? =|");
    print(Cursor.POS(coor2[0], coor2[1]+2),">>>  ", end="");
    opc=["Enter = Continuar","Esc = Regresar"]
    
    t=True;
    while t:
        nom = input();
        if nom:
            os.system("cls");
            grafico.grafico()
            print(Cursor.POS(coor2[0],coor2[1]+1),"se creara un archivo llamado", nom+".txt");
            print(Cursor.POS(coor2[0],coor2[1]+2),"¿Deseas continuar?")
            print(Cursor.POS(coor2[0],coor2[1]+3)+opc[0]);
            print(Cursor.POS(coor2[0],coor2[1]+4)+opc[1]);

            while True:
                bot=msvcrt.getch();
                os.system("cls")
                grafico.grafico()
                if bot == b'\r':
                    arch = open(nom +'.txt',"x");
                    arch.close();
                    os.system("cls");
                    grafico.grafico()
                    print(Cursor.POS(coor2[0],coor2[1]),"se ha creado el archivo", nom+".txt")
                    print(Cursor.POS(coor2[0],coor2[1]+1),"volviendo al menu")
                    input("presione Enter para continuar")
                    menu();
                elif bot == b'\x1b':
                    pass
    
    
    
def ea():
    import os;
    import msvcrt;
    from colorama import init, Back, Cursor;
    init();

    coor=[5,4]
    flechas = [4]
    lista=[]

    for x in os.listdir():
        ext = x.split('.');
        if ext[-1] == 'txt':
            lista.append(x);
    for i in range(len(lista)-0):
        print(Cursor.POS(coor[0], coor[1]) + lista[i]);
        coor[1] = coor[1] + 1;

    print(Cursor.POS(1, flechas[0]) + ">>>");
    while True:
        bot = msvcrt.getch();
        os.system("cls");

        if bot == b'P':    #Abajo
            flechas[0] = flechas[0] + 1;
            files();
            print(Cursor.POS(1, flechas[0]) + ">>>");

        elif bot == b'H':  #Arriba
            flechas[0]= flechas[0] - 1;
            print(Cursor.POS(1, flechas[0]) + ">>>");
            files();

        if flechas[0] == 3:
            flechas[0] = coor[1] - 1;
            os.system("cls")
            print(Cursor.POS(1, flechas[0]) + ">>>");
            files();

        elif flechas[0] == coor[1]:
            flechas[0] = 4;
            os.system("cls");
            print(Cursor.POS(1, flechas[0]) + ">>>");
            files();
   
        elif bot == b'\r':
            print(flechas[0]);
                
def menu():
    import msvcrt;
    import os;
    from colorama import Fore, init, Back, Cursor, Style;
    import terminal;
    import grafico;
    
    init(autoreset = True);
    os.system("mode con: cols=175 lines=63")
    coor=[5,5]
    coor2=[3,3]
    s= 3 
    
    opc=["1. Nuevo archivo de texto", "2. Mostrar/Editar archivo existente","3. Creditos ", "4. Salir"];
    grafico.grafico()
    print(Cursor.POS(coor[0], coor[1]) + Back.BLUE + opc[0] + Back.RESET);
    print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
    print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
    print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
    

    while True:

        print(Cursor.POS(coor2[0],coor2[1])+ Fore.CYAN +"Use las flechas arriba y abajo para moverse en el menu"+ Fore.RESET )
        print(Cursor.POS(coor2[0],coor2[1]+1)+ Fore.CYAN +"presione ENTER para acceder a la opcion"+ Fore.RESET)
        
        bot=msvcrt.getch();
        os.system("cls")
        if bot == b'P': #abajo
            s = s + 1
            
            if s == 4:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0]);
                print(Cursor.POS(coor[0], coor[1]+1)+ Back.BLUE + opc[1] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                

            elif s == 5:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0]);
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + Back.BLUE + opc[2] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                

            elif s == 6:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0] );
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + Back.BLUE + opc[3] + Back.RESET);
                

            elif s == 7:
                s= 3
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1])+ Back.BLUE + opc[0] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                
            
        elif bot == b'H': #arriba
            s = s - 1
            if s == 2:
                s=6
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0]);
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + Back.BLUE + opc[3] + Back.RESET);
                

            elif s == 3:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + Back.BLUE + opc[0] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                
            elif s == 4:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0]);
                print(Cursor.POS(coor[0], coor[1]+1) + Back.BLUE + opc[1] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+2) + opc[2]);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                
            elif s == 5:
                grafico.grafico()
                print(Cursor.POS(coor[0], coor[1]) + opc[0]);
                print(Cursor.POS(coor[0], coor[1]+1) + opc[1]);
                print(Cursor.POS(coor[0], coor[1]+2) + Back.BLUE + opc[2] + Back.RESET);
                print(Cursor.POS(coor[0], coor[1]+3) + opc[3]);
                    
        elif bot == b'\r':
            if s == 3 or s == 7:
                na(coor2)
            elif s == 4:
                ea()
            elif s == 5:
                terminal.pruebas2()
            elif s == 6 or s == 2:
                return
        else:
            print(Cursor.POS(coor2[0],coor2[1]+2)+ Fore.RED +"pofavor use las teclas indicadas"+ Fore.RESET)
            

def files():
    from colorama import Cursor, init;
    init();
    import os;
    coor=[5,4]
    lista = [];
    for x in os.listdir():
        ext = x.split('.');
        if ext[-1] == 'txt':
            lista.append(x);
    for i in range(len(lista)-0):
        print(Cursor.POS(coor[0], coor[1]) + lista[i]);
        coor[1] = coor[1] + 1; 





menu();
