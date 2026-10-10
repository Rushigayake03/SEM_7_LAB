def fibonacci_non_recursive(n):
    if n == 0:
        return 0

    a = 0
    b = 1

    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return b


def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



n = int(input("Enter the value of n: "))


result1 = fibonacci_non_recursive(n)
print("\nNon-Recursive Method")
print("Fibonacci number:", result1)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")



result2 = fibonacci_recursive(n)
print("\nRecursive Method")
print("Fibonacci number:", result2)
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")
