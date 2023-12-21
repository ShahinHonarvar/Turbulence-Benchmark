
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_string = str[22:82]
    result = []
    for char in sub_string:
        if char in vowels and 'N' < char <= 'o':
            result.append(char)
    return result
