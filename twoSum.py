# coding=utf-8
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert isinstance(nums, list)
        length = len(nums)
        i = 0
        nums_dict = dict()
        while i < length:
            nums_dict[nums[i]] = i
            i += 1
        i = 0
        while i < length:
            left = target - nums[i]
            if left in nums_dict:
                if nums_dict[left] != i:
                    return [i, nums_dict[left]]
            i += 1

    def twoSum2(self, nums, target):
        assert isinstance(nums, list)
        i = 0
        length = len(nums)
        while i < length:
            left = target - nums[i]
            if left == nums[i]:
                try:
                    if nums.index(left, i + 1, length):
                        return [i, nums.index(left, i + 1, length)]
                except:
                    pass
            try:
                if nums.index(left) != i:
                    return [i, nums.index(left)]
            except:
                pass
            finally:
                i += 1


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 1]
    target =
