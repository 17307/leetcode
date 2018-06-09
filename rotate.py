# coding = utf8

"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

思路：先将矩阵转置，然后每一行翻转
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        assert isinstance(matrix, list)
        length = len(matrix)
        j = 0
        # 对矩阵做转置
        while j < length:
            k = j
            while k < length:
                # swap(matrix[j][k],matrix[k][j])
                temp = matrix[j][k]
                matrix[j][k] = matrix[k][j]
                matrix[k][j] = temp
                k += 1
            j += 1
        i = 0
        while i < length:
            matrix[i].reverse()
            i += 1


if __name__ == "__main__":
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s = Solution()
    s.rotate(matrix)
