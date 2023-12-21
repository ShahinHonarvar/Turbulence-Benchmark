
def remove_repeat_chars(s):
    target_region = s[70:97]
    processed_str = ''

    for ch in s:
        if ch in target_region and target_region.count(ch) > 1:
            target_region = target_region.replace(ch, '')
        else:
            processed_str += ch

    return processed_str
