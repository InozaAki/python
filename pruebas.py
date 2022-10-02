def test3():
    from colorama import init, Back, Cursor;
    import msvcrt;
    import os;
    from escribir import prueba;
    init();
    coor=[5, 4]
    flechas = [4]
    listarch=[]
    s = 0;
    for x in os.listdir():
        ext = x.split('.');
        if ext[-1] == 'txt':
            listarch.append(x);
    for i in range(len(listarch)-0):
        print(Cursor.POS(coor[0], coor[1]) + listarch[i]);
        coor[1] = coor[1] + 1;
    print(Cursor.POS(1, flechas[0]) + ">>>");
    while True:
        bot = msvcrt.getch();
        os.system("cls");
        if bot == b'P':    #Abajo
            s = s + 1;
            flechas[0] = flechas[0] + 1;
            files();
            print(Cursor.POS(1, flechas[0]) + ">>>");

        elif bot == b'H':  #Arriba
            s = s - 1;
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
        if s < 0:
            s = len(listarch)-1;
        elif s > len(listarch)-1:
            s = 0
        if bot == b'\r':
            s == len(listarch)-1;
            n = listarch[s];
            prueba(n);
            break;
    


def files():
    from colorama import Cursor, init;
    init();
    import os;
    coor=[5,4]
    listarch = [];
    for x in os.listdir():
        ext = x.split('.');
        if ext[-1] == 'txt':
            listarch.append(x);
    for i in range(len(listarch)-0):
        print(Cursor.POS(coor[0], coor[1]) + listarch[i]);
        coor[1] = coor[1] + 1; 

test3();