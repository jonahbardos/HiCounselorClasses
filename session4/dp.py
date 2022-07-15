def fib_recursion(n):
    # Base case
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return fib_recursion(n-1) + fib_recursion(n-2)

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
    print(fib_recursion(35))

    tble = {0: 1, 1: 1}
    # print(fib_memoization(5, tble))
    print(fib_tabulation(40, tble))