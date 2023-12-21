
def return_vowels(s):
    s_list = list(s[273:275])
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [ch for ch in s_list if ch in vowels and '+' < ch <= 'o']
