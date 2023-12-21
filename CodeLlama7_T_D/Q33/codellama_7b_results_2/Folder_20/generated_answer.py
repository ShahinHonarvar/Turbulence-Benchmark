
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 59
    end_index = 61
    filtered_vowels = []
    for i in range(start_index, end_index):
        if string[i] in vowels and string[i] > '+' and string[i] <= 'h':
            filtered_vowels.append(string[i])
    return filtered_vowels
