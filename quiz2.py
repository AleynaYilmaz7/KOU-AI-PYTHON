text_file = open(r"odev.txt","r")
words = [*text_file.readlines()]


words_1= [*["".join(list(filter(str.isalnum, line))) for line in words]]
words_2= [*[" ".join(list(filter(lambda x: not x.isdigit(),line))) for line in words_1]]

words_3 = []

for i in words_2:
    j = i.replace(" ","")
    words_3.append(j)

#print(words_3)

text_file= open(r"odev.txt","w")

for elements in words_3:
    text_file.write(elements+ "\n")
text_file.close()
