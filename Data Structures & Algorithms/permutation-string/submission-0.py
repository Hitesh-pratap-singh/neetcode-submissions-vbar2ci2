class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_freq = {}

        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0)+1

        temp = s1_freq.copy()
        str_len = len(s1)

        for r in range(len(s2)):
            if s2[r] in temp and temp[s2[r]]>0:
                temp[s2[r]] = temp.get(s2[r],0)-1
                str_len-=1
            else:
                temp = s1_freq.copy()
                str_len = len(s1)
            if str_len == 0:
                return True

        return False