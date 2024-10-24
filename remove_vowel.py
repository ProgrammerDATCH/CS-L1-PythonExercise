text = input("Enter a string of text: ")
vowels = "aeiouAEIOU"
output = ""

for char in text:
    if char not in vowels:
        output += char

print("Text without vowels:", output)
