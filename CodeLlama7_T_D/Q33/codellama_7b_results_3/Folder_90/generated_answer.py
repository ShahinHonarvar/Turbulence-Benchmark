
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 142
    end_index = 145
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] not in vowels:
            if my_string[i] > '4' and my_string[i] <= 'o':
                result.append(my_string[i])
    return result
