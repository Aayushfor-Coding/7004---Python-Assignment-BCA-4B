def demonstrate_slicing(string):
    print("Original string:", string)
    print("First three characters:", string[:3])
    print("Characters from index 2 to 5:", string[2:6])
    print("Last three characters:", string[-3:])
    print("Every second character:", string[::2])

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    demonstrate_slicing(input_string)
