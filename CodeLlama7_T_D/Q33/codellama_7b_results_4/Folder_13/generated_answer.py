
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 149
    end_index = 313
    result = []
    for i in range(start_index, end_index):
        if string[i].isalpha() and string[i].lower() in vowels:
            if string[i] > 'M' and string[i] <= 'j':
                result.append(string[i])
    return result
