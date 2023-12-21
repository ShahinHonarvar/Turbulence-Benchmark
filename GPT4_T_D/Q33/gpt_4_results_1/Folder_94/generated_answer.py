
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    acceptable_chars = list(map(chr, range(ord('5'), ord('H')+1)))
    return [v for v in string[40:94] if v in vowels and v in acceptable_chars]
