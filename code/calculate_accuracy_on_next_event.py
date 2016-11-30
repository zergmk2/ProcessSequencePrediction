'''
this script takes as input the output of evaluate.py
therefore, evaluate.py needs to be executed first

Author: Niek Tax
'''

from __future__ import division
import unicodecsv

csvfile = open('output_files/folds/fold3_preds_bpi13_indicent.csv', 'r')
r = unicodecsv.reader(csvfile ,encoding='utf-8')
r.next() # header
vals = dict()
for row in r:
    l = list()
    if row[0] in vals.keys():
        l = vals.get(row[0])
    if len(row[1])==0 and len(row[2])==0:
        l.append(1)
    elif len(row[1])==0 and len(row[2])>0:
        l.append(0)
    elif len(row[1])>0 and len(row[2])==0:
        l.append(0)
    else:
        l.append(int(row[1][0]==row[2][0]))
    vals[row[0]] = l
    #print(vals)
    
l2 = list()
for k in vals.keys():
    #print('{}: {}'.format(k, vals[k]))
    l2.extend(vals[k])
    res = sum(vals[k])/len(vals[k])
    print('{}: {}'.format(k, res))

print('total: {}'.format(sum(l2)/len(l2)))