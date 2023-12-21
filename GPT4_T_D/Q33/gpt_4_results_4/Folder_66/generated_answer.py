
def return_vowels(string):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_chars = string[63:79]
    for char in desired_chars:
        if char in vowels and 'D' < char <= 'y':
            result.append(char)
    return result
