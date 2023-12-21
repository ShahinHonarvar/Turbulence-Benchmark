
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 50
    end_index = 51
    result = []
    for i in range(start_index, end_index):
        if string[i] in vowels and string[i] > ',' and string[i] <= 'v':
            result.append(string[i])
    return result
