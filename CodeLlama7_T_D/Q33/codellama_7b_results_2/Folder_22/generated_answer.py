
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 56
    end_index = 90
    result = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > 'K' and char <= 'z':
            result.append(char)
    return result
