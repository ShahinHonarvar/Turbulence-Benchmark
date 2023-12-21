
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 69
    end_index = 82
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i] > '[' and my_string[i] <= '~':
                result.append(my_string[i])
    return result
