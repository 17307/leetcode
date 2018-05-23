# coding=utf8
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
[1,2,3,4,4,5]
[1,2,2]
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int] 有序数组
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 2:  # 数组为空或者只有1个元素则直接返回
            return nums_len
        i = 0
        j = -1
        while i < nums_len:
            if j == -1:
                '''查找第一个重复元素,并把i放到第一个重复元素的j的后边'''
                if i < nums_len - 1 and nums[i] == nums[i + 1]:
                    j = i + 1
                    i = j + 1
                else:
                    i += 1
            else:
                '''如果元素i与j-1不等，则把j覆盖'''
                if nums[i] != nums[j - 1]:
                    nums[j] = nums[i]
                    j += 1
                i += 1
        if j < 0:  # i<0说明没有重复元素
            return nums_len
        return j