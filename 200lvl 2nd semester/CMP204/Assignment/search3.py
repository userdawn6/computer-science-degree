fname = input('Enter the filename: ') 
fhand = open(fname) 
count= 0 
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print ('There were', count, 'subject lines in', fname)