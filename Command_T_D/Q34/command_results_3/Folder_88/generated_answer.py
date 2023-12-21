import heapq as hq
def find_original_set(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27):
    s = set(s1).union(set(s2)).union(set(s3)).union(set(s4)).union(set(s5)).union(set(s6)).union(set(s7)).union(set(s8)).union(set(s9)).union(set(s10)).union(set(s11)).union(set(s12)).union(set(s13)).union(set(s14)).union(set(s15)).union(set(s16)).union(set(s17)).union(set(s18)).union(set(s19)).union(set(s20)).union(set(s21)).union(set(s22)).union(set(s23)).union(set(s24)).union(set(s25)).union(set(s26)).union(set(s27))
    hq.heapify(s)
    return sorted(hq.nlargest(27,s))
