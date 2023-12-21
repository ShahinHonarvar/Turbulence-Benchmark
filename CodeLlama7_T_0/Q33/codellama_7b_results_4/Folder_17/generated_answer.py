
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 60
    end_index = 99
    result = []
    for i in range(start_index, end_index + 1):
        if string[i] in vowels and string[i] > 'j' and string[i] <= 'n':
            result.append(string[i])
    return result
