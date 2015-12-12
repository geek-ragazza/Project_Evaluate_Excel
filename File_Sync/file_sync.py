#coding=utf-8
import os.path, time
import os, sys
import datetime
import shutil
import queue, threading
from Tkinter import *


from tkFileDialog import askopenfilename,askdirectory     
import sqlite3 as lite
import multiprocessing
from multiprocessing import Pool, freeze_support
from threading import Thread

def EntryIn(row, col, text, frameName,widthlenth):

        InputE = StringVar()
        EOil = Entry(frameName, width=widthlenth, font = "Helvetica 12",  textvariable=InputE, state='readonly', borderwidth=1,
                     insertbackground="red")   
        EOil.grid(row=row, column=col, sticky=W, padx=5)
        InputE.set(text)
        return InputE
def ButtonTreAction(LocalPath,RemotePath):
        ThArr=[]
        #Lval=RemoteL.get()
        #print Lval
        for pathinfile, subdirs, files in betterwalk.walk(LocalPath):
                        
                i=0
                threads = []
                for TempFilePath in map(lambda x:os.path.join(pathinfile,x),files):
                        writeINdb(TempFilePath,LocalPath,RemotePath)
                        #ThArr.append([TempFilePath,LocalPath,RemotePath])
                        #t = multiprocessing.Process(target=writeINdb, args=(TempFilePath,LocalPath,RemotePath,))
                        #threads.append(t)
                        #t.start()
                        #p = Pool(5)
                        #p.map(writeINdb,ThArr)
                        #ThArr=[]
def FastAction(LocalPath,RemotePath):
        ThArr=[]
        #Lval=RemoteL.get()
        #print Lval
        for pathinfile, subdirs, files in betterwalk.walk(LocalPath):
                        
                i=0
                threads = []
                for TempFilePath in map(lambda x:os.path.join(pathinfile,x),files):
                        writeINdb(TempFilePath,LocalPath,RemotePath)
                        #ThArr.append([TempFilePath,LocalPath,RemotePath])
                        t = multiprocessing.Process(target=writeINdb, args=(TempFilePath,LocalPath,RemotePath))
                        threads.append(t)
                        t.start()
                        #p = Pool(5)
                        #p.map(writeINdb,ThArr)
                        #ThArr=[]                                                
                               
                        
        print "DONE"   
def writeINdb(TempFilePath,LocalPath,RemotePath):
        
        OriginPath = TempFilePath
        CheckCopyPath = RemotePath+TempFilePath[len(LocalPath):]
        
        #print OriginPath
        if not os.path.exists(CheckCopyPath):
                folderPath=os.path.dirname(CheckCopyPath)
                try:
                        os.makedirs(folderPath)
                        #print folderPath
                        try:
                                shutil.copy2(OriginPath,CheckCopyPath)
                                #Thread(target=shutil.copy2, args=[OriginPath,CheckCopyPath]).start()
                        except:
                                pass
                        
                except:
                        try:
                                shutil.copy2(OriginPath,CheckCopyPath)
                                #Thread(target=shutil.copy2, args=[OriginPath,CheckCopyPath]).start()
                                
                        except:
                                pass
        else:
                if os.path.isdir(OriginPath) != True:
                        
                
                        LModified_Time=os.path.getmtime(OriginPath)
                        #LCreated_Time=os.path.getctime(OriginPath)
                        RModified_Time=os.path.getmtime(CheckCopyPath)
                        if RModified_Time!=LModified_Time:
                                try:
                                        shutil.copy2(OriginPath,CheckCopyPath)
                                        #Thread(target=shutil.copy2, args=[OriginPath,CheckCopyPath]).start()
                                except IOError:
                                        try:
                                                shutil.copy2(OriginPath,CheckCopyPath)
                                                #Thread(target=shutil.copy2, args=[OriginPath,CheckCopyPath]).start()
                                        except:
                                                pass

                        
def slowCopy(butnum):
        
        if butnum==1:
                global directory_pathL
                directory_pathL= "//Ecs01/ddb00/DEPT"
                RemoteL=EntryIn(3, 0, directory_pathL, F1,20)
        if butnum==2:
                global directory_pathR
                directory_pathR= askdirectory()
                RemoteE=EntryIn(3, 1, directory_pathR, F1,20)
        #start check
        if butnum==3:
                
                LocalPath = directory_pathL.replace('/','\\')
                RemotePath = directory_pathR.replace('/','\\')
                
                ButtonTreAction(LocalPath,RemotePath)
def OnceUpon():
        
        LocalPath = directory_pathL.replace('/','\\')
        RemotePath = directory_pathR.replace('/','\\')
        LocalPath="\\\\Ecs01\\ddb00\\DEPT\\採購發包歷史檔"
        import serial
        LocalPath=os.path.realpath(LocalPath)
        print RemotePath, LocalPath
        ButtonTreAction(LocalPath,RemotePath)
def FastSync():
        LocalPath = directory_pathL.replace('/','\\')
        RemotePath = directory_pathR.replace('/','\\')
        
        FastAction(LocalPath,RemotePath)
        





if __name__ == "__main__":
        freeze_support()
        root = Tk()
        root.geometry('400x300+500+300')
        root.configure(background ='#E2E2E2')
        F1 = Frame(root)
        F1.grid(row=0, column=0)
        F1.configure(background ='#E2E2E2')
        F2 = Frame(root)
        F2.grid(row=0, column=1)
        F2.configure(background ='#E2E2E2')


        errmsg = 'Error!'




        LocalBut1=Button(F1, text='Local File Open', command=lambda: slowCopy(1))
        LocalBut1.grid(row = 2, column = 0)
        RemoteBut1=Button(F1, text='Remote File Open', command=lambda: slowCopy(2))
        RemoteBut1.grid(row = 2, column = 1)

        StartBut1=Button(F1, text='Slow Sync', command=OnceUpon)
        StartBut1.grid(row = 4, column = 0)
        StartBut1=Button(F1, text='Fast Sync', command=FastSync)
        StartBut1.grid(row = 6, column = 0)
        root.mainloop()

