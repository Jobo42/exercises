'''
Write a function that accepts two parameters, a parent and a child string. 
Determine how many times the child string - or an anagram of the child string - appears in the parent string. 
There is a solution which can be done in near instant time.

f('AdnBndAndBdaBn', 'dAn') // 4 ("Adn", "ndA", "dAn", "And")
f('AbrAcadAbRa', 'cAda') // 2
'''

def detect_anagrams(parent, child):
    anagrams = []

    for i in range(len(parent) - len(child)):
        letter = parent[i]

        if letter in child:
                word = parent[i:i+len(child)]

                if is_anagram(word, child):
                    anagrams.append(word)
    return anagrams

# Strings must be the same length
def is_anagram(s1, s2):
    for letter in s1:
        if s1.count(letter) != s2.count(letter):
            return False
    return True


phrase = "AdnBndAndBdaBn"
key = "dAn"

anagrams = detect_anagrams(phrase, key)
print(anagrams)
