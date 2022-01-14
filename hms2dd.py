
"""
Created on Tue Jan  4 20:29:00 2022

Author: Michelle Ding

Purpose:
    To generate a new csv file of RA and DEC coordinates in Degrees decimal form
"""

#import
import csv
import numpy as np

#input RA and DEC

# ra = input('Enter RA value in the form H M S or degree: ')
# dec = input('Enter DEC value in the form D M S or degree: ')

hms_coord = r"E:\GRAVITATIONAL LENSING\HMS_coord.csv"
dd_coord = r"E:\GRAVITATIONAL LENSING\DD_coord.csv"

def hms2dd(ra, dec):    
    RA, DEC, ra_sign, dec_sign = '', '', 1, 1
      
    if dec:
        D, M, S = [float(i) for i in dec.split()]
    
    
        if str(D)[0] == '-':
            dec_sign, D = -1, abs(D)
          
        deg = D + (M/60) + (S/3600)
        
        DEC = '{0}'.format(deg*dec_sign)
    
    
    if ra:
        H, M, S = [float(i) for i in ra.split()]
    
        if str(H)[0] == '-':
            ra_sign, H = -1, abs(H)
          
        deg = 15*(H + (M/60) + (S/3600))
        
        RA = '{0}'.format(deg*ra_sign)
        
        
        RA, DEC = float(RA), float(DEC)
        
        while RA > 360:
            RA = RA - 360
        
        while DEC > 360:
            DEC = DEC - 360
            
    return [RA, DEC]

def convert_line(data):
    return data[0], hms2dd(data[1], data[2])

with open(hms_coord) as infile:
    reader = csv.reader(infile)
    with open(dd_coord) as outfile:
        writer = csv.writer(outfile)
        #writer.writerow(next(reader))
        for line in reader:
            writer.writerow(convert_line(line))
