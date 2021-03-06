# This program is a second alternative to the Isomorphic Program written by Linus Okoth
# The main difference is that this program does not use a dictionaries or set so saves on the space complexity.

#Time Complexity: O(N^2) - Update by Chika Jinanwa
#Space Complexity: O(N)

def isomorphic(s,t):
  if len(s) != len(t):
    return False
  else:
    checker=""
    for i in range(len(s)):
        if t[i] not in t[:i] or s[i] in s[:i]:
            if s[i] not in s[:i]:
                checker+=t[i]
            else:
                checker+=t[s.index(s[i])]
    return checker==t


print(isomorphic("foo","bar"))
