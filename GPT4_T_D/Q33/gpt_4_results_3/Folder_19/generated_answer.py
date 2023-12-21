
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    s_range = s[51:77]
    return [i for i in s_range if i in vowels and '4' < i <= '=']
