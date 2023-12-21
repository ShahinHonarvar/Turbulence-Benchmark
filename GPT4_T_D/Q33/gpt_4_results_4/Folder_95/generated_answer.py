
def return_vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = [ch for ch in s[32:61] if ch in vowels and '?' < ch <= 'P']
    return result
