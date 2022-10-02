def prueba(n):
    import time
    import msvcrt
    import os;
    from colorama import Fore, Back, init, Cursor;
    init();
    lista2=[];
    lista=[];
    usos=30;
    cont=30;
    x = True;
    while x == True:
        os.system("cls")
        print("|====|" + n + "|====|");
        print("Presiona ENTER al terminar de escribir");
        if (len(lista)<cont):
            lista.append(ord(msvcrt.getch()))
            for z in range(len(lista)):
                y="".join(chr(lista[z]));
                print(y ,end="");
            esc=[salir for salir in lista if salir == 13]
            borr=[eraser for eraser in lista if eraser == 8]
            usos= usos-1;
            if (len(borr)==1):
                lista.pop(-1);
                lista.pop(-1);
                usos= usos+1;
            if (len(esc)==1):
                x= False;
            if (len(lista)>=cont):
                usos=cont
        elif (len(lista)>=cont):
            for p in range(len(lista2)):
                t="".join(chr(lista2[p]));
                print(t ,end="");
            lista2.append(ord(msvcrt.getch()))
            esc=[salir for salir in lista2 if salir == 13]
            borr=[eraser for eraser in lista2 if eraser == 8]
            usos= usos-1;  
            #time.sleep(.1);
            if (len(lista2)>0):
                if (len(borr)==1):
                    lista2.pop(-1);
                    lista2.pop(-1);
                    usos= usos+1;
            if (len(lista2)==0):
                    lista.pop(-1);
                    usos= usos+1;
            if (len(esc)==1):
                lista.extend(lista2)
                lista2.clear()
                x= False;
            if (len(lista2)>=cont):
                lista.extend(lista2)
                lista2.clear()
                usos=cont
    print("¿Deseas guardar la informacion insertada?");
    info=int(input("1.Si 2.No    "));

    if info==1:
        for x in range(len(lista)):
            l= "".join(chr(lista[x]));
            arch = open(n, mode = "a", encoding="utf-8");
            arch.writelines(l);
            arch.close;
    else:
        return;
    os.system("cls");
    print("|===|" + n + "|===|")
    print("Contenido del archivo: ")
    print("#| ");
    arch = open(n, mode='r');
    leer = arch.readlines();
    cont = 0;
    for linea in leer:
        cont = cont + 1;
        print(cont, linea);
    arch.close;
    input();