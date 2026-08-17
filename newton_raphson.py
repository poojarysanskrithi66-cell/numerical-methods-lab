def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None

        x_new = x - fx / dfx
        print(f"Iteration {i+1}: x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    print("Max iterations reached without convergence.")
    return x


if __name__ == "__main__":
    # Example: f(x) = x^3 - x - 2
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1
    root = newton_raphson(f, df, 1.5)
    print(f"\nApproximate root: {root:.6f}")
