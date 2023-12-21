
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    results = [char for char in s[64:82] if (char in vowels) and ('P' < char <= 'z')]
    return results
