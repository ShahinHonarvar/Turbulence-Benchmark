
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 4 or i > 8:
            result += char
        elif char > '1' and char < 'J':
            for j, other_char in enumerate(string[i+1:]):
                if other_char != char:
                    result += other_char
                    break
    return result
