import random

file = open('datos.tsv','w')
for i in range(0,random.randint(1000,10000)):
    file.write(str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\t' + str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\t' + str(random.uniform(0.1,random.randint(1,1000))) + '\t' + str(random.random()) + '\n')

file.close()
