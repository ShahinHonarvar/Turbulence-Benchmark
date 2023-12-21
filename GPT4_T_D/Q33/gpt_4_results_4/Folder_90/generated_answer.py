
def return_vowels(text):
    result = []
    subset = text[142:145]
    for char in subset:
        if char in 'aeiou' and '4' < char <= 'o':
            result.append(char)
    return result
