file=open('example.txt','w')
print('File Name:',file.name)
print('File Open Mode:',file.mode)
print('Readable:',file.readable())
print('Writable:',file.writable())
def get_status(f):
    if(f.closed!=False):
        return 'Closed'
    else:
        return 'Open'

print('File status:',get_status(file))
file.close()
print('File status:',get_status(file))

