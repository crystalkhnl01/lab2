import random
numbers = set()

while len(numbers) < 10:
    rand_num = random.randint(1, 100)
    numbers.add(rand_num)

print("Original Set with 10 unique elements:", numbers)

min_val = min(numbers)
max_val = max(numbers)

numbers.remove(min_val)
numbers.remove(max_val)

print("Set after removing smallest and largest elements:")
print("Removed smallest:", min_val)
print("Removed largest:", max_val)
print("Remaining Set:", numbers)

