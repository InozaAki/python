


def grafico():
    import os
    from colorama import Fore, init, Back, Cursor, Style;
    init()
    os.system("mode con: cols=175 lines=63")
    coords=[1,2,3,80]
    n=True
    while n:
        print(Cursor.POS(coords[0],coords[1])+Fore.CYAN+"▀"*80+Fore.RESET);
        print(Cursor.POS(coords[0],coords[2])+Fore.CYAN+"▀"+Fore.RESET)
        print(Cursor.POS(coords[3],coords[2])+Fore.CYAN+"▀"+Fore.RESET)
        coords[2]=coords[2]+1;
        if coords[2] == 30:
            coords[2]=coords[2]+1;
            print(Cursor.POS(coords[0],coords[3])+Fore.CYAN+"▀"*80+Fore.RESET);
            n= False
            
    
   