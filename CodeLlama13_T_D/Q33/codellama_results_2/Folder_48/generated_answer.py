
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 529
    end_index = 828
    result = []
    for i in range(start_index, end_index):
        if string[i] in vowels and string[i] > 'U' and string[i] <= 'l':
            result.append(string[i])
    return result
