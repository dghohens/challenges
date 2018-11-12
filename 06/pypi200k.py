import urllib.request

NUM_PACKS_TO_REACH = 100000
PYPI = 'https://pypi.python.org/pypi'

def package_list():
    pack_list = urllib.request.urlopen('https://www.pypi.org/simple/')
    return pack_list.read()

if __name__ == "__main__":
    print('PyPI hit 100,000 packages on March 4th, 2017! https://twitter.com/pybites/status/838178449999081472')
    print("Here's when we estimate PyPI will hit 200,000 packages:")
    print(package_list())
