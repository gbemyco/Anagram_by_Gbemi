# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    return True

#Task Solution:
def find_anagram(word, anagram):
    a=list(word)
    b=list(anagram)
    list.sort(a)
    list.sort(b)
    if (a == b):
        return True
    else:
        return False
print(find_anagram('listened', 'enlisted'))
#Eureka!
