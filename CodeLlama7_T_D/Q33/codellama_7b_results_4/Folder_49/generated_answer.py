
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 10
    end_index = 97
    filtered_vowels = []
    for i in range(start_index, end_index + 1):
        if string[i] in vowels and string[i].lower() > 'r' and string[i].lower() <= 'b':
            filtered_vowels.append(string[i])
    return filtered_vowels
