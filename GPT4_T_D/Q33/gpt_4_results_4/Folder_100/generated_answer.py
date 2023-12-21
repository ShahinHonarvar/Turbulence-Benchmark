
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in input_string[23:75]:
        if char in vowels and 'L' < char <= 'd':
            result.append(char)
    return result
