import itertools as it

with open('infile.txt','r') as f, open('outfile.txt','w') as outFile:
    grouped = it.groupby(f, lambda row: row.split('*')[0])
    for item in grouped:
        if item[0] == '01':
            row = grouped.next()
            if row[0] == '02':
                for row2 in row[1]:
                    print list(item[1])
                    continue
                    outFile.write(row2+list(item[1])[0])