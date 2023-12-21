
def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 528
    end_index = 606
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i].islower():
            if my_string[i] > 'M' and my_string[i] <= 'X':
                result.append(my_string[i])
    return result
