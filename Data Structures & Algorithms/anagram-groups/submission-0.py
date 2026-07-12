class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        results = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sorted_map:
                sorted_map[sorted_word].append(word)
            else:
                sorted_map[sorted_word] = [word]

        for k, v in sorted_map.items():
            results.append(v)

        return results
        