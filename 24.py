# coding=utf-8
"""
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return False

        assert isinstance(nums, list)
        nums.sort()
        l = len(nums)
        i = 0
        while i < l:
            if i == l - 1:
                return False
            if nums[i] == nums[i + 1]:
                return True
            i += 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]

    print(s.containsDuplicate(nums))
