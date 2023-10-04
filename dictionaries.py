thisdict={"brand":"ford",
                  "model":"ecosport",
                  "type":"suv",
          "year":2014,"year":2015}
# thisdict=dict(brand="ford",model="ecosport",type="suv",year=2014)
# print(thisdict)
# print(type(thisdict))
# print(thisdict['type'])
# (thisdict['type'])="sedan"#changing the data of an existing dictionary
# print(thisdict)
# (thisdict['seater'])="five","two"#adding more fields or items in an existing dictionary and #giving 2 values for a key
# print(thisdict)
#
# #deletion operation
# del thisdict['type']
# print(thisdict)
# print(thisdict.popitem())
# print(thisdict)
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
# print(thisdict)
for i in thisdict:
    print(i)
    print(thisdict[i])

#copyin the dictionaries
thisdict1=thisdict.copy()
print(thisdict1)