
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 54
    end_index = 82
    filtered_list = []
    for i in range(start_index, end_index):
        if string[i].isalpha() and string[i].lower() in vowels and string[i] > character and string[i] <= character:
            filtered_list.append(string[i])
    return filtered_list
