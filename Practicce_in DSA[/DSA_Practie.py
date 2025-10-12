def isAnagram(s, t):
    if len(s) != len(t):
        return 123
    elif sorted(s) == sorted(t):
        print(f' sors{sorted(s)}{sorted(t)}')
        return True
    # else:
    #     return False


print(isAnagram(s="anagm", t="nam"))  # Yaha first equation called hora rahe he
print(isAnagram(s="anagram", t="nagaram"))  # yaha  second
# yaha condition commit he yaha same equation called nahe hew
print(isAnagram(s="rat", t="car"))


def isAnagram(s, t):
    if len(s) != len(t):
        return 123
    elif sorted(s) == sorted(t):
        print(f' sors{sorted(s)}{sorted(t)}')
        return True
    else:
        return False


print(isAnagram(s="anagm", t="nam"))  # Yaha first equation called hora rahe he
print(isAnagram(s="anagram", t="nagaram"))  # yaha  second
print(isAnagram(s="rat", t="car"))  # yaha third equation called hu rahe he
