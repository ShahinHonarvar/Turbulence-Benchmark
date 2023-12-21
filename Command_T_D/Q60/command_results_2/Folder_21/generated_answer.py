
import math
import heapq as hq
import bisect

def prime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Check only last digit
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check only middle digit
    if n % 5 == 0 or n % 7 == 0:
        return False
    # Check only middle digit
    if n % 11 == 0 or n % 13 == 0:
        return False
    # Check only middle digit
    if n % 17 == 0 or n % 19 == 0:
        return False
    # Check only middle digit
    if n % 23 == 0 or n % 29 == 0:
        return False
    # Check only middle digit
    if n % 31 == 0 or n % 37 == 0:
        return False
    # Check only middle digit
    if n % 41 == 0 or n % 43 == 0:
        return False
    # Check only middle digit
    if n % 47 == 0 or n % 53 == 0:
        return False
    # Check only middle digit
    if n % 59 == 0 or n % 61 == 0:
        return False
    # Check only middle digit
    if n % 67 == 0 or n % 71 == 0:
        return False
    # Check only middle digit
    if n % 73 == 0 or n % 79 == 0:
        return False
    # Check only middle digit
    if n % 83 == 0 or n % 89 == 0:
        return False
    # Check only middle digit
    if n % 97 == 0 or n % 101 == 0:
        return False
    # Check only middle digit
    if n % 103 == 0 or n % 107 == 0:
        return False
    # Check only middle digit
    if n % 109 == 0 or n % 113 == 0:
        return False
    # Check only middle digit
    if n % 127 == 0 or n % 131 == 0:
        return False
    # Check only middle digit
    if n % 137 == 0 or n % 139 == 0:
        return False
    # Check only middle digit
    if n % 149 == 0 or n % 151 == 0:
        return False
    # Check only middle digit
    if n % 157 == 0 or n % 163 == 0:
        return False
    # Check only middle digit
    if n % 167 == 0 or n % 173 == 0:
        return False
    # Check only middle digit
    if n % 179 == 0 or n % 181 == 0:
        return False
    # Check only middle digit
    if n % 191 == 0 or n % 193 == 0:
        return False
    # Check only middle digit
    if n % 197 == 0 or n % 199 == 0:
        return False
    # Check only middle digit
    if n % 211 == 0 or n % 223 == 0:
        return False
    # Check only middle digit
    if n % 227 == 0 or n % 229 == 0:
        return False
    # Check only middle digit
    if n % 233 == 0 or n % 239 == 0:
        return False
    # Check only middle digit
    if n % 241 == 0 or n % 251 == 0:
        return False
    # Check only middle digit
    if n % 257 == 0 or n % 263 == 0:
        return False
    # Check only middle digit
    if n % 269 == 0 or n % 271 == 0:
        return False
    # Check only middle digit
    if n % 273 == 0 or n % 277 == 0:
        return False
    # Check only middle digit
    if n % 281 == 0 or n % 283 == 0:
        return False
    # Check only middle digit
    if n % 293 == 0 or n % 307 == 0:
        return False
    # Check only middle digit
    if n % 311 == 0 or n % 317 == 0:
        return False
    # Check only middle digit
    if n % 331 == 0 or n % 337 == 0:
        return False
    # Check only middle digit
    if n % 347 == 0 or n % 349 == 0:
        return False
    # Check only middle digit
    if n % 353 == 0 or n % 359 == 0:
        return False
    # Check only middle digit
    if n % 367 == 0 or n % 373 == 0:
        return False
    # Check only middle digit
    if n % 379 == 0 or n % 383 == 0:
        return False
    # Check only middle digit
    if n % 389 == 0 or n % 397 == 0:
        return False
    # Check only middle digit
    if n % 401 == 0 or n % 409 == 0:
        return False
    # Check only middle digit
    if n % 419 == 0 or n % 423 == 0:
        return False
    # Check only middle digit
    if n % 431 == 0 or n % 433 == 0:
        return False
    # Check only middle digit
    if n % 443 == 0 or n % 449 == 0:
        return False
    # Check only middle digit
    if n % 457 == 0 or n % 463 == 0:
        return False
    # Check only middle digit
    if n % 467 == 0 or n % 479 == 0:
        return False
    # Check only middle digit
    if n % 487 == 0 or n % 499 == 0:
        return False
    # Check only middle digit
    if n % 503 == 0 or n % 509 == 0:
        return False
    # Check only middle digit
    if n % 521 == 0 or n % 607 == 0:
        return False
    # Check only middle digit
    if n % 607 == 0 or n % 613 == 0:
        return False
