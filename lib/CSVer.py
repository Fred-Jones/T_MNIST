##dumb af csv.reader object is wack

import csv
import os

def read_data(datadir='./data'):
    files = os.listdir(datadir)
    dats = []
    for file in files:
        with open(datadir + '/' + file, 'rwb') as csvfile:
            print 'Loading data {}'.format(file)
            dats.append(csv.reader(csvfile, delimiter=','))
    print 'Returned tuple of ({0},{1})'.format(files[0], files[1])
    return dats
