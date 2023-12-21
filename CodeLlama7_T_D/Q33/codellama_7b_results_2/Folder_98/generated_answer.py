
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 3
    end_index = 9
    filtered_vowels = []
    for i in range(start_index, end_index):
        if string[i].lower() in vowels and string[i] > 'S' and string[i] <= 'U':
            filtered_vowels.append(string[i])
    return filtered_vowels
