
def return_vowels(string):
    vowel_list = []
    for char in string[32:97]:
        if char > 'Q' and char <= ']':
            if char.lower() in 'aeiou':
                vowel_list.append(char)
    return vowel_list
