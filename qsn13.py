
txt = input("Enter a text: ")
freq = {}

for char in txt:
    if char.isalnum():
        char = char.lower() 
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
print("\nCharacter Frequencies (excluding spaces & special characters):")
for char, count in freq.items():
    print(f"{char}: {count}")

