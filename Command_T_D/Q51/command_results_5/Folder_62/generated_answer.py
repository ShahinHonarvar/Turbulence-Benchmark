import functools
@functools.lru_cache(maxsize=289)
def if_contains_anagrams(input_list):
    # https://github.com/nishant403/data-driven-compound-string-finder
    # https://github.com/nishant403/data-driven-compound-string-finder/blob/master/compound.py
    input_set = set(input_list)
    input_dict = {}
    for s in input_set:
        s = str(s).lower()
        if len(s) < 3:
            continue
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    continue
                if s[i] in s[j]:
                    continue
                if s[i] + s[j] not in input_dict:
                    input_dict[s[i] + s[j]] = 1
                elif input_dict[s[i] + s[j]] == 1:
                    input_dict[s[i] + s[j]] += 1
    return True
