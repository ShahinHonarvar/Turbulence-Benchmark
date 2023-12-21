
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in string[70:76]:
        if char in vowels and '2' < char <= ':':
            result.append(char)
    return result
