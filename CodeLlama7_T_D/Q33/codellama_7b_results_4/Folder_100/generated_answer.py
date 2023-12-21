
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 23
    end_index = 75
    result = []
    for char in my_string[start_index:end_index]:
        if char.lower() in vowels and char > 'L' and char <= 'd':
            result.append(char)
    return result
