class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word, index, count):
        node = self.root
        for i in range(index, len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if node.end:
                if i == len(word) - 1:
                    return count >= 1
                if self.search(word, i + 1, count + 1):
                    return True
        return False

def process_file(file_name):
    import time
    start_time = time.time()
    with open(file_name, 'r') as f:
        words = [line.strip() for line in f]
    trie = Trie()
    for word in words:
        trie.insert(word)

    longest_word = ''
    second_longest_word = ''
    for word in words:
        if trie.search(word, 0, 0):
            if len(word) > len(longest_word):
                second_longest_word = longest_word
                longest_word = word
            elif len(word) > len(second_longest_word):
                second_longest_word = word
    end_time = time.time()
    print(f'Longest Compound Word: {longest_word}')
    print(f'Second Longest Compound Word: {second_longest_word}')
    print(f'Time taken to process file {file_name}: {end_time - start_time} seconds')

process_file('Input_01.txt')
process_file('Input_02.txt')
