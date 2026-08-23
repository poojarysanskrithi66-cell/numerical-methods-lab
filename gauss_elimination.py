def gauss_elimination(A, b):
    n = len(A)
    
    # Build the augmented matrix [A | b]
    for i in range(n):
        A[i].append(b[i])

    # Forward elimination: make everything below the diagonal zero
    for i in range(n):
        # Pivoting: avoid dividing by zero, improve stability
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    break

        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] -= ratio * A[i][k]

    # Back substitution: solve from the last row upward
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


if __name__ == "__main__":
    # Example system:
    # 2x + y - z = 8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3
    A = [[2, 1, -1],
         [-3, -1, 2],
         [-2, 1, 2]]
    b = [8, -11, -3]

    solution = gauss_elimination(A, b)
    print("Solution:", solution)