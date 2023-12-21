
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for char in my_string[31:37]:
        if char in vowels and char > ";" and char <= "t":
            result.append(char)

    return result
