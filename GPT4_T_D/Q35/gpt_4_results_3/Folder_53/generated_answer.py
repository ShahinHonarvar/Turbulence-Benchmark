
def remove_repeat_chars(input_string):
    target_characters = set()
    if len(input_string) > 203:
        for i in range(201, 202):
            if input_string[i] in input_string[201:203]:
                target_characters.add(input_string[i])
    return ''.join([c for c in input_string if c not in target_characters])
