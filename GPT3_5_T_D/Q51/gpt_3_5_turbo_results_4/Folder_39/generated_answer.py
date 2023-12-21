
def if_contains_anagrams(strings):
    def count_chars(s):
        chars = [0] * 26
        for char in s.lower():
            if 'a' <= char <= 'z':
                chars[ord(char) - ord('a')] += 1
        return tuple(chars)

    counts = {}
    pair_count = 0
    for string in strings:
        if len(string) < 3:
            continue
        chars = count_chars(string)
        if chars in counts:
            counts[chars] += 1
            if counts[chars] % 2 == 0:
                pair_count += 1
        else:
            counts[chars] = 1

    return pair_count <= 257
