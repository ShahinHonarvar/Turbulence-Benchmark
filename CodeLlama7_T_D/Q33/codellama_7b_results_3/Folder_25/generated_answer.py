
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 28
    end_index = 76
    result = []
    for char in string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '+' and char <= 'z':
            result.append(char)
    return result
