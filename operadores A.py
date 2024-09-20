print("Act 9 clases v2")
print("Nicolas Medina MAT: 22308051281259")
# zona de clases 

class operadores1259:
    # zona de funciones
    def sum1259(self,N,M,):
        s1259=N+M
        print(f"El resultado de su suma es de: {N} + {M} = {s1259}")

    def res1259(self,N,M,):
        s1259=N-M
        print(f"El resultado de su resta es de: {N} - {M} = {s1259}")

    def mul1259(self,N,M,):
        s1259=N*M
        print(f"El resultado de su multiplicacion es de: {N} x {M} = {s1259}")

    def div1259(self,N,M,):
        s1259=N/M
        print(f"El resultado de su divicion es de: {N} / {M} = {s1259}")

    def modu1259(self,N,M,):
        s1259=N%M
        print(f"El resultado de su modulo es de: {N} % {M} = {s1259}")

    def exp1259(self,N,M,):
        s1259=N**M
        print(f"El resultado de su exponente es de: {N} xx {M} = {s1259}")

    def cos1259(self,N,M,):
        s1259=N//M
        print(f"El resultado de su cociente es de: {N} // {M} = {s1259}")



# zona de creacion del objeto
operanico=operadores1259()


# zona de uso de objetos 
print("")
print(" -Funcion suma- ")
operanico.sum1259(5,8)

print("")
print(" -Funcion resta- ")
operanico.res1259(5,8)

print("")
print(" -Funcion multiplicacion- ")
operanico.mul1259(5,8)

print("")
print(" -Funcion divicion- ")
operanico.div1259(5,8)

print("")
print(" -Funcion Modulo- ")
operanico.modu1259(5,8)

print("")
print(" -Funcion Exponente- ")
operanico.exp1259(5,8)

print("")
print(" -Funcion Cociente- ")
operanico.cos1259(5,8)