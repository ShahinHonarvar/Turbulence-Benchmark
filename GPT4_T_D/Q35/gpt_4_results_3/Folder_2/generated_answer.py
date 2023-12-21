
def remove_repeat_chars(s):
    counter = {}
    for char in s[73:93]:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    removed_chars = [char for char, count in counter.items() if count > 1]
    result = []
    for char in s:
        if char not in removed_chars:
            result.append(char)
    return "".join(result)
