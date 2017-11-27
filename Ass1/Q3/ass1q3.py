#!/usr/bin/python
## Written by Bianca Tong 26/08/2017 for COMP 4418 ass1 q3
import sys
import re
import copy
## function to classify the priority of opration
def priority(L):
    L_pri=copy.deepcopy(L)
    j=0
    xxx=0
    yyy=0
    for i in range(0,len(L)):
        j=0
        while (j<len(L[i])):
            if (L[i][j]=='('):
                xxx+=1
                L_pri[i][j]=0
                while(xxx>yyy):
                    j+=1
                    if (L[i][j]==')'):
                        yyy+=1
                    if (L[i][j]=='('):
                        xxx+=1
                    L_pri[i][j]=0
                L_pri[i][j]=0
            elif (L[i][j]=='iff' or L[i][j]=='imp'):
                L_pri[i][j]=3
            elif (L[i][j]=='and' or L[i][j]=='or'):
                L_pri[i][j]=2
            elif (L[i][j]=='neg'):
                L_pri[i][j]=1
            else:
                L_pri[i][j]=0
            j+=1
    return L_pri
## all the rules
def rule_6b(L_left,L_right,iff_x,iff_y):
    L_left_change1=[]
    L_left_change2=[]
    L_right_change=copy.deepcopy(L_right)
    for i in range(0,len(L_left)):
        L_ss=[]
        if (i!=iff_x):
            L_left_change1.append(L_left[i])
            L_left_change2.append(L_left[i])
        else:
            for k in range(0,iff_y):
                L_ss.append(L_left[i][k])
            L_left_change1.append(L_ss)
            if (L_right_change==[] or L_right_change==[[]]):
                L_right_change=copy.deepcopy([L_ss])
            else:
                L_right_change.append(L_ss)
            L_ss=[]
            for m in range(iff_y+1,len(L_left[i])):
                L_ss.append(L_left[i][m])
            L_left_change1.append(L_ss)
            if (L_right_change==[] or L_right_change==[[]]):
                L_right_change=copy.deepcopy([L_ss])
            else:
                L_right_change.append(L_ss)
    return L_left_change1,L_right,L_left_change2,L_right_change
def rule_6a(L_left,L_right,iff_x,iff_y):
    L_left_change1=copy.deepcopy(L_left)
    L_left_change2=copy.deepcopy(L_left)
    L_right_change1=[]
    L_right_change2=[]
    for i in range(0,len(L_right)):
        L_ss=[]
        if (i!=iff_x):
            L_right_change1.append(L_right[i])
            L_right_change2.append(L_right[i])
        else:
            for k in range(0,iff_y):
                L_ss.append(L_right[i][k])
            L_right_change1.append(L_ss)
            if (L_left_change2==[] or L_left_change2==[[]]):
                L_left_change2=copy.deepcopy([L_ss])
            else:
                L_left_change2.append(L_ss)
            L_ss=[]
            for m in range(iff_y+1,len(L_right[i])):
                L_ss.append(L_right[i][m])
            L_right_change2.append(L_ss)
            if (L_left_change1==[] or L_left_change1==[[]]):
                L_left_change1=copy.deepcopy([L_ss])
            else:
                L_left_change1.append(L_ss)
    return L_left_change1,L_right_change1,L_left_change2,L_right_change2
def rule_5b(L_left,L_right,imp_x,imp_y):
    L_left_change1=[]
    L_left_change2=[]
    L_right_change=copy.deepcopy(L_right)
    for i in range(0,len(L_left)):
        L_ss=[]
        if (i!=imp_x):
            L_left_change1.append(L_left[i])
            L_left_change2.append(L_left[i])
        else:
            for k in range(0,imp_y):
                L_ss.append(L_left[i][k])
            if (L_right_change==[] or L_right_change==[[]]):
                L_right_change=copy.deepcopy([L_ss])
            else:
                L_right_change.append(L_ss)
            L_ss=[]
            for m in range(imp_y+1,len(L_left[i])):
                L_ss.append(L_left[i][m])
            L_left_change1.append(L_ss)
    return L_left_change1,L_right,L_left_change2,L_right_change
