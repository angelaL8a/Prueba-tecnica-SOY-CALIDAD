"""
Prueba técnica Soy Calidad
Fecha: Agosto 1, 2024
Autor: Angela Paola Lozano Ochoa

Este script contiene soluciones para dos ejercicios de programación:
1. Análisis de frecuencia en una matriz
2. Generación de pares de números naturales que suman a n
"""

from typing import List, Tuple


"""
    Ejercicio 1
    Se tiene una matriz nxn de enteros, crear una funcion que
    retorne un arreglo cuyo primer elemento es la cantidad de
    números que aparecen solo una vez y cuyo segundo elemento
    la cantidad de términos repetidos.
"""


def count_unique_and_repeated_numbers(matrix: List[List[int]]) -> List[int]:
    """
    Counts the number of unique and repeated numbers in a matrix.
    Args:
        matrix (list): A matrix nxn containing numbers.
    Returns:
        list: A list containing the count of unique and repeated numbers in the matrix.
    Example:
        >>> matrix = [[2, 1, 3], [4, 5, 2], [6, 6, 6]]
        >>> count_unique_and_repeated_numbers(matrix)
        [4, 2]
    In the above example, the matrix contains 4 unique numbers (1,3,4,5) and 2 repeated numbers (2,6).

    Complejidad temporal: O(n^2), donde n es la dimensión de la matriz
    Complejidad espacial: O(n^2) en el peor caso
    """
    count_elements = {}
    for row in matrix:
        for element in row:
            if element in count_elements:
                count_elements[element] += 1
            else:
                count_elements[element] = 1

    # Contar números únicos y repetidos
    unique_numbers = 0
    repeated_numbers = 0
    for element in count_elements:
        if count_elements[element] == 1:
            unique_numbers += 1
        else:
            repeated_numbers += 1
    return [unique_numbers, repeated_numbers]


"""
    Ejercicio 2
    Se tiene un número natural n, crear una funcion que retorne
    una lista de todos los pares de números naturales que sumen
    el número n. n < 10^6
"""


def find_pairs_that_sum(n: int) -> List[Tuple[int, int]]:
    """
    Finds all pairs of numbers that sum up to a given number.

    Parameters:
    n (int): The target number.

    Returns:
    list: A list of tuples, where each tuple contains a pair of numbers that sum up to `n`.

    Example:
    >>> find_pairs_sum(10)
    [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]

    Complejidad temporal: O(n)
    Complejidad espacial: O(n)
    """
    # Explicación del algoritmo:
    # Se emplea la simetría de la suma de números equidistantes menores que n.
    # Este enfoque se basa en el principio de que, para cualquier n, la suma de cada
    # par de números equidistantes respecto a los extremos de la secuencia de números
    # naturales menores que n será igual a n. Matemáticamente, si consideramos la
    # secuencia {1, 2, ..., n-1}, cualquier par (a, b) tal que a + b = n puede
    # identificarse observando que a y b son elementos simétricos respecto al punto
    # medio de n. Este procedimiento es válido ya que a = k y b = n - k para k en el
    # intervalo [1, n-1], resultando en (1, n-1), (2, n-2), ..., (⌊n/2⌋, n - ⌊n/2⌋).
    return [(i, n - i) for i in range(1, n // 2 + 1)]


# Ejemplos de uso
if __name__ == "__main__":
    # Ejercicio 1
    matriz1 = [[2, 2], [2, 2]]
    matriz2 = [[2, 1, 3], [4, 5, 2], [6, 6, 6]]

    print("Ejercicio 1:")
    print(f"Resultado para {matriz1}: {
          count_unique_and_repeated_numbers(matriz1)}")
    print(f"Resultado para {matriz2}: {
          count_unique_and_repeated_numbers(matriz2)}")

    # Ejercicio 2
    n = 5
    print("\nEjercicio 2:")
    print(f"Pares que suman {n}: {find_pairs_that_sum(n)}")
