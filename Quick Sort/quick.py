"""Quick sort me hum ak variable center pick karte he jis ka name pivot rakte he us ke bad hum alag alag part me divide karke sroted from me karte he or us ko merge kar ke answer dete he  """


# def func(nums):
#     if nums <= 1:
#         return nums
# pivot = partition(nums)
#     func(nums[:pivot-1])# yaha problem ye he ke hum array ke copy bana rahe he
#     func(nums[pivot+1:]) # ab jo next me hum kam karge us me copy nahe karge
#     return nums

def func(nums, start=0, end=None):
    if end is None:
        # ye copy nahe hu ke ab or agar modify karho tu list me array nahe de
        nums = list(nums)
        end = len(nums)-1
    if start < end:
        pivot = partition(nums, start, end)
        func(nums, start, pivot-1)  # yaha array ke copy nahe hu rahe
        func(nums, pivot, end)
    return nums


def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums)-1
    left, right = start, end-1
    # Pivot_value = nums[end] # yar jo last element jo he vo pivot he  jabhe humne yaha  right=end-1 de because pivot end he
    while right > left:
        if nums[left] <= nums[end]:
            # print(f'left is {left} ')
            left += 1
        elif nums[right] > nums[end]:
            # print(f' right {right}')
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end


print(func([4, 2, 6, 3, 4, 6, 2, 1]))


# nums = [5, 2, 3, 1]


def fcun(nums, start=0, end=None):
    if end is None:
        end = len(nums)-1
    if start < end:
        pviot = partitions(nums, start, end)
        fcun(nums, start, pviot-1)
        fcun(nums, pviot+1, end)
    return nums


def partitions(nums, start=0, end=None):
    if end is None:
        end = len(nums)-1
    left, right = start, end-1
    while right < left:
        if nums[left] <= nums[end]:
            left += 1
        elif nums[right] > nums[end]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end


print(fcun([5, 2, 3, 1]))


ll = [5, 2, 3, 1]
pviot = partitions(ll)
print(ll, pviot)
