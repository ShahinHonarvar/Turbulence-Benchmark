
def return_nth_smallest_ascii(character_string):
    if 17 <= len(character_string) <= 65:
        sorted_chars = sorted(character_string[17:66])
        if len(sorted_chars) >= 8:
            return sorted_chars[7]
        else:
            return "Not enough characters"
    else:
        return "String's length is not in range 17 to 65"
