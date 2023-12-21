
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = str[11:61]
    lst = [ch for ch in str if ch.lower() in vowels and 'M' < ch <= 'W']
    return lst
