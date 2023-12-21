
def filter_chars(my_string):
    characters_to_remove = []

    for i in range(34, 36):
        if (my_string[i] > '>' and my_string[i] < 'A'):
            characters_to_remove.append(my_string[i])
            
    for character in characters_to_remove:
        my_string = my_string.replace(character, '')
        
    return my_string
