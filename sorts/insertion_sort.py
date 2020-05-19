data = [16, 19, 11, 15, 10, 12, 14]

for item in data:
    sorted_val = data.index(item)
    #item is not the first element
    while sorted_val>0:
        if data[sorted_val-1] > data[sorted_val]:
            #swap
            data[sorted_val-1],data[sorted_val] = data[sorted_val],data[sorted_val-1]
        else:
            break
        sorted_val = sorted_val-1
print (data)
    