
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[328:455] if '<' < char <= 'z' and char in vowels]
