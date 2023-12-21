
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(171, 402):
        if i > ord('I') and i <= ord('k') and chr(i).lower() in vowels:
            result.append(chr(i))
    
    return result
