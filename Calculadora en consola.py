# Hecho por: Gary Omar Nova Mamani
sw = True
Rojo='\003[1;31m'
Verde='\003[1;32m'
blanco='\003[1;30m'
while sw:
    print('\033[1;31m','Ingrese el primer numero: ',end=' ')
    n1 = int(input('\033[1;30m'))
    print('\033[1;31m','Ingrese el segundo numero: ',end=' ')
    n2 = int(input('\033[1;30m'))
    sw1=True
    while sw1:
        print('\033[1;32m',end='')
        print('==================Calculadora====================\n'
              '1. Sumar\n'
              '2. Resta\n'
              '3. Multiplicar\n'
              '4. Dividir\n'
              '5. Elegir otros numeros\n'
              '6. Salir\n'
              '=================================================')
        print('\033[1;31m')
        print('Selecciona una opcion: ')
        opcion = int(input('\033[1;30m'))
        if opcion == 1:
            print('Suma : \n',n1,'+',n2,' = ',(n1+n2))
        elif opcion == 2:
            print('Resta : \n',n1,'-',n2,' = ',(n1-n2))
        elif opcion == 3:
            print('Multiplicacion : \n',n1,'x',n2,' = ',(n1*n2))
        elif opcion == 4:
            print('Divicion : \n',n1,'/',n2,' = ',(n1/n2))
        elif opcion == 5:
            sw1 = False
        elif opcion == 6:
            sw1=False
            sw=False
else:
    print('Gracias ...!!!')
