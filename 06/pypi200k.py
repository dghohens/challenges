import urllib.request
import xmlrpc.client
import re
from time import sleep
from collections import Counter, OrderedDict

NUM_PACKS_TO_REACH = 100000
PYPI = 'https://pypi.python.org/pypi'

def get_packages(timestamp):
    client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')
    changes = client.changelog(timestamp)
    return changes

def package_list():
    ''' This function pulls all packages from pypi.org/simple and returns a list of the package names.
    I'm only going to check 1/100 of the packages to save memory and API calls.'''
    pack_regex = re.compile(b'">(\S+)</a>')
    pack_list1 = urllib.request.urlopen('https://www.pypi.org/simple/')
    pack_list2 = pack_list1.read()
    pack_list3 = pack_list2.split(b'\n')
    pack_list4 = []

    for i in pack_list3[6:-2:1000]:
        a = pack_regex.search(i)
        pack_list4.append(a.group(1).decode('utf-8'))

    return pack_list4

def get_dates(packagelist):
    '''Check dates from pypi.org/pypi/<package>/json, strip out dates, find first date. Return list of all first upload dates.'''
    first_dates = []
    date_regex = re.compile(b'_time":"(\d\d\d\d-\d\d-\d\d)T\d\d')
    for i in packagelist:
        a = ''
        print(i)
        try:
            b = urllib.request.urlopen('https://www.pypi.org/pypi/%s/json' % i).read()
            c = date_regex.findall(b)
            a = c[0]
            for i in c:
                if i < a:
                    a = i
            print(a.decode())
            first_dates.append(a.decode())
        except urllib.error.HTTPError as e:
            print(e)
        except IndexError as f:
            print(f)

        sleep(.5)

    return first_dates

def package_number_history(date_list):
    total_packages = 0
    historical_counts = {}
    date_counts = dict(Counter(date_list))
    ordered_date_counts = OrderedDict(sorted(date_counts.items()))
    for i,j in ordered_date_counts.items():
        total_packages += j
        historical_counts[i] = total_packages

    return historical_counts


if __name__ == "__main__":
    print('PyPI hit 100,000 packages on March 4th, 2017! https://twitter.com/pybites/status/838178449999081472')
    print("Here's when we estimate PyPI will hit 200,000 packages:")

    packlist = package_list()
    print(packlist)
    print(len(packlist))
    upload_dates = get_dates(packlist)
    running_total = package_number_history(upload_dates)
    print(running_total)
