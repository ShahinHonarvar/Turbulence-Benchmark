
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_s = s[46:49]
    result = [i for i in sub_s if i in vowels and ord('[') < ord(i) <= ord('p')]
    return result
