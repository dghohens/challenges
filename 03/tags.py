from itertools import product
from difflib import SequenceMatcher
import re

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
rssfile = open(RSS_FEED)
rssread = rssfile.read()

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags1 = TAG_HTML.findall(rssread)
    tags1 = [w.replace('-', ' ') for w in tags1]
    return tags1


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    tagsd2 = {}
    for i in tags:
        if i in tagsd2:
            tagsd2[i] += 1
        else:
            tagsd2[i] = 1
    tagsd2 = sorted(tagsd2.items(), key = lambda x: x[1],reverse = True)
    return tagsd2


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    simtags3 = []
    for i in tags:
        prodtags3 = list(product([i,''], tags))
        for j in prodtags3:
            seqtags3 = SequenceMatcher(None, j[0].lower(), j[1].lower())
            if seqtags3.ratio() != 0.0 and seqtags3.ratio() >= SIMILAR and seqtags3.ratio() != 1.0:
                if j[0] not in [i for i in simtags3]:

    return simtags3
'''
if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
'''

get_similarities(get_tags())

