def demonstrate_string_functions(string):
    print("Original string:", string)
    print("Uppercase:", string.upper())
    print("Lowercase:", string.lower())
    print("Capitalized:", string.capitalize())
    print("Length:", len(string))
    print("Split by space:", string.split())
    print("Reversed:", string[::-1])
    print("Count of 'a':", string.count('a'))
    print("Index of 'e':", string.index('e'))

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    demonstrate_string_functions(input_string)
