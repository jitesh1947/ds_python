# Bubble sort in Python
data = [-2, 45, 0, 11, -9]
print(data)
print("After sort")
for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        # To sort in descending order, change > to < in this line.
        if data[j] > data[j + 1]:
            # swap if greater is at the rear position
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)