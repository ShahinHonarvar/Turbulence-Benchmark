
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    
    for ch in s[14:60]:
        if ch > 'D' and ch <= 'v' and ch in vowels:
            result.append(ch)
    
    return result
