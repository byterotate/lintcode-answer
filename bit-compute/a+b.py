class Solution:
    """
    注意这里用python会导致超时，实际是使用c++通过的
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
      while b != 0:
        olda = a
        oldb = b
        a = olda ^ oldb
        b = (olda & oldb) << 1
      return a