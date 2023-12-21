
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 11
    end_index = 53
    result = []
    for i in range(start_index, end_index + 1):
        if string[i] in vowels and string[i] > '+' and string[i] <= 'W':
            result.append(string[i])
    return result
