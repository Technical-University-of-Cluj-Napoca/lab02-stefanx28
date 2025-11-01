from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    set_anagrams = defaultdict(list)

    for s in strs:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord('a')] += 1
        key = tuple(key)
        set_anagrams[key].append(s)
    
    return list(set_anagrams.values())
    pass

if __name__ == "__main__":
    s = input().split()
    res = group_anagrams(s)
    print(res)
