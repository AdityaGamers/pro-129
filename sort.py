import csv 
data=[]
with open("archive.csv") as a:
    reader=csv.reader(a)
    for i in  reader:
        data.append(i)
headers=data[0]
planetdata=data[1:]
for i in planetdata:
    i[0]=i[0].lower()
planetdata.sort(key=lambda planetdata:planetdata[0])
with open("archive1.csv","a+") as r:
    writer=csv.writer(r)
    writer.writerow(headers)
    writer.writerows(planetdata)
with open("archive1.csv") as input,open("archivesorted.csv","w",newline="") as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(x.strip() for x in row):
            writer.writerow(row)


