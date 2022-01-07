
"""
Created on Tue Jan  4 20:29:00 2022

Author: Michelle Ding

Purpose:
    To convert RA and DEC into degrees
"""

#import
import math

#input RA and DEC

ra = input('Enter RA value in the form H M S or degree: ')
dec = input('Enter DEC value in the form D M S or degree: ')


if bool(ra) == False or bool(dec) == False:
    print('Please enter both RA and DEC values!')
    
    
# if all(x.isalpha() or x.isspace() for x in ra) == False or \
# all(x.isalpha() or x.isspace() for x in dec) == False:
#     print('Please only use numbers and spaces!')
    
    
else:
    if ra.count(' ') == 2 and dec.count(' ') == 2:
    #converts RA and DEC from Hour/Degree:Min:Sec to Degree
    
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
            
    
    if ra.count(' ') == 0 and dec.count(' ') == 0:
    #converts RA and DEC from Degree to Hour/Degree:Min:Sec
    
        RA, DEC, ra_sign, dec_sign = '', '', '', ''
          
        ra, dec = float(ra), float(dec)
          
        while ra > 360:
            ra = ra - 360
        
        while dec > 360:
            dec = dec - 360
          
          
        if dec:
            if str(dec)[0] == '-':
                dec_sign, dec = '-', abs(dec)
          
            D = math.floor(float(dec))
        
            M = abs(math.floor((dec-D)*60))
        
        
            if round:
                S = int((abs((dec-D)*60)-M)*60)
          
          
            else:
                S = (abs((dec-D)*60)-M)*60
          
            DEC = '{0}{1} {2} {3}'.format(dec_sign, D, M, S)
          
          
        if ra:
            if str(ra)[0] == '-':
                ra_sign, ra = '-', abs(ra)
          
            H = math.floor(ra/15)
        
            M = math.floor(((ra/15)-H)*60)
        
        
            if round:
                S = int(((((ra/15)-H)*60)-M)*60)
          
          
            else:
                S = ((((ra/15)-H)*60)-M)*60
          
            RA = '{0}{1} {2} {3}'.format(ra_sign, H, M, S)
            
        
        else:
            print('Input of the wrong format')
        

    print ('RA = ' + str(RA), 'DEC = ' + str(DEC))

