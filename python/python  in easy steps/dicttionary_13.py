dict = {'name':'Bob','ref':'Python','sys':'Win'}
print('Dictionary :',dict)
print('Reference :',dict['ref'])
print('keys :',dict.keys())
del dict['name']
dict['user']='Tom'

print('Dictionary :',dict)
print('Is there any A name key? :', 'name' in dict)
