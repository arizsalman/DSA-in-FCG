"""Python slicing ka Concept 

Start index (include hota hai) → jo bhi likho, usi index se values milni shuru ho jati hain.

End index (exclude hota hai) → us index tak jaata hai, lekin us element ko include nahi karta.

👉 Ye bad behavior nahi hai, ye intentionally aisa design kiya gaya hai.
    actually ye smart behavior hai jo maths aur programming me consistency laata hai.
"""


def func(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]  # is ko ese bhekar sakte  he nums[0:mid]0 se mid tak
    # is ko kse he likehe ge . -1 kar ge tu last element include nahe hoga .
    right = nums[mid:]
    # is line me hum ak arry ko do isso me tol rahe he
    left_sort, right_sort = func(left), func(right)

    # or  is me hum 2 haso ko 1 hase me jol raahe he
    sorted_nums = left_sort, right_sort
    return sorted_nums


""" ye hum ne skeleton  bana he ke ye kam kese karta he """


# print(func([2, 6, 3, 5, 1, 2, 4, 9]))


def merge(left, right):
    j = i = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def fun(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    left_sort, right_sort = fun(left), fun(right)
    return merge(left_sort, right_sort)


print(fun([2, 6, 3, 5, 1, 2, 4, 9]))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    num1 = (left[i:])
    num2 = (right[j:])
    return result+num1+num2


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_two(left, right)


def main(arr):
    return merge_sort(arr)


print(main([8, 3, 3, 5, 6, 1, 8, 2, 9]))
