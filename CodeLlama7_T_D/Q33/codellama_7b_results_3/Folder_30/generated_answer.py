
def return_vowels(my_string):
    vowels = ["A", "E", "I", "O", "U"]
    start_index = 11
    end_index = 61
    result = []
    for i in range(start_index, end_index + 1):
        char = my_string[i]
        if (char.isalpha() and char.lower() not in vowels) or (char.isdigit() and int(char) > 64):
            result.append(char)
    return result
