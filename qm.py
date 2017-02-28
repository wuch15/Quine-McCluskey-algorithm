print("输入位数:")
v_num=input()
print("输入最小项:")
v_num=int(v_num)
smin=input()
smin = smin.split(" ")


#v_num = 4
#smin =[4,8,10,11,12,15]
mlen=len(smin[0])
if (mlen> 0):
    for i in range(len(smin)):
        smin[i]=int(smin[i])
else:
    print("X=0")
print (smin)
print("输入无关项:")
sd=input()

#sd =[9,14]
bis=[]
bid=[]
sd= sd.split(" ")
dlen=len(sd[0])
if(dlen>0):
    for i in range(len(sd)):
        sd[i]=int(sd[i])
    for i in sd:
        x = bin(i).replace('0b', '')
        x = "0" * (int(v_num) - len(x)) + x
        bid.append([x,i])
if (mlen> 0):
    for i in smin:
        x = bin(i).replace('0b', '')
        x = "0" * (int(v_num) - len(x)) + x
        bis.append([x,i])
#print(bis,bid)
def cmp(x,y):
    num=0
    index = -1
    for i in range(len(x)):
        if(x[i]!=y[i]):
            index = i
            num+=1
    return index,num
tf=dict({})
for i in range(v_num+1):
    tf[i]=[]
biall=bis+bid
for x in biall:
    tf[x[0].count('1')].append([x[0],False,[x[1]]])
#print(tf)
holder = []
noho=[]
for i in range(v_num):
    for x in range(len(tf[i])):
        for y in range(len(tf[i+1])):
            index,num=cmp(tf[i][x][0],tf[i+1][y][0])
            if(num==1):
                tp=tf[i][x][0]
                #print(tf[i][x][0],tf[i+1][y][0],index)
                tf[i][x][1]=True
                tf[i+1][y][1] = True
                tp = list(tp)
                tp[index]='2'
                st=""
                for u in tp:
                    st=st+u
                holder.append([st,False,list(set(tf[i][x][2]+tf[i+1][y][2]))])

#print(tf)
for i in range(v_num):
    for x in range(len(tf[i])):
        if tf[i][x][1]==False:
            noho.append(tf[i][x])
#print(noho)
#print(holder)

while(len(holder)>0):
    pholder=[]
    for x in range(len(holder)):
        for y in range(len(holder)):
            if(x!=y):
                index, num = cmp(holder[x][0], holder[y][0])
                if(num==1):
                    holder[x][1]=True
                    holder[y][1] = True
                    tp = list(holder[x][0])
                    tp[index]='2'
                    st=""
                    for u in tp:
                        st = st + u
                    pholder.append((st, False,tuple(set(holder[x][2]+holder[y][2]))))
    pholder= list(set(pholder))

    pht=[]
    for m in pholder:
        m=list(m)
        m[2]=list(m[2])
        pht.append(m)
    pholder=pht

    for i in range(len(holder)):
        if holder[i][1]==False:
            noho.append(holder[i])
    holder = pholder
    #print("h",holder)
    #print("no",noho)
remover=[]
for x in range(len(noho)):
    for y in range(x+1,len(noho)):
        if x!=y and noho[x][0]==noho[y][0]:
            remover.append(noho[x])
#print("remover", remover)
#print("noBEFORE",noho)
for x in remover:
    if x in noho:
        noho.remove(x)

#print("no",noho)
for x in sd:
    for y in range(len(noho)):
        if x in noho[y][2]:
            noho[y][2].remove(x)

#print("no",noho)
target=set(smin)
setters=[]
for x in noho:
    setters.append(set(x[2]))
#print(target)

tag=[]
for x in setters:
    temptag=[]
    for y in target:
        if y in x:
            temptag.append(1)
        else:
            temptag.append(0)
    tag.append(temptag)
#print(tag)
cover=set([])
cover0=setters
s=target
resultlist=[]
replay=dict({})
refer=dict({})
#print('***************')
ii=1
for se in cover0:
    replay[tuple(se)]=ii
    ii+=1
