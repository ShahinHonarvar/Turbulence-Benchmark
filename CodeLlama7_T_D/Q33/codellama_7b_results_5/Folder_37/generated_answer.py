
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 82
    end_index = 90
    filtered_vowels = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i].lower() in vowels:
            if my_string[i] > 'T' and my_string[i] <= 'b':
                filtered_vowels.append(my_string[i])
    return filtered_vowels
