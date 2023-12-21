
def return_vowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = []
    for char in string[22:82]:
        if char in vowels and char > 'N' and char <= 'o':
            result.append(char)
    return result