def rule_5a(L_left,L_right,imp_x,imp_y):
    L_left_change=copy.deepcopy(L_left)
    L_right_change=[]
    for i in range(0,len(L_right)):
        L_ss=[]
        if (i!=imp_x):
            L_right_change.append(L_right[i])
        else:
            for k in range(0,imp_y):
                L_ss.append(L_right[i][k])
            if (L_left_change==[] or L_left_change==[[]]):
                L_left_change=copy.deepcopy([L_ss])
            else:
                L_left_change.append(L_ss)
            L_ss=[]
            for m in range(imp_y+1,len(L_right[i])):
                L_ss.append(L_right[i][m])
            L_right_change.append(L_ss)
    return L_left_change,L_right_change
def rule_4b(L_left,L_right,or_x,or_y):
    L_left_change1=[]
    L_left_change2=[]
    for i in range(0,len(L_left)):
        L_ss=[]
        if (i!=or_x):
            L_left_change1.append(L_left[i])
            L_left_change2.append(L_left[i])
        else:
            for k in range(0,or_y):
                L_ss.append(L_left[i][k])
            L_left_change1.append(L_ss)
            L_ss=[]
            for m in range(or_y+1,len(L_left[i])):
                L_ss.append(L_left[i][m])
            L_left_change2.append(L_ss)
    return L_left_change1,L_left_change2,L_right
def rule_4a(L_left,L_right,or_x,or_y):
    L_right_change=[]
    for i in range(0,len(L_right)):
        L_ss=[]
        if (i!=or_x):
            L_right_change.append(L_right[i])
        else:
            for k in range(0,or_y):
                L_ss.append(L_right[i][k])
            L_right_change.append(L_ss)
            L_ss=[]
            for m in range(or_y+1,len(L_right[i])):
                L_ss.append(L_right[i][m])
            L_right_change.append(L_ss)
    return L_left,L_right_change
def rule_3b(L_left,L_right,and_x,and_y):
    L_left_change=[]
    for i in range(0,len(L_left)):
        L_ss=[]
        if (i!=and_x):
            L_left_change.append(L_left[i])
        else:
            for k in range(0,and_y):
                L_ss.append(L_left[i][k])
            L_left_change.append(L_ss)
            L_ss=[]
            for m in range(and_y+1,len(L_left[i])):
                L_ss.append(L_left[i][m])
            L_left_change.append(L_ss)
    return L_left_change,L_right
def rule_3a(L_left,L_right,and_x,and_y):
    L_right_change1=[]
    L_right_change2=[]
    for i in range(0,len(L_right)):
        L_ss=[]
        if (i!=and_x):
            L_right_change1.append(L_right[i])
            L_right_change2.append(L_right[i])
        else:
            for k in range(0,and_y):
                L_ss.append(L_right[i][k])
            L_right_change1.append(L_ss)
            L_ss=[]
            for m in range(and_y+1,len(L_right[i])):
                L_ss.append(L_right[i][m])
            L_right_change2.append(L_ss)
    return L_left,L_right_change1,L_right_change2
def rule_2b(L_left,L_right,neg_x,neg_y):
    L_left_change=[]
    L_right_change=copy.deepcopy(L_right)
    for i in range(0,len(L_left)):
        L_ss=[]
        if (i==neg_x):
            for j in range(neg_y+1,len(L_left[i])):
                L_ss.append(L_left[i][j])
        else:
            L_left_change.append(L_left[i])
        if (L_ss!=[]):
            if (L_right_change==[] or L_right_change==[[]]):
                L_right_change=copy.deepcopy([L_ss])
            else:
                L_right_change.append(L_ss)
    return L_left_change,L_right_change
def rule_2a(L_left,L_right,neg_x,neg_y):
    L_left_change=copy.deepcopy(L_left)
    L_right_change=[]
    for i in range(0,len(L_right)):
        L_ss=[]
        if (i==neg_x):
            for j in range(neg_y+1,len(L_right[i])):
                L_ss.append(L_right[i][j])
        else:
            L_right_change.append(L_right[i])
        if (L_ss!=[]):
            if (L_left_change==[] or L_left_change==[[]]):
                L_left_change=copy.deepcopy([L_ss])
            else:
                L_left_change.append(L_ss)
    return L_left_change,L_right_change
def rule_1(L_left,L_right):
    for i in range(0,len(L_left)):
        for j in range(0,len(L_left[i])):
            if (len(L_left[i][j])==1):
                continue
            else:
                return False
    for i in range(0,len(L_right)):
        for j in range(0,len(L_right[i])):
            if (len(L_right[i][j])==1):
                continue
            else:
                return False
    for i in range(0,len(L_left)):
        if (L_left[i] in L_right):
            return True
    return False
## import a sequence
L_org=sys.argv[1]
L_orgg=L_org.split()
L_org_sp=[]
for i in L_orgg:
    if (i.isalpha()):
        L_org_sp.append(i)
    else:
        L_s=''
        for k in range(0,len(i)):
            if (i[k].isalpha()):
                L_s+=i[k]
                if (k==len(i)-1):
                    L_org_sp.append(L_s)
                else:
                    continue
            else:
                if (L_s==''):
                    L_org_sp.append(i[k])
                    continue
                else:
                    L_org_sp.append(L_s)
                    L_org_sp.append(i[k])
                    L_s=''

## to seperate the original list into left and right lists
n=0
for i in range(0,len(L_org_sp)):
    if (L_org_sp[i]=='seq'):
        n=i
        break
L_left=[]
L_s=[]
for j in range(1,n-1):
    if (L_org_sp[j]==','):
        L_left.append(L_s)
        L_s=[]
    else:
        L_s.append(L_org_sp[j])
L_left.append(L_s)
L_right=[]
L_s=[]
for k in range(n+2,len(L_org_sp)-1):
    if (L_org_sp[k]==','):
        L_right.append(L_s)
        L_s=[]
    else:
        L_s.append(L_org_sp[k])
L_right.append(L_s)
All_lists=[]
All_lists.append([L_left,L_right])
n=0
results=[]
rules=[]
num=0
while(n < len(All_lists)):
    nnn=0
    while(rule_1(All_lists[n][0],All_lists[n][1]) is False):
        nnn+=1
        if (nnn>100):
            break
        ## to compute the priority of the left and right lists
        L_left_pri=priority(All_lists[n][0])
        L_max_l=[]
        if (L_left_pri!=[[]] and L_left_pri!=[]):
            for i in range(0,len(L_left_pri)):
                if (L_left_pri[i]!=[]):
                    L_max_l.append(max(L_left_pri[i]))
            q=0
            qq=0
            xxx=0
            yyy=0
            while (max(L_max_l)==0):
                q=0
                qq+=1
                xxx=0
                yyy=0
                for i in range(0,len(All_lists[n][0])):
                    xxx=0
                    yyy=0
                    q=0
                    j=0
                    while (j<len(All_lists[n][0][i])):
                        if (All_lists[n][0][i][j]=='('):
                            xxx+=1
                        elif (All_lists[n][0][i][j]==')'):
                            yyy+=1
                        if (q==0 and All_lists[n][0][i][j]=='('):
                            del All_lists[n][0][i][j]
                            j=j-1
                            q+=1
                        elif (q==1 and All_lists[n][0][i][j]==')' and xxx==yyy):
                            del All_lists[n][0][i][j]
                            j=j-1
                            q+=1
                        elif (q==2):
                            break
                        j+=1
                if (q==0):
                    break
                else:
                    L_max_l=[]
                    L_left_pri=priority(All_lists[n][0])
                    for i in range(0,len(L_left_pri)):
                        L_max_l.append(max(L_left_pri[i]))
                    continue
            ## To compute the sequent: first left list and then right list
            if (q!=0 or qq==0):
                s=False
                for i in range(0,len(L_left_pri)):
                    for j in range(0,len(L_left_pri[i])):
                        if (L_left_pri[i][j]==max(L_max_l)):
                            x=i
                            y=j
                            s=True
                            break
                    if(s):
                        break
                L_l=copy.deepcopy(All_lists[n][0])
                if (L_l[x][y]=='neg'):
                    L_left_change,L_right_change=rule_2b(All_lists[n][0],All_lists[n][1],x,y)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    results.append([L_left_change,L_right_change])
                    rules.append('Rule P2b')
                elif (L_l[x][y]=='and'):
                    L_left_change,L_right_change=rule_3b(All_lists[n][0],All_lists[n][1],x,y)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    results.append([L_left_change,L_right_change])
                    rules.append('Rule P3b')
                elif (L_l[x][y]=='or'):
                    L_left_change1,L_left_change2,L_right_change=rule_4b(All_lists[n][0],All_lists[n][1],x,y)
                    All_lists[n][0]=copy.deepcopy(L_left_change1)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    All_lists.append([L_left_change2,L_right_change])
                    results.append([L_left_change1,L_right_change])
                    results.append(['add'])
                    results.append([L_left_change2,L_right_change])
                    rules.append('Rule P4b')
                elif (L_l[x][y]=='imp'):
                    L_left_change1,L_right_change1,L_left_change2,L_right_change2=rule_5b(All_lists[n][0],All_lists[n][1],x,y)
                    All_lists[n][0]=copy.deepcopy(L_left_change1)
                    All_lists[n][1]=copy.deepcopy(L_right_change1)
                    All_lists.append([L_left_change2,L_right_change2])
                    results.append([L_left_change1,L_right_change1])
                    results.append(['add'])
                    results.append([L_left_change2,L_right_change2])
                    rules.append('Rule P5b')
                elif (L_l[x][y]=='iff'):
                    L_left_change1,L_right_change1,L_left_change2,L_right_change2=rule_6b(All_lists[n][0],All_lists[n][1],x,y)
                    All_lists[n][0]=copy.deepcopy(L_left_change1)
                    All_lists[n][1]=copy.deepcopy(L_right_change1)
                    All_lists.append([L_left_change2,L_right_change2])
                    results.append([L_left_change1,L_right_change1])
                    results.append(['add'])
                    results.append([L_left_change2,L_right_change2])
                    rules.append('Rule P6b')
                else:
                    print("incorrect!")
        L_right_pri=priority(All_lists[n][1])
        L_max_r=[]
        if (L_right_pri!=[[]] and L_right_pri!=[]):
            q=0
            qqq=0
            xxx=0
            yyy=0
            for i in range(0,len(L_right_pri)):
                if (L_right_pri[i]!=[]):
                    L_max_r.append(max(L_right_pri[i]))
            while (max(L_max_r)==0):
                q=0
                qqq+=1
                xxx=0
                yyy=0
                for i in range(0,len(All_lists[n][1])):
                    xxx=0
                    yyy=0
                    q=0
                    j=0
                    while (j<len(All_lists[n][1][i])):
                        if (All_lists[n][1][i][j]=='('):
                            xxx+=1
                        elif (All_lists[n][1][i][j]==')'):
                            yyy+=1
                        if (q==0 and All_lists[n][1][i][j]=='('):
                            del All_lists[n][1][i][j]
                            q+=1
                            j=j-1
                        elif (q==1 and All_lists[n][1][i][j]==')' and xxx==yyy):
                            del All_lists[n][1][i][j]
                            q+=1
                            j=j-1
                        elif (q==2):
                            break
                        j+=1
                if (q==0):
                    break
                else:
                    L_max_r=[]
                    L_right_pri=priority(All_lists[n][1])
                    for i in range(0,len(L_right_pri)):
                        L_max_r.append(max(L_right_pri[i]))
                    continue
            if (q!=0 or qqq==0):
                s=False
                for i in range(0,len(L_right_pri)):
                    for j in range(0,len(L_right_pri[i])):
                        if (L_right_pri[i][j]==max(L_max_r)):
                            xr=i
                            yr=j
                            s=True
                            break
                    if(s):
                        break
                L_r=copy.deepcopy(All_lists[n][1])
                if (L_r[xr][yr]=='neg'):
                    L_left_change,L_right_change=rule_2a(All_lists[n][0],All_lists[n][1],xr,yr)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    results.append([L_left_change,L_right_change])
                    rules.append('Rule P2a')
                elif (L_r[xr][yr]=='and'):
                    L_left_change,L_right_change1,L_right_change2=rule_3a(All_lists[n][0],All_lists[n][1],xr,yr)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change1)
                    All_lists.append([L_left_change,L_right_change2])
                    results.append([L_left_change,L_right_change1])
                    results.append(['add'])
                    results.append([L_left_change,L_right_change2])
                    rules.append('Rule P3a')
                elif (L_r[xr][yr]=='or'):
                    L_left_change,L_right_change=rule_4a(All_lists[n][0],All_lists[n][1],xr,yr)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    results.append([L_left_change,L_right_change])
                    rules.append('Rule P4a')
                elif (L_r[xr][yr]=='imp'):
                    L_left_change,L_right_change=rule_5a(All_lists[n][0],All_lists[n][1],xr,yr)
                    All_lists[n][0]=copy.deepcopy(L_left_change)
                    All_lists[n][1]=copy.deepcopy(L_right_change)
                    results.append([L_left_change,L_right_change])
                    rules.append('Rule P5a')
                elif (L_r[xr][yr]=='iff'):
                    L_left_change1,L_right_change1,L_left_change2,L_right_change2=rule_6a(All_lists[n][0],All_lists[n][1],xr,yr)
                    All_lists[n][0]=copy.deepcopy(L_left_change1)
                    All_lists[n][1]=copy.deepcopy(L_right_change1)
                    All_lists.append([L_left_change2,L_right_change2])
                    results.append([L_left_change1,L_right_change1])
                    results.append(['add'])
                    results.append([L_left_change2,L_right_change2])
                    rules.append('Rule P6a')
                else:
                    print("incorrect!")
    n+=1
    rules.append('Rule 1')
    if (nnn>100):
        break
## output all the proofs in reversing order
if (nnn<=100):
    print("True.")
    print("---------")
    print("Proofs:")
    resultt=[]
    str_org=''
    q=0
    for i in range(0,len(L_org_sp)):
        str_org+=L_org_sp[i]+' '
##    for i in range(1,len(sys.argv)):
##        str_org+=sys.argv[i]+' '
    resultt.append(str_org)
    string=''
    i=0
    rest=[]
    rr=[[str_org]]
    e=0
    g=1
    while(i<len(results)):
        if (results[i]==['add']):
            rest.append(results[i+1])
            del results[i]
            g-=1
            i+=1
            continue
        else:
            rr.append(results[i])
        if (rules[i+e+g]=='Rule 1'):
            if (rest!=[]):
                rr.append(rest[0])
                e+=1
                del rest[0]
                while(rules[i+e+g]=='Rule 1'):
                    if (rest!=[]):
                        rr.append(rest[0])
                        e+=1
                        del rest[0]
                    else:
                        break
        i+=1
    if(rest!=[]):
        rr.append(rest[0])
    for i in range(1,len(rr)):
        string_right=''
        string_left=''
        string=''
        if (rr[i][0]==[]):
            string_left=''
        else:
            for k in range(0,len(rr[i][0])):
                for m in range(0,len(rr[i][0][k])):
                    string_left+=' '+rr[i][0][k][m]
                if (k<len(rr[i][0])-1):
                    string_left+=','
        if (rr[i][1]==[]):
            string_right=''
        else:
            for k in range(0,len(rr[i][1])):
                for m in range(0,len(rr[i][1][k])):
                    string_right+=' '+rr[i][1][k][m]
                if (k<len(rr[i][1])-1):
                    string_right+=','
        string='['+string_left+' ] '+'seq'+' ['+string_right+' ]'
        resultt.append(string)
    resultt.reverse()
    rules.reverse()
    len_r=[]
    for i in range(0,len(resultt)):
        len_r.append(len(resultt[i]))
    for i in range(0,len(resultt)):
        if (i+1<10):
            x=max(len_r)-len(resultt[i])+1
            print("{}.  {}".format((i+1),(resultt[i])),end='')
            for k in range(0,x):
                print(' ',end='')
            print(rules[i])
        else:
            x=max(len_r)-len(resultt[i])+1
            print("{}. {}".format((i+1),(resultt[i])),end='')
            for m in range(0,x):
                print(' ',end='')
            print(rules[i])
    print("----------")
    print("QED.")
else:
    print("False.")





