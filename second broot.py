a=0
your_list = 'abcdefghijklmnopqrstuvwxyz'
complete_list = []
for current in range(8):
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
        #f=open('list', 'w')
        #f.write('string st['+str(len(a))+']=["'+'", "'.join(a)+'"];')
        #f.close()
        print('string st['+str(len(a))+']=["'+'", "'.join(a)+'"];')
    complete_list = complete_list+a
