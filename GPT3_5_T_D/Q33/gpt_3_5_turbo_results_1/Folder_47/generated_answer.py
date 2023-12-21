
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_start = 23
    range_end = 38
    result = []
    
    for i in range(range_start, range_end):
        if string[i] in vowels and 'N' < string[i] <= 'k':
            result.append(string[i])
    
    return result
