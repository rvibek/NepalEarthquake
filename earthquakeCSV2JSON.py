import sys, csv, json

# if len(sys.argv) == 1:
#     print "1 argument for filename required"
#     sys.exit()

gdoc = csv.reader(open("earthquakenep.csv"))

# Get the 1st line, assuming it contains the column titles
fieldnames = gdoc.next() 

# Get the total number of columns
fieldnames_len = len(fieldnames)

data = [] # Empty list
i = 0

for row in gdoc:
    
    # Add an empty dict to the list
    data.append({})
    
    for j in range(0, len(row)):
        data[i][fieldnames[j]] = row[j]
    
    # What if the last few cells are empty ? There may not be commas
    for j in range(len(row), fieldnames_len):
        data[i][fieldnames[j]] = ""
    
    i = i + 1

myjson = open("earthquake.json", "w")
print json.dumps(data)
xjson = '{"earthquake" :'+str.replace(json.dumps(data)," ","")+'}'
myjson.write(xjson)
sys.exit()
