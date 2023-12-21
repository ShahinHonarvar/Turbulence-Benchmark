
import collections

def if_contains_anagrams(strings):
    count = 0
    freq_dict = collections.defaultdict(int)

    for s in strings:
        s_lower = s.lower()
        freq_dict[''.join(sorted(s_lower))] += 1

    for count in freq_dict.values():
        if count >= 2:
            pairs = count * (count - 1) // 2
            if count >= 3:
                count -= 2
                pairs += count * (count - 1) // 2
            count += pairs

    return count >= 88
