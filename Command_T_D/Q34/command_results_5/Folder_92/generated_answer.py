import sys
import heapq as hp
def find_original_set(S1, S2, S3, S4, S5, S6, S7, S8):
    q = [(S1, 0, 1), (S2, 1, 1), (S3, 2, 1), (S4, 3, 1), (S5, 4, 1), (S6, 5, 1), (S7, 6, 1), (S8, 7, 1)]
    h = []
    hq = []
    for s in q:
        if s[0] not in h:
            hp.heappush(hq, (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]))
            h.append(s[0])
    for s in q:
        if s[0] in h:
            hp.heappush(hq, (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]))
    while hq:
        s = hp.heappop(hq)
        s1, s2, s3, s4, s5, s6, s7, s8 = s
        if s1 <= s2 <= s3 <= s4 <= s5 <= s6 <= s7 <= s8:
            return s
    return None
