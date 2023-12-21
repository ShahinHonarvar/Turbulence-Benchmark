
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 71
    end_index = 88
    filtered_vowels = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] > '9' and my_string[i] <= 'P':
            filtered_vowels.append(my_string[i])
    return filtered_vowels
