#!/usr/bin/env python3

import logging, re
from dateAndY import gen_date_and_y

msg = '''
(O< .: Collect dates (x_axis) and corresponding weight measurements (y_axis)
(/)_   from my daily logfile.
'''
dailyLog = "/home/dwa/share/log/daily.log"
weightLog = "/home/dwa/share/log/dateAndWeight.log"

def weight_sub(logfile):
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
    with open(logfile, 'w') as f:
        lbs = re.compile(r'^(#weight\s)(\d\d\d\.\d)')
        kg = re.compile(r'^(#weight\s)(\d\d\.\d)')
        for line in searchLines:
            # Convert lbs to kg and remove tags
            if lbs.search(line) != None:
                mo = lbs.search(line)
                k = float(mo.group(2)) / 2.2046 # metric conversion
                line = re.sub(r'#weight\s\d\d\d\.\d', str(round(k, 1)), line)
                f.write(line)
            # Remove tags
            elif kg.search(line) != None:
                mo = kg.search(line)
                line = re.sub(r'#weight\s\d\d\.\d', str(mo.group(2)), line)
                f.write(line)
            else:
                f.write(line)

if __name__ == '__main__':
    gen_date_and_y(dailyLog, weightLog, '^201[4-9]-\d\d-\d\d', '^#weight\s\d\d...?')
    weight_sub(weightLog)
