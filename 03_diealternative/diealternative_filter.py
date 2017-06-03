import json

with open ('diealternative.json') as infile:
    data = json.load(infile)
    

children = data["data"]["children"]

print len(children)
print children[0]["data"]["title"]
print "after = ", data["data"]["after"]


filteredlist = []

for elem in children:
	d = elem["data"]
	b = {}
	b["title"] = d["title"]
	b["num_comments"] = d["num_comments"]
	b["ups"] = d["ups"]
	b["downs"] = d["downs"]
	print d["title"], d["num_comments"], d["ups"], d["downs"], d["id"]
	filteredlist.append(b)

with open('diealternative2_scraped.json', 'w') as outfile:
 	json.dump(filteredlist, outfile)

