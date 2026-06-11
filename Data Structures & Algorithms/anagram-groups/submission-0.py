class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 #a to z 

            for c in s:
                count[ord(c) - ord("a")] += 1 #Ascii value of current char - ascii value of "A"
                                         # 100(d) - 97
            res[tuple(count)].append(s) 

        return list(res.values())                      
