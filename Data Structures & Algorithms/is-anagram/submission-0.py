class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_table_s = {}
        freq_table_t = {}

        # itr = 0
        for itr in range(len(s)):
            if s[itr] in freq_table_s:
                freq_table_s[s[itr]] = freq_table_s[s[itr]]+1
            else:
                freq_table_s[s[itr]] = 0

        # itr = 0
        for itr in range(len(t)):
            if t[itr] in freq_table_t:
                freq_table_t[t[itr]] = freq_table_t[t[itr]]+1
            else:
                freq_table_t[t[itr]] = 0

                
        for key, value in freq_table_s.items():
            if key not in freq_table_t:
                return False
            elif freq_table_t[key] != value:
                return False
        
        return True
