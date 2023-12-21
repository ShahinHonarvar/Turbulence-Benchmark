
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    starting_index = 24
    ending_index = 64
    result = []
    for i in range(starting_index, ending_index + 1):
        if my_string[i] in vowels and my_string[i] > "F" and my_string[i] <= "h":
            result.append(my_string[i])
    return result
