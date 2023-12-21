
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(2, 7):
        if i < len(string):
            char = string[i]
            if '^' < char <= 'd' and char in vowels:
                result.append(char)
    return result
