#!/usr/bin/python3
"""
This module contains a function to divide all elements of a matrix
by a given divisor with proper input validations.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats,
                   or rows are not of the same size,
                   or div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of floats: New matrix with divided elements
        rounded to 2 decimals.
    """
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            any(not all(isinstance(el, (int, float)) for el in row)
                for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix

