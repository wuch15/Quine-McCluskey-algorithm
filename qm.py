import random
from time import clock
print('武楚涵 2015011079')
print('输入查询次数:')
instr_num=input()
instr_num=int(instr_num)
for ins_num in range(instr_num):
    v_num=0
    #aaa=input()
    #bbb=input()
    print('输入最小项:')
    smin=input()
    smin = smin.split(" ")
    table2=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    mlen=len(smin[0])
    if (mlen> 0):
        for i in range(len(smin)):
            smin[i]=int(smin[i])
    else:
        print("X=0")
    #print (smin)
    print('输入无关项:')
    sd=input()
    sd= sd.split(" ")
    dlen=len(sd[0])
    if(dlen>0):
        for i in range(len(sd)):
            sd[i]=int(sd[i])
    if(mlen==0):
        print(0)
        continue
    if (dlen == 0):
        sd=[]
    if(smin[0]==0 and len(smin)==1 and len(sd)==0):
        print(1)
        continue

    bis=[]
    bid=[]
    if (len(smin) == 0):
        print(0)
        continue

    ki=smin+sd
    ti=max(ki)

    #进行输入字符的切分预处理

    for i in range(11):
        if table2[i+1]>=ti+1 and ti+1>table2[i]:
            v_num = i+1


    if(ti+1 in table2)and len(ki)==ti+1:
        print(1)
        continue
    if (len(sd) > 0):
        for i in sd:
            x = bin(i).replace('0b', '')
            x = "0" * (int(v_num) - len(x)) + x
            bid.append([x,i])
    if (len(smin)> 0):
        for i in smin:
            x = bin(i).replace('0b', '')
            x = "0" * (int(v_num) - len(x)) + x
            bis.append([x,i])
    def cmp(x,y):
        num=0
        index = -1
        for i in range(len(x)):
            if(x[i]!=y[i]):
                index = i
                num+=1
        return index,num
    tf=dict({})
    #输入的最小项和无关项变成01字符串
    for i in range(v_num+1):
        tf[i]=[]
    biall=bis+bid
    for x in biall:
        tf[x[0].count('1')].append([x[0],False,[x[1]]])#统计1的个数来分组
    holder = dict()
    noho = []
    for i in range(v_num):
        holder[i] = []
        for x in range(len(tf[i])):
            for y in range(len(tf[i + 1])):
                index, num = cmp(tf[i][x][0], tf[i + 1][y][0])
                if (num == 1):
                    tp = tf[i][x][0]
                    tf[i][x][1] = True
                    tf[i + 1][y][1] = True
                    tp = list(tp)
                    tp[index] = '2'#用2来代替'-'
                    st = ""
                    for u in tp:
                        st = st + u
                    holder[i].append([st, False, list(set(tf[i][x][2] + tf[i + 1][y][2]))])
    for i in range(v_num + 1):
        for x in range(len(tf[i])):
            if tf[i][x][1] == False:
                noho.append(tf[i][x])
    dic_rem = []
    for x in holder.keys():
        if len(holder[x]) == 0:
            dic_rem.append(x)
    for x in dic_rem:
        holder.pop(x)
    while (len(holder) > 0):#重复进行合并
        pholder = dict()
        for x in holder.keys():
            pholder[x] = []
        tp = list(holder.keys())
        for ind in range(len(tp) - 1):
            for x in range(len(holder[tp[ind]])):
                for y in range(len(holder[tp[ind + 1]])):
                    index, num = cmp(holder[tp[ind]][x][0], holder[tp[ind + 1]][y][0])
                    if (num == 1):
                        holder[tp[ind]][x][1] = True
                        holder[tp[ind + 1]][y][1] = True
                        tpt = list(holder[tp[ind]][x][0])
                        tpt[index] = '2'
                        st = ""
                        for u in tpt:
                            st = st + u
                        pholder[tp[ind]].append(
                            (st, False, tuple(set(holder[tp[ind]][x][2] + holder[tp[ind + 1]][y][2]))))
        for k in pholder.keys():
            pholder[k] = list(set(pholder[k]))

        for k in pholder.keys():
            for m in range(len(pholder[k])):
                pholder[k][m] = list(pholder[k][m])
                pholder[k][m][2] = list(pholder[k][m][2])

        for ind in holder.keys():
            for i in range(len(holder[ind])):
                if holder[ind][i][1] == False:
                    noho.append(holder[ind][i])
        dic_rem2 = []
        for x in pholder.keys():
            if len(pholder[x]) == 0:
                dic_rem2.append(x)
        for x in dic_rem2:
            pholder.pop(x)
        holder = pholder
    remover=[]
    #进行一些去重工作
    for x in range(len(noho)):
        for y in range(x+1,len(noho)):
            if x!=y and noho[x][0]==noho[y][0]:
                remover.append(noho[x])
    for x in remover:
        if x in noho:
            noho.remove(x)
    target=set(smin)

    for x in sd:
        for y in range(len(noho)):
            if x in noho[y][2]:
                noho[y][2].remove(x)


    setters = []
    for x in noho:
        setters.append(set(x[2]))

    cover=set([])
    cover0=setters
    s=target
    resultlist=[]
    replay=dict({})
    refer=dict({})
    prime=dict({})

    tempset0=[]
    #找出本质本原蕴含项
    for x in s:
        num = 0
        temp = None
        for se in cover0:
            if x in se:
                num += 1
                temp = se
        if num == 1:
            tempset0.append(temp)


    noho_dup = set()
    for i in range(len(cover0)):
        for j in range(i + 1, len(cover0)):
            if set(cover0[i]) == set(cover0[j]):
                noho_dup.add(j)
    tp_cover0=cover0
    for x in noho_dup:
        if x in cover0:
            cover0.remove(tp_cover0[x])
    noho_remove = set()
    tp2_cover0 = cover0
    for i in range(len(cover0)):
        for j in range(len(cover0)):
            if i != j and len(set(cover0[i]) - set(cover0[j])) == 0:
                noho_remove.add(i)
    for x in noho_remove:
        if x in cover0:
            cover0.remove(tp2_cover0[x])

    ii=1
    for se in cover0:
        replay[tuple(se)]=ii
        ii+=1

    for temp in tempset0:
        s = s- set(temp)
        target = target - set(temp)
        if temp in cover0:
            for a in range(len(cover0)):
                cover0[a]=cover0[a] - temp

        for a in cover0[:]:
            if(len(a)==0):
                cover0.remove(a)

        bbb=[]
        bsd=False
        for x in replay.keys():
            if temp==set(x):
                bbb = x
                bsd = True
        if bsd:
            prime[bbb]=replay[bbb]
            replay.pop(bbb)
    kkk={v:k for k,v in replay.items()}
    while (len(s)>0):#进入最小集合覆盖的循环，使用多种策略的启发式算法
        bs1 = False
        bs2 = False
        bs3 = False
        bs4 = False
        for se in cover0:#第一步检查是否有集合已经包含剩余的项
            if(len(s-se)==0):
                cover = set(list(cover) + list(se))
                resultlist.append(se)
                bs1 = True
                break
        if(bs1):
            break
        tempset=[]
        for x in s:#第二步检查是否有只被包含一次的项
            num=0
            temp=None
            for se in cover0:
                if x in se:
                    num+=1
                    temp=se
            if num==1:
                tempset.append(temp)
                bs2=True
        for temp in tempset:
            cover = set(list(cover) + list(temp))
            resultlist.append(temp)
            if temp in cover0:
                cover0.remove(temp)
            tst=[]
            teb = False
            for x in replay.keys():
                if set(x)==temp:
                    tst=x
                    teb =True
            if teb:
                refer[tuple(tst)]=replay[tuple(tst)]
            if tuple(tst) in replay.keys():
                replay.pop(tuple(tst))
            s=s-temp
            break
        if (bs1 == False and bs2 == False):#第三步检查是否有被包含的集合
            removelist=[]
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

        if (bs1 == False and bs2 == False and bs3 == False):#第四步检查是否有元素的包含项属于其他元素的被包含项
            snlist={}
            for x in s:
                temps=[]
                for se in cover0:
                    if x in se:
                        temps.append(se)
                snlist[x]=temps
            removelist2=[]
            for val in snlist.keys():
                for val2 in snlist.keys():
                    if val!=val2 and len([ i for i in snlist[val] if i not in snlist[val2]])==0:
                        removelist2.append(val2)
                        cover.add(val2)
                        bs4=True
            removelist2=set (removelist2)
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

        if(bs1==False and bs2==False and bs3==False and bs4==False ):#最后策略，选取能覆盖最多的项
            maxnum=0
            maxtemp=None
            for se in cover0:
                if(len(se)>maxnum):
                    maxnum=len(se)
                    maxtemp=se
            cover = set(list(cover) + list(maxtemp))
            resultlist.append(maxtemp)
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
                refer[tst]=replay[tst]
            for zzz in vr:
                vvv.pop(zzz)
            replay = {v: k for k, v in vvv.items()}

        target=s
    for k in refer.keys():
        replay[k]=refer[k]
    rp = []
    for s in resultlist:
        tst = []
        tgb = False
        max_sum=0
        for x in replay.keys():
            if len(s-set(x))==0:
                if len(x)>max_sum:
                    tst = x
                    tgb = True
        if tgb:
            rp.append(list(kkk[replay[tst]]))#进行结果的处理，转换为输出
    def king(x):
        st=""
        for i in x:
            if i == '1':
                st = st + '2'
            if i == '0':
                st = st + '1'
            if i == '2':
                st = st + '0'
        return int(st)
    def king(x):
        st=""
        for i in x:
            if i == '1':
                st = st + '2'
            if i == '0':
                st = st + '1'
            if i == '2':
                st = st + '0'
        return int(st)
    add=[]
    for x in rp:
        for y in noho:
            if set(x)==set(y[2]):
                add.append(y[0])
                break
    add2=[]
    for x in prime.keys():
        for y in noho:
            if set(x) == set(y[2]):
                add2.append(y[0])
    dv1=dict()
    dv2=dict()
    for x in add:
        dv1[king(x)]=x
    for x in add2:
        dv2[king(x)]=x
    dvv1= sorted(dv1.items(), key=lambda d:d[0])
    dvv2 = sorted(dv2.items(), key=lambda d:d[0])
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
    kt=[]
    answer=""
    for k in range(len(dvv1)) :
        kt.append(bi2word(dvv1[len(dvv1)-1-k][1]))

    for k in range(len(dvv2)) :
        at.append(bi2word(dvv2[len(dvv2)-1-k][1]))
    if len(at)==0:
        if len(kt)==0:
            print(0)
        else:
            answer ='+'.join(kt)
    else:
        if len(kt) == 0:
            answer ='+'.join(at)
        else:
            answer = '+'.join(at)+'+'+'+'.join(kt)
    print(answer)
