import csv

# READ CSV FILE
with open('file.csv') as f:
    csvfile = csv.reader(f)
    for row in csvfile:
        name, email, address = row
        print(f"Name: {name}\nEmail: {email}\nAddress: {address}")

# WRITE CSV FILE
lst = [['name1', 'email1', 'address1'], ['name2', 'email2', 'address2']]
with open('file.csv') as f:
    writer = csv.writer(f)
    writer.writerows(lst)  # write each inner list as a row
    # use writerow method to write a single row

# Reading and Writing CSV Files with Dictionaries
# READ
with open('file.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(
            f"Name: {row['name']}\nEmail: {row['email']}\nAddress: {row['address']}")

# WRITE
users = [{'name': 'name1', 'email': 'email1', 'address': 'address1'},
         {'name': 'name2', 'email': 'email2', 'address': 'address2'},
         {'name': 'name3', 'email': 'email3', 'address': 'address3'}]
keys = ["name", "email", "address"]
with open('file.csv') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# Other
with open('file.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

print(mpg[:3])
print(len(mpg))
print(mpg[0].keys())

print(sum(float(d['cty']) for d in mpg) / len(mpg))
print(sum(float(d['hwy']) for d in mpg) / len(mpg))

cylinders = set(d['cyl'] for d in mpg)
print(cylinders)


CtyMpgByCyl = []

for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['cyl'] == c:  # if the cylinder level type matches,
            summpg += float(d['cty'])  # add the cty mpg
            cyltypecount += 1  # increment the count
    # append the tuple ('cylinder', 'avg mpg')
    CtyMpgByCyl.append((c, summpg / cyltypecount))

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

vehicleclass = set(d['class'] for d in mpg)  # what are the class types
print(vehicleclass)


HwyMpgByClass = []

for t in vehicleclass:  # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['class'] == t:  # if the cylinder amount type matches,
            summpg += float(d['hwy'])  # add the hwy mpg
            vclasscount += 1  # increment the count
    # append the tuple ('class', 'avg mpg')
    HwyMpgByClass.append((t, summpg / vclasscount))

HwyMpgByClass.sort(key=lambda x: x[1])
print(HwyMpgByClass)
