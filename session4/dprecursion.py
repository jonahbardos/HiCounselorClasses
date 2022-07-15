def solve_recursion(m, w, v, n):
 
    # base cases 
    if n == 0 or m == 0:
        return 0
    
    # The given item CANNOT fit inside the KNAPSACK
    # If the weight is greater than the capacity we dont include in our knapsack

    if w[n - 1] > m:
        return solve_recursion(m, w, v, n-1)

    # Here we have 2 options. We can either take or not take
    else:
        n_included = v[n-1] + solve_recursion(m - w[n - 1], w, v, n-1)

        n_excluded = solve_recursion(m, w, v, n-1)

        return max(n_included, n_excluded)


if __name__ == "__main__":
    weights = [4, 2, 3]
    values = [10, 4, 7]
    n = 3
    capacity = 5

    print(solve_recursion(capacity, weights, values, n))