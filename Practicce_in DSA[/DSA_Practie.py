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


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Practice 206

def func(head):
    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next

    left, right = 0, len(head)-1
    while left < right:
        if head in left:
            left += 1
        right -= 1
    return stack


print(func([1, 2, 3, 4, 5]))
