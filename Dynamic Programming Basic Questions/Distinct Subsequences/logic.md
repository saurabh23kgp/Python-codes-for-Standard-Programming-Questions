# Distinct Subsequences

This is an easy one. For base cases, the length of the longer string can never be smaller than the length of the shorter string. Also,
if the length of the shorter string is 0, then the number of ways to find the distinct subsequences of the shorter string is 1 and only 1
(think why?)

For all other cases, if last letter of both the strings do not match, then find leave apart the last word of longer string and find the
shorter string in remaining part of the longer string.

If last letter of both the strings match, then we can do 2 things:-

1) Ignore the last letter of longer string as above and find the ways to find smaller string in larger string accordingly.

2) Consider the last letter matched, remove the last letter of both shorter and longer strings and then find the remaining shorter string 
in remaining longer string

Add number of ways of doing 1) and 2).
