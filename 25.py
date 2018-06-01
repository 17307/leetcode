# -*- coding: utf-8 -*-
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""
'''
思路：所有元素异或---最后剩下一个
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        res = 0
        while i < length:
            res ^= nums[i]
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1, 2, 3, 4, 4, 5]
    print(s.singleNumber(nums))
