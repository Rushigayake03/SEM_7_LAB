import heapq

def huffman(chars, freq):
    # Create min heap
    h = [(f, c) for c, f in zip(chars, freq)]
    heapq.heapify(h)

    # Build Huffman Tree
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)

        new_node = (a[0] + b[0], (a[1], b[1]))
        heapq.heappush(h, new_node)

    # Generate Huffman Codes
    def code(tree, c=""):
        if isinstance(tree, str):
            print(tree, ":", c if c else "0")
        else:
            code(tree[0], c + "0")
            code(tree[1], c + "1")

    code(h[0][1])

    return h[0]


# Input
n = int(input("Enter number of characters: "))

chars = input("Enter characters: ").split()
freq = list(map(int, input("Enter frequencies: ").split()))

# Huffman Encoding
tree = huffman(chars, freq)

print("Huffman Tree:", tree)
print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")