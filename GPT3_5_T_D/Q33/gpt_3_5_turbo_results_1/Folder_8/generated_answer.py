
def return_vowels(string):
    result = []
    for char in string[64:82]:
        if 'P' < char <= 'z' and char in 'aeiouAEIOU':
            result.append(char)
    return result
