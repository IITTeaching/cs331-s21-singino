import urllib.request
from unittest import TestCase

def cleanData(data, maxLen):
  lst = []
  for item in data:
    if isinstance(item, int):
      itemList = list(str(item))
      lst.append(['\0'] * (maxLen-len(itemList)) + itemList)
    elif isinstance(item, str):
      itemList = list(item)
      lst.append(itemList + ['\0'] * (maxLen-len(itemList)))
  return lst

def largest(data):
  largest = len(str(data[0]))
  for item in data[1:]:
    if len(str(item)) > largest:
      largest = len(str(item))
  return largest

def positionSort(lst, pos):
  bucketSize = 256
  buckets = [[] for _ in range(bucketSize)]
  for item in lst:
    buckets[ord(item[pos]) % bucketSize].append(item)
  return [item for bucket in buckets for item in bucket]

def radixSort(data):
  maxLen = largest(data)
  lst = cleanData(data, maxLen)
  for n in range(maxLen):
    lst = positionSort(lst, maxLen - n - 1)
  lst = [item.strip('\0') for item in [''.join(item) for item in lst]]
  for n in range(len(lst)):
    if isinstance(data[n], int):
      lst[n] = int(lst[n])
    elif isinstance(data[n], float):
      lst[n] = float(lst[n])
  return lst

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
  file = urllib.request.urlopen(book_url).read().decode()
  lst = [str(n)[2:-1] for n in file.encode('ascii','replace').split()]
  sortedBook = radixSort(lst)

  tc = TestCase()
  tc.assertEqual(sorted(lst), sortedBook)

  return sortedBook

radix_a_book()