kkk={v:k for k,v in replay.items()}
while (len(cover)<len(target)):
    #time.sleep(0.1)
    bs1 = False
    bs2 = False
    bs3 = False
    bs4 = False
    #print(cover)
    #print(cover0)
    for se in cover0:
        if(len(s-se)==0):
            cover = set(list(cover) + list(se))
            resultlist.append(se)
            bs1 = True
            break
    #print("step1")
    #print(cover)
    #print(cover0)
    #print(s)
    #print(resultlist)
    if(bs1):
        break
    tempset=[]
    for x in s:
        num=0
        temp=None
        for se in cover0:
            if x in se:
                num+=1
                temp=se
        if num==1:
            tempset.append(temp)
            #cover=set(list(cover)+[x])
            bs2=True
    for temp in tempset:
        cover = set(list(cover) + list(temp))
        #replay = set(list(replay) + list(temp))
        resultlist.append(temp)
        if temp in cover0:
            cover0.remove(temp)
        #print("replay!!!!!",replay)
        tst=[]
        for x in replay.keys():
            if set(x)==temp:
                tst=x
        refer[tuple(tst)]=replay[tuple(tst)]
        if tuple(tst) in replay.keys():
            replay.pop(tuple(tst))
        s=s-temp
        break
    ##print("step2")
    ##print(cover)
    ##print(cover0)
    ##print(s)
    ##print(resultlist)
    if (bs1 == False and bs2 == False):
        removelist=[]
        #cover0=[{1,2,3},{1,3},{2},{1,2,4,3,6}]
        for si in cover0:
            for sj in cover0:
                if si!=sj and len(si-sj)==0:
                    removelist.append(si)
                    bs3=True
        for x in removelist:
            if x in cover0:
                cover0.remove(x)
            tcv=[]
            btcv=False
            for cv in replay.keys():
                if set(x) == set(cv):
                    tcv = cv
                    btcv = True
            if btcv :
                replay.pop(tcv)
        #print("step3")
        #print(cover)
        #print(cover0)
        #print(s)
        #print(resultlist)
    if (bs1 == False and bs2 == False and bs3 == False):
        snlist={}
        for x in s:
            temps=[]
            for se in cover0:
                if x in se:
                    temps.append(se)
            snlist[x]=temps
        #print(snlist)
        removelist2=[]
        for val in snlist.keys():
            for val2 in snlist.keys():
                #print(len([ i for i in snlist[val] if i not in snlist[val2]]))
                if val!=val2 and len([ i for i in snlist[val] if i not in snlist[val2]])==0:
                    removelist2.append(val2)
                    cover.add(val2)
                    bs4=True
        removelist2=set (removelist2)
        #print(removelist2)
        temp=[]
        for se in cover0:
            se = se-removelist2
            temp.append(se)

        sss = {v:k for k, v in replay.items()}
        for k in sss.keys():
            sss[k]=tuple(set(sss[k])-removelist2)
        replay = {v:k for k, v in sss.items()}
        cover0 = temp

        s=s-removelist2
        ##print("step4")
        ##print(cover)
        ##print(cover0)
        ##print(s)
        ##print(resultlist)
    if(bs1==False and bs2==False and bs3==False and bs4==False ):
        print('不满足要求')
        maxnum=0
        maxtemp=None
        #cover0=[{1,2,3},{1,3},{2},{1,2,4,3,8}]
        for se in cover0:
            if(len(se)>maxnum):
                maxnum=len(se)
                maxtemp=se
        cover = set(list(cover) + list(maxtemp))
        resultlist.append(maxtemp)
        #resultlist= list(set(resultlist))
        tp=[]
        if maxtemp in cover0:
            cover0.remove(maxtemp)
        for se in cover0:
            tp.append(se-maxtemp)
        cover0 = tp
        s = s-maxtemp
        vvv = {v: k for k, v in replay.items()}
        vr =[]
        for r in vvv.keys():
            vvv[r]=tuple(set(vvv[r])-maxtemp)
            if(len(vvv[r])==0):
                vr.append(r)
        tst = []
        btst2=False
        for x in replay.keys():
            if set(x) == maxtemp:
                tst = x
                btst2 =True
        if btst2:
            refer[tuple(maxtemp)]=replay[tuple(maxtemp)]
        for zzz in vr:
            vvv.pop(zzz)
        replay = {v: k for k, v in vvv.items()}
        #print("step5")
        #print(cover)
        #print(cover0)
        #print(s)
        #print(resultlist)

    #print(replay)
#print("refer",refer)
#print("replay",replay)
for k in refer.keys():
    replay[k]=refer[k]
#print("merged replay",replay)
rp = []
for s in resultlist:
    tst = []
    for x in replay.keys():
        if set(x) == s:
            tst = x
    rp.append(list(kkk[replay[tst]]))
    #print(list(kkk[replay[tuple(s)]]))
#print(rp)
add=[]
for x in rp:
    for y in noho:
        if set(x)==set(y[2]):
            add.append(y[0])
#print(add)
def bi2word(x):
    table='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    st=""
    j=0
    for i in x:
        if i=='1':
            st=st+table[j]
        if i == '0':
            st = st + table[j]+'\''
        j+=1
    return st
at=[]
for k in add :
    at.append(bi2word(k))
answer = 'X='+'+'.join(at)
print(answer)