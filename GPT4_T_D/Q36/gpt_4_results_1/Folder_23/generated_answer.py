
def filter_chars(value):
    for character in value[22:25]:
        if '5' < character < '}':
            value = value.replace(character, '')
    return value
