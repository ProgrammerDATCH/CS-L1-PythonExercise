camel_case = input("Enter a variable name in camel case: ")
snake_case = ""

for char in camel_case:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print("The variable name in snake case is:", snake_case)
