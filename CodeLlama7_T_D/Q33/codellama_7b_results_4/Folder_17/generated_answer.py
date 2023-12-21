
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 60
    end_index = 99
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].lower() in vowels and my_string[i] > 'j' and my_string[i] <= 'n':
            result.append(my_string[i])
    return result
