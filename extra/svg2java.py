#!/usr/bin/python

# This was a quick hack for generating the star in the visual hash.

svg = 'M 1.7e-7,1037.1448 1.8773281,1042.9725 8,1042.9575 l -4.9624192,3.5863 1.9066909,5.8183 L -4e-8,1048.7502 -4.9442721,1052.3616 -3.0375809,1046.5433 -8,1042.957 l 6.1226718,0.015 z'

svg = 'M 2.2734424e-7,-8.4756811 1.8936006,-2.5973891 8.0693433,-2.6129598 3.0639101,1.0044533 4.9871282,6.873122 1.2638481e-8,3.2305143 -4.9871286,6.8731218 l 1.9232185,-5.8686685 -5.0054331,-3.6174135 6.1757426,0.015571 z'

# plus
svg = 'm 2.0844584,-2.1170607 5.8652343,0 0,4.296875 -5.8652343,0 0,5.8652344 -4.296875,0 0,-5.8652344 -5.8652344,0 0,-4.296875 5.8652344,0 0,-5.8759765 4.296875,0 0,5.8759765'

# X

svg = 'M 3.7239628,0.06047535 8.0833378,4.4198503 4.4388065,8.0643816 0.07943153,3.7050066 -4.2799435,8.0643816 -7.9244747,4.4198503 l 4.359375,-4.35937495 -4.359375,-4.35937505 3.6445312,-3.6445312 4.35937503,4.359375 4.35937497,-4.3710938 3.6445313,3.6445313 -4.359375,4.37109375'

mode = ''
obj = 'X'
for p in svg.split(' '):
    if p == 'M':
        mode = 'lineTo'
    elif p == 'm':
        mode = 'rLineTo'
    elif p == 'L':
        mode = 'lineTo'
    elif p == 'l':
        mode = 'rLineTo'
    elif p == 'z':
        pass
    else:
        (x,y) = p.split(',')
        print "%s.%s(%ff,%ff);" % (obj, mode, float(x), float(y))