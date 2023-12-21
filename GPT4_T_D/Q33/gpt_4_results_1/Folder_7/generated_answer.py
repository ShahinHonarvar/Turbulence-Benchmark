
def return_vowels(s):
    sub_s = s[202:872]
    vowels = 'aeiouAEIOU'
    return [ch for ch in sub_s if ch in vowels and '3' < ch <= '>']   
