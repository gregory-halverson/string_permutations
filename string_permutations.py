__author__ = 'gregory'

import sys
import string

def permute(list):
    if len(list) == 1:
        return [list]

    if type(list) is str:
        return [''.join(subperm) for subperm in permute([ch for ch in list])]

    permutations = []

    for i in range(len(list)):
        for permutation in permute(list[:i] + list[(i + 1):]):
            permutations.append([list[i]] + permutation)

    return permutations

def key_value(s):
    hierarchy = string.digits + string.ascii_uppercase + string.ascii_lowercase
    value = ''

    for i in range(len(s)):
        value += "%02d" % hierarchy.index(s[i])

    return value

with open(sys.argv[1], 'r') as file:
    for line in file:
        perms = permute(line.strip())
        perms = sorted(perms, key=lambda e: key_value(e))
        print(','.join(perms))