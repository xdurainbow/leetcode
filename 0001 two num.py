"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
首先将nums拷贝一份，然后对nums进行排序，按上述方法找到哪两个数的和为目标值，然后在之前备份的数组中查看这两个数值的索引。
这里需要注意的是，由于数组中可能有重复值，例如给定数组为[3,3]，目标值为6，按上述方法返回的是[0,0]，而不是[0,1]。
因此在找到第一个索引值后，把第一个数改变下，只要不和第二个数相等即可，这里采取的方法是设置为第二个值+1，见倒数第三行，
这样就不会在求第二个索引值时受影响。
"""
import copy

class Solution:
    def twoSum(self, nums, target):
        num = copy.deepcopy(nums)
        nums.sort()
        i = 0
        j = len(nums) - 1
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        a = num.index(nums[i])
        #
        num[a] = nums[j] + 1
        b = num.index(nums[j])
        return [a, b]


if __name__ == '__main__':
    num_list = [2, 7, 11, 15]
    tar = 9
    s = Solution()
    print(s.twoSum(num_list, tar))
