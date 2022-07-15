def fib_memoization(n, table):
    if n not in table:
        table[n] = fib_memoization(n-1, table) + fib_memoization(n-2, table)
    else:
        pass
    
    return table[n]

def fib_tabulation(n, table):
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[i]


if __name__ == "__main__":
    # We define the base case using the dictionary
    tble = {0:1, 1:1}

    # Linear time O(n)
    print(fib_memoization(5, tble))
    print(fib_tabulation(5, tble))