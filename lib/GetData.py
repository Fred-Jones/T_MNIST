import os
import pandas as pd

def read_csv(datadir='./data'):
    files = os.listdir(datadir)
    dats = ()
    for file in files:
        print 'Loading {} ...'.format(file)
        with open(datadir + '/' + file, 'r') as csvfile:
            dats += (pd.read_csv(csvfile, header=0),)
    print 'Completed: convert .csv files to pd.d\nReturns dict object'
    return dats
