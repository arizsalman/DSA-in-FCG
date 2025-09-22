"""Leetcode No 34 """

# nums = [5, 7, 7, 8, 8, 10], target = 8, [3, 4]


def find(nums,  target):

    def first(nums, target):
        left, right = 0, len(nums)-1
        find = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                find = mid
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return find

    def last(nums, target):
        left, right = 0, len(nums)-1
        find = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                find = mid
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return find
    return first(nums, target), last(nums, target)


print(find(nums=[5, 7, 7, 8, 8, 10], target=8))
print(find(nums=[5, 7, 7, 8, 8, 10], target=6))


# arr = [2,3,4,7,11], k = 5
def func(arr, k):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)
        missing = arr[mid]-(mid+1)
        if missing < k:
            left = mid+1
        else:
            right = mid-1
    return left + k


print(func(arr=[2, 3, 4, 7, 11], k=5))
