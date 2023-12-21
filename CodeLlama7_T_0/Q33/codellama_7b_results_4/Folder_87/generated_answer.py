
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 34
    end_index = 58
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i] in vowels:
            if my_string[i] > 'b' and my_string[i] <= 'o':
                result.append(my_string[i])
    return result
