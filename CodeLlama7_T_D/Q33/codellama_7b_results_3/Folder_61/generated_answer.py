
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 1
    end_index = 4
    filtered_vowels = []
    for i in range(start_index, end_index + 1):
        current_char = my_string[i]
        if current_char in vowels and current_char > 'C' and current_char <= 'I':
            filtered_vowels.append(current_char)
    return filtered_vowels
