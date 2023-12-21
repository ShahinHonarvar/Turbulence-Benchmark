
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 21
    end_index = 23
    result = []
    for char in string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels:
            if char > '-' and char <= 'n':
                result.append(char)
    return result
