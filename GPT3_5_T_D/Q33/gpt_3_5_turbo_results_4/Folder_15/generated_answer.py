
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    if len(string) <= 6 or len(string) <= 3:
        return result
    for i in range(5, 6):
        if string[i] in vowels and string[i] > string[3] and string[i] <= '^':
            result.append(string[i])
    return result
