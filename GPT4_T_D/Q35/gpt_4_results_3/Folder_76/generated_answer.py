
def remove_repeat_chars(text):
    char_counts = {}

    for i in range(331, 543):
        if text[i] not in char_counts:
            char_counts[text[i]] = 1
        else:
            char_counts[text[i]] += 1

    new_text = ""
    for char in text:
        if char in char_counts and char_counts[char] > 1:
            continue
        new_text += char
    return new_text
