# coding=utf-8
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        assert isinstance(nums, list)

        length = len(nums)
        # 判断0是否存在
        try:
            flag = nums.index(0)
        except ValueError:
            return nums
        # 从0的下一个数开始，让后面的数取代前面的flag位置
        i = flag + 1
        while i < length:
            if nums[i] != 0:
                nums[flag] = nums[i]
                flag += 1
            i += 1
        # 把后面的数置0
        while flag < length:
            nums[flag] = 0
            flag += 1
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 0, 7]
    nums2 = [0, 1, 0, 3, 12]
    print(s.moveZeroes(nums2))
