
def return_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[19:32] if ch in vowel_list and '0' < ch <= '7']
