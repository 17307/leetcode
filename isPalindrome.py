class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[]
        for i in range(len(s)):
            if s[i].isalnum():#选择字母或数字
                s1.append(s[i].lower())
        if s1==s1[::-1]:#翻转后是否与之前的相等
            return True
        else:
            return False
