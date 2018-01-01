'''Given a rotated sorted array, find the index of the pivot '''

print(__doc__)


def find_index(words, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(words)-1
    if low > high:
        return 0
    if low == high:
        return low

    mid = (low + high) // 2

    if mid < high and words[mid+1][0] < words[mid][0]:
        return mid+1
    if mid > low and words[mid-1][0] > words[mid][0]:
        return mid
    if words[high][0] > words[mid][0]:
        return find_index(words, low, mid-1)

    return find_index(words, mid+1, high)

def main():
    test_cases = [['ptolemaic', 'quixotic',  'retrograde', 'supplant', 'undulate', 'xenoepist',
                   'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'],
                  ['babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage', 'ptolemaic',
                   'quixotic',  'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote'],
                  ['asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage',
                   'ptolemaic', 'quixotic',  'retrograde', 'supplant', 'undulate', 'xenoepist']]

    for case in test_cases:
        print(find_index(case))

if __name__ == '__main__':
    main()