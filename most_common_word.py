import collections
import re
paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
word=[word for word in re.sub('[^\w]',' ',paragraph)
.lower().split() if word not in banned]
count=collections.Counter(word)
print(count.most_common(1))