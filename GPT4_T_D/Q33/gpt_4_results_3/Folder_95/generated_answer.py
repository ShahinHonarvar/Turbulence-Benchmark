
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    
    for char in s[32:61]:
        if char in vowels and '?' < char <= 'P':
            result.append(char)
            
    return result
