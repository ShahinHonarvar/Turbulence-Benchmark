
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 21
    end_index = 23
    result = []
    for i in range(start_index, end_index):
        if string[i].isalpha() and string[i] in vowels:
            if string[i] > '-' and string[i] <= 'n':
                result.append(string[i])
    return result
