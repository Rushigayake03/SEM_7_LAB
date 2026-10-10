# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


# Take input from user
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input("Enter weight of item " + str(i + 1) + ": "))
    value = int(input("Enter value of item " + str(i + 1) + ": "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

# Display result
maximum, items = knapsack(weights, values, capacity)

print("\nMaximum value:", maximum)
print("Selected items:", items)
print("Time Complexity: O(n * capacity)")
print("Space Complexity: O(n * capacity)")