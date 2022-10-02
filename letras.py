from colorama import Back, Fore, init, Style, Cursor;
init()


def test():
    coordenadas1=[6];
    coordenadas2=[5];
    return coordenadas1, coordenadas2;




def A(coordenadas1, coordenadas2):
    
    letra=["#####","#","##","###","####"]
    
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

   

def B(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[0]);
    print(Cursor.POS(coordenadas1[0]+5, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+5, coordenadas2[0]+3)+letra[1]);   
    
def C(coordenadas1, coordenadas2):
    
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

def D(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[0]);
    print(Cursor.POS(coordenadas1[0]+5, coordenadas2[0]+1)+letra[2]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+2)+letra[2]);
    print(Cursor.POS(coordenadas1[0]+5, coordenadas2[0]+3)+letra[2]);

def E(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[0]);

def F(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[3]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);

def G(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);

def H(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);


def I(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0])+letra[3]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+4)+letra[3]);

def J(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0])+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);

def K(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+4)+letra[1]);

def L(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);   
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[0]);

def M(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[3]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+4)+letra[1]);

def N(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

def O(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

def P(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[4]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[4]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);


def Q(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+5)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+6)+letra[2]);

def R(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[4]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[4]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+4)+letra[1]);

def S(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[4]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[4]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[4]);
    

def T(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[0]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+4)+letra[1]);
    
def U(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

def V(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);


def W(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[3]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+6, coordenadas2[0]+3)+letra[1]);
    
def X(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0]+4)+letra[1]);

def Y(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+4, coordenadas2[0])+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+4)+letra[1]);

def Z(coordenadas1, coordenadas2):
    letra=["#####","#","##","###","####"]
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0])+letra[4]);
    print(Cursor.POS(coordenadas1[0]+3, coordenadas2[0]+1)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+2, coordenadas2[0]+2)+letra[1]);
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+3)+letra[1]);
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+letra[4]);

def espacio(coordenadas1, coordenadas2):
    
    
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]), "     ");
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+1),"     ");
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+2)+"     ");
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+3)+"     ");
    print(Cursor.POS(coordenadas1[0], coordenadas2[0]+4)+"     ");
    print(Cursor.POS(coordenadas1[0]+1, coordenadas2[0]+4), "     ");
    


def prueba1( nombre1, nombre2, nombre3, nombre4, nombre5):
    import msvcrt;
    import os;
    from colorama import Back, Fore, init, Style, Cursor;
    import time
    coordenadas1, coordenadas2=test()
    elemento=[]
    n= True;
    cont=5;
    while n:
        if cont == 5:
            for x in nombre1[0]:
                elemento.append(x)
            imprimir(elemento, coordenadas1, coordenadas2);
            elemento.clear()
            cont= cont-1;
            time.sleep(3)
            coordenadas1[0]= coordenadas1[0]=6
            coordenadas2[0]= coordenadas2[0]=5
            os.system("cls")
        elif cont == 4:
            for x in nombre2[0]:
                elemento.append(x)
            imprimir(elemento, coordenadas1, coordenadas2);
            elemento.clear()
            cont= cont-1;
            time.sleep(3)
            coordenadas1[0]= coordenadas1[0]=6
            coordenadas2[0]= coordenadas2[0]=5
            os.system("cls")
        elif cont == 3:
            for x in nombre3[0]:
                elemento.append(x)
            imprimir(elemento, coordenadas1, coordenadas2);
            elemento.clear()
            cont= cont-1;
            time.sleep(3)
            coordenadas1[0]= coordenadas1[0]=6
            coordenadas2[0]= coordenadas2[0]=5
            os.system("cls")
        elif cont == 2:
            for x in nombre4[0]:
                elemento.append(x)
            imprimir(elemento, coordenadas1, coordenadas2);
            elemento.clear()
            cont= cont-1;
            time.sleep(3)
            coordenadas1[0]= coordenadas1[0]=6
            coordenadas2[0]= coordenadas2[0]=5
            os.system("cls")
        elif cont == 1:
            for x in nombre5[0]:
                elemento.append(x)
            imprimir(elemento, coordenadas1, coordenadas2);
            elemento.clear()
            cont= cont-1;
            time.sleep(3)
            coordenadas1[0]= coordenadas1[0]=6
            coordenadas2[0]= coordenadas2[0]=5
            os.system("cls")
        if cont == 0:
            n=False;      

    
def imprimir(elemento, coordenadas1, coordenadas2):
    for a in elemento:
        if a == 'a': 
            A(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'b': 
            B(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+9
        elif a == 'c': 
            C(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7 
        elif a == 'd': 
            D(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+10
        elif a == 'e': 
            E(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'f': 
            F(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'g': 
            G(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'h': 
            H(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'i': 
            I(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'j': 
            J(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+8
        elif a == 'k': 
            K(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+5
        elif a == 'l': 
            L(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'm': 
            M(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+10
        elif a == 'n': 
            N(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'o': 
            O(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'p': 
            P(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+6
        elif a == 'q': 
            Q(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'r': 
            R(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+6
        elif a == 's': 
            S(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+6
        elif a == 't': 
            T(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'u': 
            U(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'v': 
            V(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'w': 
            W(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+10
        elif a == 'x': 
            X(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'y': 
            Y(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        elif a == 'z': 
            Z(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+6
        elif a == ' ':
            espacio(coordenadas1, coordenadas2)
            coordenadas1[0]=coordenadas1[0]+7
        if coordenadas1[0]>=  164:
            coordenadas2[0]= coordenadas2[0]+8
            coordenadas1[0]= coordenadas1[0]=6




















