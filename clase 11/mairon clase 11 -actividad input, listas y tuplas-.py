print("EJERCICIO DE INPUT, LISTAS Y TUPLAS")
print("Ingresa 10 numeros enteros:")
uno=int(input("primero: "))
dos=int(input("segundo: "))       
tre=int(input("tercero: "))
cua=int(input("cuarto: "))
cin=int(input("quinto: "))
sei=int(input("sexto: "))
sie=int(input("septimo: "))
och=int(input("octavo: "))
nue=int(input("noveno: "))
die=int(input("decimo: "))
numeros=[uno,dos,tre,cua,cin,sei,sie,och,nue,die]
print(f"La lista de numeros es: {numeros}")
num1=(numeros[0],numeros[0]**2)
num2=(numeros[1],numeros[1]**2)
num3=(numeros[2],numeros[2]**2)
num4=(numeros[3],numeros[3]**2)
num5=(numeros[4],numeros[4]**2)
num6=(numeros[5],numeros[5]**2)
num7=(numeros[6],numeros[6]**2)
num8=(numeros[7],numeros[7]**2)
num9=(numeros[8],numeros[8]**2)
num10=(numeros[9],numeros[9]**2)
tupla=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
print(f"Los numeros y su cuadrado son: {tupla}")
suma=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]+numeros[5]+numeros[6]+numeros[7]+numeros[8]+numeros[9]
opmt=(suma/10,suma*2,(suma/10)/2)
print(f"la suma de todos los numeros da: {suma}\nEl promedio de todos da: {opmt[0]}\nEl doble de la suma es: {opmt[1]}\nLa mitad del promedio de los numeros es: {opmt[2]}")
opmtd=[((numeros[4]+numeros[2])*numeros[7])/numeros[1],(numeros[3]*numeros[5])-(numeros[9]*numeros[6]),(numeros[1]**numeros[9])-(numeros[2]+numeros[3]+numeros[9])]
print(f"Algunas operaciones con los numeros:\nPrimera: {numeros[4]}+{numeros[2]}*{numeros[7]}/{numeros[1]} Es igual a: {opmtd[0]}\nSegundo: {numeros[3]}*{numeros[5]}-{numeros[9]}*{numeros[6]} Es igual a: {opmtd[1]}\nTercero: {numeros[1]}**{numeros[9]}-{numeros[2]}+{numeros[3]}+{numeros[9]} Es igual a: {opmtd[2]}")