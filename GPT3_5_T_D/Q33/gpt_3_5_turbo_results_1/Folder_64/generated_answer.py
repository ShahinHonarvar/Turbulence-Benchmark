
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:7]:
        if char > 'F' and char <= 'j' and char.lower() in vowels:
            result.append(char)
    return result
