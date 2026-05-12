from hash_map import HashMap
from DoublyLinkedList import DoublyLinkedList

# We need a data structure to store all the words in the list of English words as well as a means of grouping anagrams together. What data structure should we use and what how should we store the words and anagrams?
"""
I want to say we store the words inside a list, and to group anagrams together we use a hashmap, that way we can iterate over the entire list and add the anagrams to the hashmap as we go. The key should be something that anagrams share, meaning they should all go into the same bucket, and inside the bucket is each and every word that is an anagram with each and every other word in that bucket
"""
# How do we know if two words are anagrams?
"""
We know two words are anagrams if they contain the same frequency of characters, so we must maintain a count of each character using hashmap to then map each one properly to a bucket in which the key is a hash of the calculate character frequency
"""
# How do we process the words in the file storing the list of English words and place them into the data structure?

def h(word):
    letters = [l.lower() for l in word]
    sorted_letters = sorted(letters)
    key = ''.join(sorted_letters)
    return key

def main():
    map = {}
    file_name = 'Dictionary.txt'
    max_len = 0
    with open(file_name, 'r') as dict_words:
        for line in dict_words:
            word = line.strip()
            key = h(word)
            if key in map:
                word_list = map.get(key)
                word_list.append(word)
                if max_len > len(word_list)+1:
                    max_len = len(word_list)
            else:
                map[key] = [word]

    print(map[h('listen')])
    print(map[h('trance')])
    print(map[h('weakliness')])

"""
This, to me is the simplest way to add them all to a list, but I feel like since we don't want to use more than one loop, we should process each word line by line and place it into the hashmap based on its calculated character frequency, and skip the list step all together 
"""

if __name__ == '__main__':
    main()

