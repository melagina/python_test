'''
Created on 31 мая 2019 г.

@author: m.elagina
'''
bri = set(['brazil', 'russia', 'india'])
if 'india' in bri:
    print(' india in bri')
else:
    print(' india not in bri')
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
print(bri & bric)    