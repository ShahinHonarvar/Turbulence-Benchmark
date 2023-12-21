
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(63, min(79, len(s))):
        if s[i] in vowels and 'D' < s[i] <= 'y':
            result.append(s[i])
    return result
