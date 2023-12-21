
def return_vowels(s):
    vowels = "aeiouAEIOU"
    range_string = s[20:43]
    result = [ch for ch in range_string if ch in vowels and '5' < ch <= 'M']
    return result
