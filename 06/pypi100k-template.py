import urllib.request
import xmlrpc.client
import arrow

NUM_PACKS_TO_REACH = 100000
PYPI = 'https://pypi.python.org/pypi'

def get_packages(timestamp):
    client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')
    changes = client.changelog(timestamp)
    return changes

def package_list():
    pack_list = urllib.request.urlopen('https://www.pypi.org/simple/')
    return pack_list.read()

if __name__ == "__main__":
    print('PyPI hit 100,000 packages on March 4th, 2017! https://twitter.com/pybites/status/838178449999081472')
    print("Here's when we estimate PyPI will hit 200,000 packages:")
    current_time = arrow.utcnow()
    print(current_time)
    print(current_time.timestamp)
    print(len(get_packages(current_time.timestamp)))
    for i in range(24):
        if current_time.month == 1:
            current_time = current_time.replace(years=-1)
            current_time = current_time.replace(month = 12)
            # call package list
            #print(current_time)
            print(current_time.date)
            print(len(get_packages(current_time.timestamp)))
        else:
            current_time = current_time.replace(month = (current_time.month - 1))
            #call package list
            #print(current_time)
            print(current_time.date)
            print(len(get_packages(current_time.timestamp)))
#    print(package_list())
