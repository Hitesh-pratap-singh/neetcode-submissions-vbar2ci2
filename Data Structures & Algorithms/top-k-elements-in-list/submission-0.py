class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = {}
        result = []

        for num in nums:
            if num in freq_arr:
                freq_arr[num] += 1
            else:
                freq_arr[num] = 0

        
        sorted_freq_arr = dict(sorted(freq_arr.items(), key=lambda item: item[1]))
        print(sorted_freq_arr)
        idx = 1
        for key, value in sorted_freq_arr.items():
            print(len(sorted_freq_arr)-idx, k)
            if len(sorted_freq_arr)-idx < k:
                result.append(key)
            idx += 1

        return result

