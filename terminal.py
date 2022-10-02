

def pruebas2(): 
    import os
    import letras;
    import casifinal;
    frase=['cervantes cervera oscar javier' ,'corona soltero david de jesus' ,'de alba velarde christian moises' ,'garcia garcia yolanda estefania','espinoza espinoza axel antonio']
    nombre1=[nombre for nombre in frase if nombre.startswith("cervantes")]
    nombre2=[nombre for nombre in frase if nombre.startswith("corona")]
    nombre3=[nombre for nombre in frase if nombre.startswith("de")]
    nombre4=[nombre for nombre in frase if nombre.startswith("garcia")]
    nombre5=[nombre for nombre in frase if nombre.startswith("espinoza")]
    print(nombre1, nombre2, nombre3, nombre4, nombre5)
    os.system("mode con: cols=175 lines=63")
    letras.prueba1( nombre1, nombre2, nombre3, nombre4, nombre5)
    casifinal.volver()
    

