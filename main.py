from data_structures.trie import Trie

trie = Trie()

trie.add("apple")
trie.add("application")
trie.add("apply")


words = trie.words_with_prefix("app")
print(words)

print(trie.longest_common_prefix())
