from functools import reduce

# initializing string
test_str = "GeeksforGeeks"

# using reduce to get count of each element in string
all_freq = dict(reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, test_str, {}))

# printing result
print("Count of all characters in GeeksforGeeks is :\n " + str(all_freq))
#This code is contributed by Vinay Pinjala.
