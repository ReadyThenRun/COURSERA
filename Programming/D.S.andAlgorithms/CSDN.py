#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#made by Sucs Liu
#2017-11-21
import math
import random
import time
def Solution():#返回距离最近的点对及它们的距离
    #测试数据生成

    AX = []
    AY = []
    for i in range(1, 10000):#生成一万个数据
        AX.append(random.randint(0, 100000))
        AY.append(random.randint(0, 100000))
    PairPointA = list(zip(AX, AY))#一维数组到二维数组
    #print(list(PairPointA))    
    #PairPointA = [(1, 2), (2, 6), (7, 8), (-1, 9), (0, 12), (10, 10)]
    #PairPointA = [(0, 1), (3, 2), (4, 3), (5, 1), (1, 2), (2, 1), (6, 2), (7, 2), (8, 3), (4, 5), (9, 0), (6, 4)]
    #预排序
    SAx = sorted(PairPointA, key = lambda point: point[0]) # Sorted Array
    SAy = sorted(PairPointA, key = lambda point: point[1]) #
    #print(SAx, '\n', SAy)
    #minpair, mindist = BruteSolution(PairPointA)#测试暴力解决
    #print(mindist,'\n', minpair)
    #进行递归求解
    minpair, mindist = FindClosestPairPoint(SAx, SAy)
    return minpair, mindist


def BruteSolution(PairPointA):#暴力法  时间复杂度O(n*n)
    Alen = len(PairPointA)
    #初始化 mindist, minpair
    mindist = GetDistance(PairPointA[0], PairPointA[1])
    minpair = (PairPointA[0], PairPointA[1])
    #遍历 
    for i in range(0, Alen-2):
        for j in range(i+1, Alen-1):
            dist = GetDistance(PairPointA[i], PairPointA[j])
            if mindist > dist:
                mindist = dist
                minpair = (PairPointA[i], PairPointA[j])
    return minpair, mindist

def GetDistance(point1, point2):
    # distc = sqrt( (x1-x2)**2 + (y1 - y2)**2 )
    return math.sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def MidAreaMin(SAx, SAy, delta): #总时间复杂度为O(n)
    #获取在2*delta区域内的点，并按y坐标排序
    SAlen = len(SAx)
    midXvalue = SAx[SAlen//2][0]
    SAydelta = []
    for point in SAy: #根据SAy中点的x的坐标是否在 2*delta区域内来判断该点是否在区域内，时间复杂度为 O(n)
        if midXvalue - delta <= point[0] <= midXvalue +delta:
            SAydelta.append(point)
    SAydlen = len(SAydelta)
    #print('SAydlen:%s'%SAydlen)
    #初始化 mindist, minpair
    if SAydlen <= 1:#处理过的y数组可能只有一个元素，需要单独处理
        return ((0,0), (0, 0)) , (delta +1)#返回一个大于delta的距离，来忽略这类情况
    mindist = GetDistance(SAydelta[0], SAydelta[1])
    minpair = (SAydelta[0], SAydelta[1])

    for i in range(0, SAydlen-2):# 遍历2*delta内的各点对，时间复杂度为 O(5*n)
        for j in range(i+1, min(i+5, SAydlen-1)):
            dist = GetDistance(SAydelta[i], SAydelta[j])
            if mindist > dist:
                mindist = dist
                minpair = (SAydelta[i], SAydelta[j])
    return minpair, mindist


def FindClosestPairPoint(SAx, SAy):# T(n) = 2*T(n/2) + O(n)
    SAlen = len(SAx)
    if SAlen <= 3:#递归出口
        minpair, mindist = BruteSolution(SAx)
        return minpair, mindist
    else:
        #分解
        midx =  SAlen//2 #分割线位置
        SAxl = SAx[0: midx]#子问题Left 按x坐标排序
        SAxr = SAx[midx: ] #子问题Right 按x排序
        SAyl, SAyr = [], []
        midXvalue = SAx[midx][0] #分割线的位置的值 
        for point in SAy: #子问题Left、Right按y排序
            if point[0] < midXvalue:
                SAyl.append(point)
            else:
                SAyr.append(point)
        #递归解决
        minpairL, mindistL = FindClosestPairPoint(SAxl, SAyl)
        minpairR, mindistR = FindClosestPairPoint(SAxr, SAyr)
        #合并
        if mindistL < mindistR:#合并两个字问题的解
            mindist = mindistL
            minpair = minpairL
        else:
            mindist = mindistR
            minpair = minpairR

        minpairM, mindistM = MidAreaMin(SAx, SAy, mindist)#处理delta*2delta区域内的点对距离

        if mindist > mindistM:
            mindist = mindistM
            minpair = minpairM
    return minpair, mindist

#输出调试模块
Tstart = time.time()
minpair, mindist = Solution()
Tfinish = time.time()
print('closest pair point is :%s\nthe distance is :%s  TimeUsed: %s s' %(minpair, mindist, (Tfinish-Tstart)))
