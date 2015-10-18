##dumb af csv.reader object is wack

import csv
import os

def read_data(datadir='./data'):
    files = os.listdir(datadir)
    dats = []
    for file in files:
        with open(datadir + '/' + file, 'rw') as csvfile:
            print 'Loading data {}'.format(file)
            dats.append(csv.reader(csvfile, delimiter=','))
    return dats
