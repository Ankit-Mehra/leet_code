class Solution:
    def findCommon(self, a, b):
        string = ""
        for i in range(min(len(a), len(b))):
            if (a[i]!=b[i]):
                break
            string += a[i]
        return string
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxi = strs[0]
        for i in strs[1:]:
            maxi = self.findCommon(maxi, i)
            if (maxi == ""):
                break
        return maxi
        
            
strs = ["a","a","b"]
print(solulongestCommonPrefix(strs))    
