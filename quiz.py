
##### soru 1 ######
num = int(input("Enter a number: "))
if (num % 2) == 0:
     print("{0} is Even number". format(num))
else:
     print("{0} is Odd number". format(num))
    
    
    
##### soru 2 ######    
list = []
for i in range(0,5):
    value = int(input("Enter five number: "))
    list.insert(i,value)

for x in range(list[0], list[4]+1):
    if x> 1:
        for y in range(2, x):
            if (x%y == 0):
                print("{} isn't a prime number".format(x))
                break

        else:
            print("{} is a prime number".format(x))
            
            
            
##### soru 3 ######           
def TemizVeri():
    first_string = "Ah5me4t"
    second_string = "M9eHm4eT"
    third_string = "Ha3K5a1n"

    string_list = [first_string, second_string, third_string]
    new_list = []
    for i in string_list:
        if i == first_string:
            new_first_string = ''.join(filter(lambda x: not x.isdigit(), first_string))
            new_list.append(new_first_string)
    for j in string_list:
        if j == second_string:
            new_second_string = ''.join(filter(lambda x: not x.isdigit(), second_string))
            new_list.append(new_second_string.lower().capitalize())
    for k in string_list:
        if k == third_string:
            new_third_string = ''.join(filter(lambda x: not x.isdigit(), third_string))
            new_list.append(new_third_string.lower().capitalize())

    string_list = new_list

    print("{} - {} - {}".format(string_list[0], string_list[1], string_list[2]))

TemizVeri()

