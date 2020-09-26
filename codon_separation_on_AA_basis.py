header=''
str=''
A=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
K=[]
L=[]
M=[]
N=[]
P=[]
Q=[]
R=[]
S=[]
T=[]
V=[]
W=[]
Y=[]
X=[]
with open("test.txt","r") as file1:
    read=file1.read()
    data=read.split("\n")
    for each in data:
        if(">" in each):
            header=each
        else:
            for i in range(0,len(each),3):
                str=each[i:i+3:]
                if(str=='GCT'):
                    A.append(str)
                    str=''
                elif(str=='GCC'):
                    A.append(str)
                    str=''
                elif(str=='GCA'):
                    A.append(str)
                    str=''
                elif(str=='GCG'):
                    A.append(str)
                    str=''
                elif(str=='CGT'):
                    R.append(str)
                    str=''
                elif(str=='CGC'):
                    R.append(str)
                    str=''
                elif(str=='CGA'):
                    R.append(str)
                    str=''
                elif(str=='CGG'):
                    R.append(str)
                    str=''
                elif(str=='AGA'):
                    R.append(str)
                    str=''
                elif(str=='AGG'):
                    R.append(str)
                    str=''
                elif(str=='AAT'):
                    N.append(str)
                    str=''
                elif(str=='AAC'):
                    N.append(str)
                    str=''
                elif(str=='GAT'):
                    D.append(str)
                    str=''
                elif(str=='GAC'):
                    D.append(str)
                    str=''
                elif(str=='TGT'):
                    C.append(str)
                    str=''
                elif(str=='TGC'):
                    C.append(str)
                    str=''
                elif(str=='CAA'):
                    Q.append(str)
                    str=''
                elif(str=='CAG'):
                    Q.append(str)
                    str=''
                elif(str=='GAG'):
                    E.append(str)
                    str=''
                elif(str=='GAA'):
                    E.append(str)
                    str=''
                elif(str=='GGA'):
                    G.append(str)
                    str=''
                elif(str=='GGT'):
                    G.append(str)
                    str=''
                elif(str=='GGG'):
                    G.append(str)
                    str=''
                elif(str=='GGC'):
                    G.append(str)
                    str=''
                elif(str=='CAT'):
                    H.append(str)
                    str=''
                elif(str=='CAC'):
                    H.append(str)
                    str=''
                elif(str=='ATT'):
                    I.append(str)
                    str=''
                elif(str=='ATC'):
                    I.append(str)
                    str=''
                elif(str=='ATA'):
                    I.append(str)
                    str=''
                elif(str=='ATG'):
                    M.append(str)
                    str=''
                elif(str=='TTA'):
                    L.append(str)
                    str=''
                elif(str=='TTG'):
                    L.append(str)
                    str=''
                elif(str=='CTT'):
                    L.append(str)
                    str=''
                elif(str=='CTC'):
                    L.append(str)
                    str=''
                elif(str=='CTA'):
                    L.append(str)
                    str=''
                elif(str=='CTG'):
                    L.append(str)
                    str=''
                elif(str=='AAA'):
                    K.append(str)
                    str=''
                elif(str=='AAG'):
                    K.append(str)
                    str=''
                elif(str=='TTT'):
                    F.append(str)
                    str=''
                elif(str=='TTC'):
                    F.append(str)
                    str=''
                elif(str=='CCT'):
                    P.append(str)
                    str=''
                elif(str=='CCC'):
                    P.append(str)
                    str=''
                elif(str=='CCA'):
                    P.append(str)
                    str=''
                elif(str=='CCG'):
                    P.append(str)
                    str=''
                elif(str=='TCT'):
                    S.append(str)
                    str=''
                elif(str=='TCC'):
                    S.append(str)
                    str=''
                elif(str=='TCA'):
                    S.append(str)
                    str=''
                elif(str=='TCG'):
                    S.append(str)
                    str=''
                elif(str=='AGT'):
                    S.append(str)
                    str=''
                elif(str=='AGC'):
                    S.append(str)
                    str=''
                elif(str=='ACT'):
                    T.append(str)
                    str=''
                elif(str=='ACC'):
                    T.append(str)
                    str=''
                elif(str=='ACA'):
                    T.append(str)
                    str=''
                elif(str=='ACG'):
                    T.append(str)
                    str=''
                elif(str=='TGG'):
                    W.append(str)
                    str=''
                elif(str=='TAT'):
                    Y.append(str)
                    str=''
                elif(str=='TAC'):
                    Y.append(str)
                    str=''
                elif(str=='GTT'):
                    V.append(str)
                    str=''
                elif(str=='GTC'):
                    V.append(str)
                    str=''
                elif(str=='GTA'):
                    V.append(str)
                    str=''
                elif(str=='GTG'):
                    V.append(str)
                    str=''
                elif(str=='TAA'):
                    X.append(str)
                    str=''
                elif(str=='TAG'):
                    X.append(str)
                    str=''
                elif(str=='TGA'):
                    str=''
                    X.append(str)
                    str=''
            with open("codoncount.txt","a") as file2:
                file2.write(header+"\n")
                file2.write("A")
                for listitem in A:
                    file2.write(',%s' % listitem)
                    A=[]
                file2.write("\n")
                file2.write("C")
                for listitem in C:
                    file2.write(',%s' % listitem)
                    C=[]
                file2.write("\n")
                file2.write("D")
                for listitem in D:
                    file2.write(',%s' % listitem)
                    D=[]
                file2.write("\n")
                file2.write("E")
                for listitem in E:
                    file2.write(',%s' % listitem)
                    E=[]
                file2.write("\n")
                file2.write("F")
                for listitem in F:
                    file2.write(',%s' % listitem)
                    F=[]
                file2.write("\n")
                file2.write("G")
                for listitem in G:
                    file2.write(',%s' % listitem)
                    G=[]
                file2.write("\n")
                file2.write("H")
                for listitem in H:
                    file2.write(',%s' % listitem)
                    H=[]
                file2.write("\n")
                file2.write("I")
                for listitem in I:
                    file2.write(',%s' % listitem)
                    I=[]
                file2.write("\n")
                file2.write("K")
                for listitem in K:
                    file2.write(',%s' % listitem)
                    K=[]
                file2.write("\n")
                file2.write("L")
                for listitem in L:
                    file2.write(',%s' % listitem)
                    L=[]
                file2.write("\n")
                file2.write("M")
                for listitem in M:
                    file2.write(',%s' % listitem)
                    M=[]
                file2.write("\n")
                file2.write("N")
                for listitem in N:
                    file2.write(',%s' % listitem)
                    N=[]
                file2.write("\n")
                file2.write("P")
                for listitem in P:
                    file2.write(',%s' % listitem)
                    P=[]
                file2.write("\n")
                file2.write("Q")
                for listitem in Q:
                    file2.write(',%s' % listitem)
                    Q=[]
                file2.write("\n")
                file2.write("R")
                for listitem in R:
                    file2.write(',%s' % listitem)
                    R=[]
                file2.write("\n")
                file2.write("S")
                for listitem in S:
                    file2.write(',%s' % listitem)
                    S=[]
                file2.write("\n")
                file2.write("T")
                for listitem in T:
                    file2.write(',%s' % listitem)
                    T=[]
                file2.write("\n")
                file2.write("V")
                for listitem in V:
                    file2.write(',%s' % listitem)
                    V=[]
                file2.write("\n")
                file2.write("W")
                for listitem in W:
                    file2.write(',%s' % listitem)
                    W=[]
                file2.write("\n")
                file2.write("Y")
                for listitem in Y:
                    file2.write(',%s' % listitem)
                    Y=[]
                file2.write("\n")
                file2.write("X")
                for listitem in X:
                    file2.write(',%s' % listitem)
                    X=[]
                file2.write("\n")