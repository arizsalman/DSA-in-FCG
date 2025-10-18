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

# def func(head):
#     stack = []
#     current = head
#     while current:
#         stack.append(current)
#         current = current.next

#     left, right = 0, len(head)-1
#     while left < right:
#         if head in left:
#             left += 1
#         right -= 1
#     return stack


# print(func([1, 2, 3, 4, 5]))


# def fun(head):
#     per = None
#     curr = head

#     while curr:
#         temp = curr.next
#         curr.next = per
#         """temp = curr.next → aage ka pointer save karta hai.
# curr.next = per → peeche ka pointer set karta hai (link reverse karta hai)."""
#         per = curr
#         curr = temp
#     return per


# """Pehle next se aage ki value dekh rahe hain,

# Phir us node ka next pointer peeche (previous) ki taraf kar rahe hain.

# Exactly yehi hai linked list reversal ka concept."""

# print(fun([1, 2, 3, 4, 5]))


# def func(n):

#     if n == 0:
#         return 1
#     return n * func(n-1)


# print(func(2))

# def removeNthFromEnd(self, head):
#     slow = head
#     fast = head

#     for _ in range(n):
#         fast = fast.next

#     if fast == None:
#         return head.next

#     while fast. next:
#         slow = slow.next
#         fast = fast.next

#     slow.next = slow.next.next
#     return head


# print(removeNthFromEnd(1, 2, 3, 4)2)


# Leetcode no 278 !


def func(n, bad):
    left, right = 1, n
    while left < right:
        mid = (left+right)//2
        if mid >= bad:
            right = mid
        else:
            left = mid+1

    return left


print(func(5, 4))
