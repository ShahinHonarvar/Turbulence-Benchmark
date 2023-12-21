
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    v = [letter for letter in s[323:526] if letter in vowels and '+' < letter <= ':']
    return v
