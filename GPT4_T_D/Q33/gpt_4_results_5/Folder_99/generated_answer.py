
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[323:526] if char in vowels and '+' < char <= ':']
