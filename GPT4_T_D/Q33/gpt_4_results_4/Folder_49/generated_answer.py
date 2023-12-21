
def return_vowels(s):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    return [ch for ch in s[10:97] if ch in vowels and 'R' < ch <= 'b']
