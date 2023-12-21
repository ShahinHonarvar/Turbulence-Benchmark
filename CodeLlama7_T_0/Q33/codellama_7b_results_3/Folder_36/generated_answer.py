
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 604
    end_index = 949
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].lower() in vowels and my_string[i] > 'N' and my_string[i] <= 'U':
            result.append(my_string[i])
    return result
