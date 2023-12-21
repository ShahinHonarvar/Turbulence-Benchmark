
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [i for i in string[1:7] if i > 'F' and i <= 'j' and i in vowels]
    return result
