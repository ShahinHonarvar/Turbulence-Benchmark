
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    
    for i in range(528, 606):
        if s[i] in vowels and ord('M') < ord(s[i]) <= ord('X'):
            result.append(s[i])
    
    return result
