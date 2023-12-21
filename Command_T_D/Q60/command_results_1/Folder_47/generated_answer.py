
import re
import functools
import itertools
import bisect
import heapq
import math

MOD = 998244353
INF = float("inf")
OPS = {">>": (1, 0), "<<": (0, -1), "<>": (-1, 0), "->": (0, 1)}


@functools.lru_cache(maxsize=2 ** 8)
def prime():
    """Returns a list of prime numbers"""
    # Factors
    factors = [(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 637, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 733, 739, 743, 751, 757, 761, 763, 769, 773, 781, 783, 797, 809, 811, 821, 823, 827, 829, 833, 839, 853, 857, 859, 863, 867, 871, 873, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1113, 1121, 1122, 1125, 1129, 1133, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1291, 1297, 1303, 1307, 1311, 1317, 1323, 1333, 1343, 1347, 1353, 1359, 1363, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1453, 1459, 1471, 1481, 1483, 1487, 1491, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1649, 1657, 1663, 1667, 1669, 1693, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1793, 1799, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1881, 1901, 1907, 1913, 1919, 1933, 1937, 1943, 1947, 1951, 1957, 1963, 1967, 1971, 1973, 1977, 1983, 1987, 1993, 1999, 2003, 2009, 2013, 2017, 2023, 2029, 2049, 2059, 2063, 2069, 2081, 2083, 2087, 2099, 2111, 2129, 2131, 2137, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2281, 3217, 4253, 4423, 9689)

    # Factors with odd
    # Factors with even
    # Factors with multiple of 5
    # Factors with multiple of 3
    # Factors with multiple of 2
    # Factors with prime number
    # Factors with multiple of prime number
    # Factors with odd and even
    # Factors with odd and even and multiple of 5
    # Factors with odd and even and multiple of 3
    # Factors with odd and even and multiple of 2
    # Factors with odd and even and multiple of prime number
    # Factors with odd and even and multiple of multiple of prime number
    # Factors with odd and even and multiple of prime number and prime number
    # Factors with odd and even and multiple of prime number and prime number and prime number
    # Factors with odd and even and multiple of prime number and prime number and prime number and prime number
    # Factors with odd and even and multiple of prime number and prime number and prime number and prime number and prime number
    # Factors with odd and even and multiple of prime number and prime number and prime number and prime number and prime number and prime number
    # Factors with odd
	