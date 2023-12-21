
def return_vowels(string):
    vowels = "aeiou"
    letters = list(string[10:83])
    result = [i for i in letters if i in vowels and '%' < i <= 'e']
    return result
