'''
Created on 20 июн. 2019 г.

@author: m.elagina
'''
import pickle


shoplistfile = 'list.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # load the object from the file
print(storedlist)