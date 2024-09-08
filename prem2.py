def wordBreak(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                break

    return 1 if dp[n] else 0


n = int(input("Enter the number of words in the dictionary: "))
dictionary = set(input("Enter the words in the dictionary: ").split())
s = input("Enter the string s: ")


result = wordBreak(s, dictionary)
print(result)