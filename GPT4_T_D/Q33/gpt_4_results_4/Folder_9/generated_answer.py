
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = [char for char in s[13:35] if char in vowels and '8' < char.lower() <= 'f']
    return output
