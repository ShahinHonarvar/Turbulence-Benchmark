
def remove_repeat_chars(string):
    if 6 <= len(string) < 9:
        char_counts = {}
        for char in string:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
        
        new_string = ""
        for char in string[:6]:
            new_string += char
        
        for char in string[6:]:
            if char_counts[char] > 1:
                continue
            else:
                new_string += char
        
        return new_string + string[9:]
    else:
        return string
