**Word Composition Program**

This program identifies the longest and second longest compound words in a given list of words. A compound word is defined as a word that can be constructed by concatenating shorter words also found in the list.

**Overview**

The program uses a Trie data structure for efficient word lookup. Each node in the Trie represents a character, and a flag at each node indicates the end of a word. This allows for quick insertion and search operations, making it ideal for this problem.

The main optimization in this version of the program is to avoid sorting the entire list of words, which can be costly for large lists. Instead, we keep track of the longest and second longest compound words as we process each word.

**Steps to Execute**

1. Ensure that Python is installed on your system.
2. Save the Python script in a file, say word_comp.py.
3. Prepare your input files with words. Each word should be on a new line.
4. Open a terminal/command prompt.
5. Navigate to the directory where you saved word_comp.py.
6. Run the script with the command python word_comp.py.

Please replace 'Input_01.txt' and 'Input_02.txt' in the script with the paths to your actual files.

**Design Decisions and Approach**

The decision to use a Trie was based on its efficient search and insert operations. The Trie allows us to quickly determine if a word can be constructed from other words in the list.

The approach taken was to first insert all the words into the Trie. Then, for each word in the list, we check if it is a compound word by searching for its constituent parts in the Trie. We keep track of the longest and second longest compound words as we process each word.
