import collections
def group_anagrams(strs):
    anagrams=collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams

token=['eat','tae','tan','ate','nat','bat']
res=group_anagrams(token)
print(res)