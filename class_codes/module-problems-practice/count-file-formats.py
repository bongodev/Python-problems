import os

files = os.listdir("files")

extensions = []

for file in files:
    filename_parts = file.split(".")
    extension = filename_parts[-1]
    extensions.append(extension)

# print(extensions)

# find count without library function
unique_exts = list(set(extensions))

countTotal = {}

for ext in unique_exts:
    count = extensions.count(ext)
    countTotal[ext] = count


print(countTotal)

# find count with library function
from collections import Counter

countTotalUsingLibrary = Counter(extensions)
print(countTotalUsingLibrary)
