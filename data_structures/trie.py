class Trie:
    def add(self, word):
        dict_so_far = self.root

        for c in word:
            if c not in dict_so_far:
                dict_so_far[c] = {}
            dict_so_far = dict_so_far[c]

        dict_so_far[self.end_symbol] = True
            
    def exists(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
            
        return self.end_symbol in current

    def __search_level(self, current_level: dict, current_prefix: str, words: list[str]) -> list[str]:
        if self.end_symbol in current_level:
            words.append(current_prefix)

        sorted_chars = list(
            filter(
                lambda c: c != self.end_symbol,
                sorted(current_level)
            )
        )

        for letter in sorted_chars:
            prefix_so_far = current_prefix + letter
            self.__search_level(current_level[letter], prefix_so_far, words)

        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        matched_words = []
        current_level = self.root

        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]

        return self.__search_level(current_level, prefix, matched_words)
            
    def find_matches(self, document: str) -> set[str]:
        matches = set()
        
        for i in range(len(document)):
            level_so_far = self.root

            for j in range(i, len(document)):
                current_end_substr = document[j]
                
                if current_end_substr not in level_so_far:
                    break
                
                level_so_far = level_so_far[current_end_substr]
                if self.end_symbol in level_so_far:
                    found_substr = document[i:j + 1]
                    matches.add(found_substr)

        return matches
        
    def longest_common_prefix(self) -> str:
        current = self.root
        prefix = ""

        while True:
            childrens = list(current.keys())

            if self.end_symbol in childrens:
                break
            
            if len(childrens) == 0 or len(childrens) > 1:
                break

            prefix += childrens[0]
            current = current[childrens[0]]
        
        return prefix


    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

