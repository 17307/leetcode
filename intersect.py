# coding=utf-8

"""
给定两个数组，写一个方法来计算它们的交集。
例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
"""
import collections


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = collections.Counter(nums1)
        dic2 = collections.Counter(nums2)

        both = [i for i in dic1.keys() if i in dic2.keys()]  # 找到两者共有的值
        res = []
        for i in both:
            res.extend([i] * min(dic1[i], dic2[i]))
        return res


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2,1]
    print(s.intersect(nums2, nums1))
