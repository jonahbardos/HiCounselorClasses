
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
    # print(fib_recursion(10))

    tble = {0:1, 1:1}

    # print(fib_memoization(100, tble))
    print(fib_tabulation(100, tble))

"""
    N = 3 items     M = 5kg capacity of knapsack
    item #1         w_1 = 4kg           v_1 = 10$
    item #2         w_2 = 2kg           v_2 = 4$
    item #3         w_3 = 3kg           v_3 = 7$
    
        |   0   |   1   |   2   |   3   |   4   |   5   |       weights [kg]
        -------------------------------------------------
    0   |       |       |       |       |       |       |       no of items
        -------------------------------------------------
    1   |       |       |       |       |       |       |       [item 1]
        -------------------------------------------------
    2   |       |       |       |       |       |       |       [item 1, item 2]
        -------------------------------------------------
    3   |       |       |       |       |       |       |       all items
        -------------------------------------------------
"""