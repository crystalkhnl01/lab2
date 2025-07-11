sentence = input("Enter a sentence: ")
vowels = set("aeiouAEIOU")
unique_vowels = set()

for char in sentence:
    if char in vowels:
        unique_vowels.add(char)

print("Unique vowels used:", unique_vowels)
