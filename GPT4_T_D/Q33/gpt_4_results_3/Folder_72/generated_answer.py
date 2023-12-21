
def return_vowels(str1):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    sublist = [ch for ch in str1[37:57] if ch > '*' and ch <= 'P' and ch in vowels]
    return sublist
