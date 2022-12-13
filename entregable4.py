from typing import TextIO
import sys


Solution = tuple[int, int, int]  # l, r, coste


def read_data(f: TextIO) -> list[int]:
    l = []
    for linea in f:
        l.append(int(linea))
    return l


def process(v: list[int]) -> Solution:
    picos = calcula_picos(v)
    sol = (0,1,0)
    return calcula_valle(picos, v)


def calcula_picos(v: list[int]) -> list[int]:
    creciendo = True
    aux = 0
    picos = []

    for i in range(1, len(v), 1):
        if list[i] > list[aux]:
            creciendo = True
        else:
            if creciendo:
                picos.append(i-1)
                creciendo = False
        aux = i

    if creciendo:
        picos.append(len(v)-1)

    return picos


def calcula_valle(auxI: int, auxD: int, v: list[int]) -> Solution:
    return None


def show_results(sol: Solution):
    print(sol[0] + " " + sol[1] + " " + sol[2])


if __name__ == "__main__":
    v = read_data(sys.stdin)
    sol = process(v)
    show_results(sol)
