
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if len(string) > 872:
        substring = string[202:872]
        result = [ch for ch in substring if ch in vowels and '3' < ch <= '>']
        return result
    else:
        return []
