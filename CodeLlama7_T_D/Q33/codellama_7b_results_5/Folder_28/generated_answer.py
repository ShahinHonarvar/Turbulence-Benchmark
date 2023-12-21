
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    start_index = 41
    end_index = 50
    result = []
    for i in range(start_index, end_index):
        if string[i].isalpha() and string[i] in vowels and string[i] > 'W' and string[i] <= '[':
            result.append(string[i])
    return result
