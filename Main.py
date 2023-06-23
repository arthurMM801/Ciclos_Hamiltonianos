from euleriano import verificaE
from hamiltoniano import verificaH
from ciclos import *

def main():
    print("Ciclo 1")
    verificaH(ciclo1)
    verificaE(ciclo1, 0)

    print("Ciclo 2")
    verificaH(ciclo2)
    verificaE(ciclo2, 0)

    print("Ciclo 3")
    verificaH(ciclo3)
    verificaE(ciclo3, 0)

    print("Ciclo 4")
    verificaH(ciclo4)
    verificaE(ciclo4, 0)

if __name__ == '__main__':
    main()