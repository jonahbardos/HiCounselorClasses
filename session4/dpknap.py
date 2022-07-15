class KnapsackProblem:
    def __init__(self, n, M, w, v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]

    def solve(self):
        # Use formula here and populate DP table
        for i in range(self.n+1):
            for w in range(self.M+1):
                exclude_item = self.S[i-1][w]
                include_item = 0 # because by default all 0s
            
                if self.w[i] <= w:
                    include_item = self.v[i] + self.S[i - 1][w - self.w[i]]

                # This is how we memoization. We store sub-results to avoid
                # recalculating the same values 
                self.S[i][w] = max(exclude_item, include_item)
    
    def show_result(self):
        print("MAX profit", self.S[self.n][self.M])

        w = self.M
        for n in range(self.n, 0, -1):
            if self.S[n][w] != 0 and self.S[n][w] != self.S[n-1][w]:
                print("We take item", n)
                w = w - self.w[n]

if __name__ == "__main__":
    num_of_items = 3
    knapsack_capacity = 5
    weights = [0, 4, 2, 3]
    values = [0, 10, 4, 7]
    knapsack = KnapsackProblem(num_of_items, knapsack_capacity, weights, values)
    knapsack.solve()
    knapsack.show_result()
    # print(knapsack.S)