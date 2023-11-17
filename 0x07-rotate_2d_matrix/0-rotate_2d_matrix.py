#!/usr/bin/python3
"""Rotate 2D Matrix Module."""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return '\n'.join(str(row) for row in matrix)
