# Enumerate in action
words = ["Hey", "there"]
for i, word in enumerate(words, 1):
    print(f"'Word #{i}: <{word}> has {len(word)} letters.'")

print()
# for i, v in enumerate('abc', start=-100):
#     print(i)

# for tup in enumerate('abc'):
#     print(tup)

pages = [5, 17, 31, 50]
for i, (start, end) in enumerate(zip(pages, pages[1:]), 1):
    # print(start,end,sep='-')
    print(f"'{i}: {start}-{end} is {end - start} pages long.'")

# Enumerate can be used in filtering indices
nums = [4071, 53901, 96045, 84886, 5228, 20108, 42468, 89385, 22040, 18800, 4071]
odd = lambda x: x % 2

result = [i for i, num in enumerate(nums) if odd(num)]
print(result)

print()
# Table of content like feature
starts = [1, 10, 21, 30]
stops = [9, 15, 28, 52]
print(dict(enumerate(zip(starts, stops))))
