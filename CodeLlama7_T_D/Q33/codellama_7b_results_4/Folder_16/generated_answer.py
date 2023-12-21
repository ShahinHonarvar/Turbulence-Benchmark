
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 133
    end_index = 306
    result = []
    for i in range(start_index, end_index):
        if string[i].isalpha() and string[i].lower() in vowels:
            if string[i] > 'c' and string[i] <= 'd':
                result.append(string[i])
    return result
