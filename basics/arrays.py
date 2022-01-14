# arrays are ver bad at inserting and deleting
# arrays is like a train with a bunch of cars in order.
# has an index.

new_list = [1,2,3]

result = new_list[0]
# 1

if 1 in new_list: print(True)

for n in new_list:
    if n==1:
        print(True)
        break

new_list.append(4)

print(len(new_list))

new_list.extend([5,6,7])
new_list.insert(0,0)
print(new_list)