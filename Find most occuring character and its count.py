from collections import Counter

sentence = input("Enter the string: ")

res = Counter(sentence)

max_key = max(res, key = res.get)

print(max_key, res[max_key])
