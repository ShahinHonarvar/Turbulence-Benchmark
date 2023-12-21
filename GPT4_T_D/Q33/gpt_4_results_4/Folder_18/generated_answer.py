
def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(528, 606):
        if i < len(s) and s[i] > 'M' and s[i] <= 'X' and s[i].lower() in vowels:
            result.append(s[i])
    return result
