
def remove_repeat_chars(string):
    characters_to_remove = set()
    for c in string[19:60]:
        if string[19:60].count(c) > 1:
            characters_to_remove.add(c)
            
    return "".join([c for c in string if c not in characters_to_remove])
