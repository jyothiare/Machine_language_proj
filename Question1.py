# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:32:23 2018

@author: basind
"""

# Python program to search all
# anagrams of a pattern in a text
 
MAX=256
 
# This function returns true
# if contents of arr1[] and arr2[]
# are same, otherwise false.
def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True
     
# This function search for all
# permutations of pat[] in txt[]  
def search(pat, txt):
 
    M = len(pat)
    N = len(txt)
 
    # countP[]:  Store count of
    # all characters of pattern
    # countTW[]: Store count of
    # current window of text
    countP = []
 
    for i in range(MAX):
        countP.append(0)
 
    countTW = []
 
    for i in range(MAX):
        countTW.append(0)
 
    for i in range(M):
        (countP[ ord(pat[i]) ]) += 1
        (countTW[ ord(txt[i]) ]) += 1
 
    # Traverse through remaining
    # characters of pattern
    for i in range(M,N):
 
        # Compare counts of current
        # window of text with
        # counts of pattern[]
        if compare(countP, countTW):
            print("Found at Index", (i-M))
 
        # Add current character to current window
        (countTW[ ord(txt[i]) ]) += 1
 
        # Remove the first character of previous window
        (countTW[ ord(txt[i-M]) ]) -= 1
     
    # Check for the last window in text    
    if compare(countP, countTW):
        print("Found at Index", N-M)
         
# Driver program to test above function       
txt = "UDACITY"
pat = "DY"      
search(pat, txt)   
 
# This code is contributed
# by Upendra Singh Bartwal


def is_anagram(s1, s2):
    s1 = list(s1)
    # Sort a string and then compare with each other
    s1.sort()   # Quick sort O(n*log(n))
    return s1 == s2

# Find out sorted(possible substring of s) and compare with sorted(t).
# @param {string, string} input strings
# @return {bool} Question1 answer
def question1(s, t):
    global debug
    match_length = len(t)
    pattern_length = len(s)
    sorted_t = list(t)
    sorted_t.sort()     # Quick sort O(n*log(n))

    for i in range(pattern_length - match_length + 1):
        if debug:
            print (s[i: i+match_length], t)
        if is_anagram(s[i: i+match_length], sorted_t):
            return True
    return False