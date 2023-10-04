# set1={10,45,13,True,90,33}
# print(set1)
# print(type(set1))
# set1.add(10.1)
# set1.add((11,12,13))
# print(set1)
# # set1.clear()
# set1.discard(12)
# set1.pop()
# print(set1)
#
# #operations on set
#
# #union
set2={'ram','sam','ken'}
set3={'kam','john','leo','ram','sam','ken'}
set4={'a','sam','c'}
# print(set2.union(set3))
# print(set2|set3)
# #union on multiple sets
# print(set2.union(set3,set4))
# print(set2|set3|set4)
# #passing tuple
# print(set2.union(('d','c')))
# #updation
# set2.update(set3)
# print(set2)
# set2.update(['jai','abi'])
# print(set2)

#intersection
# print(set2.intersection(set3))
# print(set2 &set3)
# print(set2.intersection(['ram','t','y'])) #passing list
# set3.intersection_update(set2)
# print(set3)

#Difference
# print(set2.difference(set3))
# print(set2-set3)
# print(set2.difference(('f','e')))
# print(set2.difference(set3,set4))
# set2.difference_update(set3)
# print(set2)

#symmetric_difference
# print(set2.symmetric_difference(set3))#exor operation
# print(set2^set3^set4)
# set2.symmetric_difference_update(set3)
# print(set2)
# set2.symmetric_difference_update(('y','o','ram'))
# print(set2)

#disjoint,subset,superset
print(set2.isdisjoint(set3))
print(set2.issubset(set3))
print(set2>=set3)#superset
print(set2<=set3)#subset
print(set2.issuperset(set3))
print(set2.isdisjoint(['g','k','l']))
print(set2.issubset(['kam','john','leo','ram','sam','ken']))
