import os

insert_line = '00005,A,27/02/23,CS,Finish Coursework\n'

if os.path.isfile('moscow.bak'):
    os.remove('moscow.bak')
if os.path.isfile('moscow.csv'):
    os.rename('moscow.csv', 'moscow.bak')

target_file = open('moscow.csv', 'w')

with open('moscow.bak', 'w') as moscow_file:
    for x in moscow_file:
        line = x
        fields = line.split(',')
        if fields[0] == '00006':
            target_file.write(insert_line)
        target_file.write(line)
target_file.close()

