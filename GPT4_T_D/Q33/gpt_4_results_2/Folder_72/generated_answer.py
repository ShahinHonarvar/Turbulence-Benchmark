
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [v for v in string[37:57] if v in vowels and 'P' >= v > '*']
    return result
