
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 71
    end_index = 81
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i] > ">" and my_string[i] <= "U":
                result.append(my_string[i])
    return result
