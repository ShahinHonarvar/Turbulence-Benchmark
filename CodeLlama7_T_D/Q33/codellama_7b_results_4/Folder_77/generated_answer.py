
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 837
    end_index = 975
    result = []
    for i in range(start_index, end_index + 1):
        char = my_string[i]
        if char.isalpha() and char.lower() in vowels:
            if char > 'N' and char <= 'W':
                result.append(char)
    return result
