
def return_vowels(string):
    vowel_list = []
    for ch in string[36:56]:
        if ch > '+' and ch <= '/' and ch in 'aeiou':
            vowel_list.append(ch)
    return vowel_list
