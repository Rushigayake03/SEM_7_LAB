# Fractional Knapsack using Greedy Method
def fractional_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by value/weight ratio in descending order
    items.sort(reverse=True)


    total = 0

    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total += value
        else:
            total += ratio * capacity
            break

    return total


# Take input from user
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = float(input("Enter weight of item " + str(i + 1) + ": "))
    v = float(input("Enter value of item " + str(i + 1) + ": "))
    weights.append(w)
    values.append(v)

capacity = float(input("Enter knapsack capacity: "))

result = fractional_knapsack(weights, values, capacity)

print("Maximum value:", result)
print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")