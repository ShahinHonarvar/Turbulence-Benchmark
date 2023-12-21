
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    s = s[14:60]
    return [ch for ch in s if (ch > 'D' and ch <= 'v' and ch in vowels)]
