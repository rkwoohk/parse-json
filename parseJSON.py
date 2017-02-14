import json
import sys

rawdata = "{}"
csvdata = []

if not sys.stdin.isatty():
    rawdata = sys.stdin.read()

data = json.loads(rawdata)["hits"]["hits"]

# Print specific fields
'''
for row in data:
    csvdata = [row["_source"]["@timestamp"], row["_source"]["host"], row["_source"]["message"]]
    csvdata = '|'.join(map(str,csvdata))
    print csvdata.replace('\n','')
'''

# Sort and print all fields
sortedkey = sorted(data[0]["_source"])
for row in data:
    for key in sortedkey:
        csvdata.append(row["_source"][key])
    csvdata = '|'.join(map(str, csvdata))
    print csvdata.replace('\n','')
    csvdata = []
