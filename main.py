first = float(input("Enter the first number: [m] "))
second = float(input("Enter the second number: [m] "))
destination = float(input("Enter the destination between two points: [mm] "))
if second > first:
    second, first = first, second
distinction = int((first - second)*100)/100
print("%s m = %s mm" % (distinction, destination))
supplement = (int((int(first) - second)*100))/100
point = (int((destination * supplement) / distinction*1000))/1000
print("%s m = %s mm" % (supplement, point))
