
def return_nth_smallest_ascii(string):
    substring = string[12:88]
    characters = set(substring)
    sorted_characters = sorted(characters)
    
    if len(sorted_characters) >= 17:
        return sorted_characters[16]
    else:
        return None
