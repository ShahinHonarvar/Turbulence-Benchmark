
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 13
    end_index = 37
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i].lower() in vowels and my_string[i] > 'Z' and my_string[i] <= '}':
            result.append(my_string[i])
    return result
