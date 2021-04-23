from unittest import TestCase
import random
import string
import urllib.request

def radixSort(data):
  #Solution Here
  pass

###
# Test Cases
###

def singleDigits():
  tc = TestCase()
  lst = [str(n) for n in list(range(10))[::-1]]
  tc.assertEqual(sorted(lst), radixSort(lst))

def multipleDigits():
  tc = TestCase()
  lst = [str(n) for n in list(range(0, 500, 7))[::-1]]
  tc.assertEqual(sorted(lst), radixSort(lst))

def randomNumbersBase10():
  tc = TestCase()
  lst = [str(random.randint(0, 1000)) for _ in range(200)]
  tc.assertEqual(sorted(lst), radixSort(lst))

def randomStringsSameLength():
  tc = TestCase()
  lst = [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(100)]
  tc.assertEqual(sorted(lst), radixSort(lst))

def randomNumbersBinary():
  tc = TestCase()
  lst = [bin(random.randint(0, 1000)) for _ in range(100)]
  tc.assertEqual(sorted(lst), radixSort(lst))

def randomStringsRandomLength():
  tc = TestCase()
  lst = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5,25))) for _ in range(100)]
  tc.assertEqual(sorted(lst), radixSort(lst))

def book():
  tc = TestCase()
  bookUrl = 'https://www.gutenberg.org/files/84/84-0.txt'
  file = urllib.request.urlopen(bookUrl).read().decode()
  lst = [str(n)[2:-1] for n in file.encode('ascii','replace').split()]
  tc.assertEqual(sorted(lst), radixSort(lst))

###
# Test Helpers
###

def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

###
# Main
###

def main():
    for t in [singleDigits,
              multipleDigits,
              randomNumbersBase10,
              randomStringsSameLength,
              randomNumbersBinary,
              randomStringsRandomLength,
              book]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
