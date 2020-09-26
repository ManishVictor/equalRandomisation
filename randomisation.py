import random
new_cod=''
split_readcod=[]
l=k=0
header=''
iter_cod=[]
iter_pep=[]
num=0
# file1=open("coronapep.txt","a+")
# file1.write("\n>DUMMY_FASTA_DUMMY")
# file1.close()
with open("codoncount.txt","r") as file1:
    read_cod=file1.readlines()
with open("pep.txt","r") as file2:
    read_pep=file2.readlines()
for each in read_pep:
    if(">" in each):
        iter_pep.append(num)
        num+=1
    else:
        num+=1
num=0
for each in read_cod:
    if(">" in each):
        iter_cod.append(num)
        num+=1
    else:
        num+=1
#print(iter_cod)
num=0
for i in iter_cod:
    for j in iter_pep:
        if(read_cod[i]==read_pep[j]):
            header=read_cod[i]
            k=i+1
            l=j+1
            a=0
            print(k,l)
            new_cod=''
            num=num+1
            while(a<=len(read_pep[l]) and k<iter_cod[num]):
                split_readcod=read_cod[k].rstrip("\n").split(",")
                #print(split_readcod)
                #print(k)
                #print(a)
                aa=read_pep[l][a]
                if(read_pep[l][a]!=split_readcod[0]):
                    k=k+1
                elif(read_pep[l][a]==split_readcod[0] or a<=len(read_pep[l][a])):
                    index=random.randint(1,len(split_readcod)-1)
                    new_cod+=split_readcod[index]
                    del split_readcod[index]
                    a=a+1
                    k=i+1
            with open("random.txt","a")as file4:
                file4.write(header)
                file4.write(new_cod+"\n")
                new_cod=''