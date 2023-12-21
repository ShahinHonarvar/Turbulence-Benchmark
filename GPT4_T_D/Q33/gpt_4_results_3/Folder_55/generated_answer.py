
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']  
    res = [c for c in string[1:5] if c in vowels and c>='!' and c<='j'] 
    return res
