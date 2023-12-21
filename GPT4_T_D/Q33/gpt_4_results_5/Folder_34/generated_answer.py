
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sublist = [x for x in s[19:32] if x in vowels and '0' < x <= '7']
    return sublist
