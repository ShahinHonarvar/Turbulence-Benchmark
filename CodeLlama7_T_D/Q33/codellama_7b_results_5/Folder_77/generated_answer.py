
def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 837
    end_index = 975
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i] > 'N' and my_string[i] <= 'W':
                result.append(my_string[i])
    return result
