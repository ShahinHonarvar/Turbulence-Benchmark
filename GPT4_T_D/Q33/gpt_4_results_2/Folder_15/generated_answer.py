
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    criteria = [char for char in s[5:6] if (char > '3' and char <= '^' and char in vowels)]
    return criteria
