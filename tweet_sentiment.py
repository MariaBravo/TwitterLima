__author__ = 'luchy'

import sys
import json
import re

fc = open("/home/luchy/Desktop/thebuzz", mode='a')


def hw():
    print ('Hello, world!')

def lines(fp):
    # print (str(len(fp.readlines())))

    fp.seek(0,0)
    for l in fp:
        try:
            value = json.loads(l)

            try:
                value2 = value[u'text']
            except:
                value2 = ''

            try:
                value3 = value[u'place']
                try:
                    value3a = value3[u'country']
                except:
                    value3a = ''
                try:
                    value3b = value3[u'country_code']
                except:
                    value3b = ''
                try:
                    value3c = value3[u'full_name']
                except:
                    value3c = ''
                try:
                    value3d = value3[u'name']
                except:
                    value3d = ''
            except:
                value3 = ''

            r1 = re.search('Peru', value2)
            r2 = re.search('Lima', value2)

            r3 = re.search('Peru', value3c)
            r4 = re.search('Lima', value3c)

            r5 = re.search('Peru', value3d)
            r6 = re.search('Lima', value3d)

            if ((value3a == 'Peru') or (value3b == 'PE') or (r1 != None) or (r2 != None) or (r3 != None) or (r4 != None) or (r5 != None) or (r6 != None)):
                fc.write(l + '\n')
                # print(l)

        except:
            value = ''



def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1], "rt")

    hw()
    # lines(sent_file)
    lines(tweet_file)
    fc.close()

if __name__ == '__main__':
    main()