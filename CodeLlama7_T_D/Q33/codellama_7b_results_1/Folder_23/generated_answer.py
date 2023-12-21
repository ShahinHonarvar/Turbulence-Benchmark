
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 56
    end_index = 96
    result = []
    for i in range(start_index, end_index + 1):
        char = my_string[i]
        if char in vowels and char > "&" and char <= "T":
            result.append(char)
    return result
