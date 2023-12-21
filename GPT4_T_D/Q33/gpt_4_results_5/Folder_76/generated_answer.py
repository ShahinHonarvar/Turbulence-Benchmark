
def return_vowels(string):
    vowels = 'aeiou'
    list_vowels = []
    string = string[495:837]
    for ch in string:
        if ch.lower() in vowels and 'B' < ch <= 't':
            list_vowels.append(ch)
    return list_vowels
