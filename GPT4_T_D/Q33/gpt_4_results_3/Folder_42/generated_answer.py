
def return_vowels(s):
    vowel_list = []
    for ch in s[12:39]:
        if ch in "aeiouAEIOU" and ";" < ch <= "|":
            vowel_list.append(ch)
    return vowel_list
