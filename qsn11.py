numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
unique_numbers = set(numbers)
sorted_list = sorted(unique_numbers)
print("Sorted list without duplicates:", sorted_list)
