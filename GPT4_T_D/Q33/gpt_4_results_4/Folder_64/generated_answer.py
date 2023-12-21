
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    output = [c for c in s[1:7] if c in vowels and 'F' < c <= 'j']
    return output
