
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [i for i in s[20:41] if i in vowels and 'K' < i <= 'Z']
    return result
