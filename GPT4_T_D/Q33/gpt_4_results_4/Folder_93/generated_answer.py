
def return_vowels(s):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    result = [ch for ch in s[54:82] if ch in vowels and '=' < ch <= '@']
    return result
