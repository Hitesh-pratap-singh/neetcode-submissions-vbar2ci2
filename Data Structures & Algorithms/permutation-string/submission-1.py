class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_freq = {}

        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0)+1

        temp = s1_freq.copy()
        # str_len = len(s1)

        l,r = 0,0

        while r<len(s2) and l<len(s2):
            if s2[r] in temp and temp[s2[r]]>0:
                temp[s2[r]] -= 1 
                if r-l+1 == len(s1):
                    return True
                r+=1
            elif s2[r] in temp and temp[s2[r]]==0:
                temp[s2[l]]+=1
                l+=1
            else:
                r+=1
                l=r

        return False