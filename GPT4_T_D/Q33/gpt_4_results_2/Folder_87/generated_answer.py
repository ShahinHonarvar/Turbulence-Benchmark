
def return_vowels(string):
    vowels = ['e','i','o']
    return [letter for letter in string[34:58] if letter in vowels and 'b' < letter <= 'o']
