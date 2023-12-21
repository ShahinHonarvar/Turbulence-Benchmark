
def return_vowels(s):
    vowels = set("aeiou")
    sub_str = s[45:76]
    return [ch for ch in sub_str if ch in vowels and 'b' < ch <= 'z']
