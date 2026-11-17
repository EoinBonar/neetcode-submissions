class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = dict()
        length = len(s)
        
        for x in s:
            dic[x] = dic.get(x,0) + 1

        for y in t:
            dic[y] = dic.get(y,0) - 1

        return(all(v == 0 for v in dic.values()))
        