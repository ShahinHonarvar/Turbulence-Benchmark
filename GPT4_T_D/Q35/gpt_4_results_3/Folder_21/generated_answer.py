
def remove_repeat_chars(s):
    subset = s[463:995]
    occur_more_than_once = [char for char in subset if subset.count(char) > 1]
    return ''.join([char for char in s if char not in occur_more_than_once])
