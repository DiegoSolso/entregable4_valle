from typing import TextIO
import sys


Solution = tuple[int, int, int]  # l, r, coste


def read_data(f: TextIO) -> list[int]:
    lista = []
    for linea in f:
        if linea.strip():
            n = int(linea)
            lista.append(n)
    return lista


def process(v: list[int]) -> Solution:
    picos = calcula_picos(v)
    picos = limpia_picos (picos, v)
    solucion = (0, 1, 0)
    for i in range (1, len(picos), 1):
        aux = calcula_valle(i-1, i, v)
        if aux[2] > solucion[2]:
            solucion = aux

    return solucion


def calcula_picos(v: list[int]) -> list[int]:
    creciendo = True
    aux = 0
    picos = []

    for i in range(1, len(v), 1):
        if v[i] > v[aux]:
            creciendo = True
        else:
            if creciendo:
                picos.append(i-1)
                creciendo = False
        aux = i

    if creciendo:
        picos.append(len(v)-1)

    return picos


def limpia_picos(picos: list[int], v: list[int]) -> list[int]:
    picos_limpios = [picos[0]]
    aux = 0
    for i in range(1, len(picos), 1):
        if v[picos[i]] >= v[picos[aux]]:
            picos_limpios.append(picos[i])
            aux = i

    while aux != len(picos)-1:
        maximo = aux + 1
        for i in range(aux + 2, len(picos), 1):
            if v[picos[i]] > v[picos[maximo]]:
                maximo = i
        picos_limpios.append(maximo)
        aux = maximo

    return picos_limpios


def calcula_valle(l: int, r: int, v: list[int]) -> Solution:
    l_mayor = True
    tam = 0
    min = r

    if v[r] > v[l]:
        l_mayor = False
        min = l

    if l_mayor:
        while v[l] > v[r]:
            l += 1
        l -= 1
    else:
        while v[r] > v[l]:
            r -= 1
        r += 1

    for i in range(l + 1, r, 1):
        tam += v[min] - v[i]

    return l, r, tam


def show_results(sol: Solution):
    print(f"{sol[0]} {sol[1]} {sol[2]}")


if __name__ == "__main__":
    v = read_data(sys.stdin)
    sol = process(v)
    show_results(sol)
