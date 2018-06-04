# coding=utf-8
"""
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        assert isinstance(digits, list)
        # 判断位数
        length = len(digits)
        i = length - 1
        while i >= 0:
            # 找出不是9的位数
            if digits[i] == 9:
                i -= 1
                continue
            else:
                # 此位+1，后面置0
                digits[i] += 1
                while i < length - 1:
                    digits[i + 1] = 0
                    i += 1
                return digits
        # 如果全是9的话
        if i == -1:
            new_digits = [1]
            while i < length - 1:
                new_digits.append(0)
                i += 1
            return new_digits


if __name__ == "__main__":
    s = Solution()
    digits = [9, 9, 9]
    print(s.plusOne(digits))
