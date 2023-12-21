
def return_vowels(my_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 56
    end_index = 68
    vowel_list = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i] > 'M' and my_string[i] <= 'X':
                vowel_list.append(my_string[i])
    return vowel_list
