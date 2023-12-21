
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 24
    end_index = 59
    result = []
    for i in range(start_index, end_index + 1):
        char = my_string[i]
        if char.isalpha() and char.lower() in vowels and char > "N" and char <= "U":
            result.append(char)
    return result
