
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 29
    end_index = 31
    found_vowels = []

    for i in range(start_index, end_index):
        if my_string[i].lower() in vowels and my_string[i] > 'a' and my_string[i] <= 'f':
            found_vowels.append(my_string[i])

    return found_vowels
