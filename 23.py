# coding=utf-8
'''
这道题有种类似翻转字符的方法，思路是先把前n-k个数字翻转一下，再把后k个数字翻转一下，最后再把整个数组翻转一下
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        step = len(nums)
        while k > step:
            k = k % step
        # 获取第一次需要取逆的
        step_pre = (step - k)
        i = 0
        while i < step_pre / 2:
            #   swap(nums[i], nums[step_pre - i - 1])
            temp = nums[i]
            nums[i] = nums[step_pre - i - 1]
            nums[step_pre - i - 1] = temp
            i += 1
        print(nums)

        # 获取第二次需要取逆的  k
        step_nex = k / 2
        i = 0

        while i < step_nex:
            # swap(nums[k+i],nums[step-i-1])
            temp = nums[step - k + i]
            nums[step - k + i] = nums[step - i - 1]
            nums[step - i - 1] = temp
            i += 1
        print(nums)
        # 整体取逆
        i = 0
        count = step / 2
        while i < count:
            # swap(nums[i],nums[step-i])
            temp = nums[i]
            nums[i] = nums[step - i - 1]
            nums[step - i - 1] = temp
            i += 1
        print(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]

    k = 11
    s = Solution()
    s.rotate(nums, k)
