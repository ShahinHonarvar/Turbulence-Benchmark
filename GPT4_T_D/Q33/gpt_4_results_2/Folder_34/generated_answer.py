
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sublist = [ch for ch in string[19:32] if ch > '0' and ch <= '7' and ch in vowels]
    return sublist
