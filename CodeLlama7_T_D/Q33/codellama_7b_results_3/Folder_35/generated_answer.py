
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 483
    end_index = 664
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char not in filtered_list and vowels.count(char) > 0:
            filtered_list.append(char)
    return filtered_list
