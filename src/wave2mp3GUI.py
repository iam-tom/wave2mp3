#!/usr/bin/env python
import wx
import os
import sys
import random

import math
from threading import Thread

import wave2mp3


class dlg(wx.Frame):
  def __init__(self):


    self.cwd=os.getcwd()
    self.ts_dir_list = list()
    self.f=wx.Frame(None,title="Evaluation GUI",size=(650,300))

    # variables for output
    self.pf_list = list()
    self.ts_list = list()
    self.cl_list = list()



    self.makeLayout(self.f)
    self.makeBindings()
    self.f.Show()
  def makeBindings(self):
    self.dir_btn.Bind(wx.EVT_BUTTON,self.OnAddDir)
    self.pf_btn.Bind(wx.EVT_BUTTON,self.OnAddPf)
    self.ok_btn.Bind(wx.EVT_BUTTON,self.OnProcess)


    self.del_dir_btn.Bind(wx.EVT_BUTTON,lambda evt,gl=self.ts_glist,l=self.ts_dir_list :self.OnResetList(evt,l,gl))
    self.del_pf_btn .Bind(wx.EVT_BUTTON,lambda evt,gl=self.pf_glist,l=self.pf_list :self.OnResetList(evt,l,gl))

  def makeLayout(self,parent):
    pf_btn_txt=wx.StaticText(parent,-1,"Select .wav files")
    self.pf_btn=wx.Button(parent,-1,"Browse",(70,30))

    self.del_pf_btn=wx.Button(parent,-1,"Reset",(70,30))

    dir_btn_txt=wx.StaticText(parent,-1,"Output Directory")
    self.dir_btn=wx.Button(parent,-1,"Browse",(70,30))

    self.del_dir_btn=wx.Button(parent,-1,"Reset",(70,30))


    self.ok_btn=wx.Button(parent,-1,"WAV2MP3",(70,30))




    # visual feedback lists
    self.ts_glist=wx.ListBox(choices=[],id=-1,parent=parent,size=wx.Size(80,100))
    self.pf_glist=wx.ListBox(choices=[],id=-1,parent=parent,size=wx.Size(80,100))

    # dummy for filling empty spaces
    dummy=wx.StaticText(parent,-1,'')

    # Change to flexgridsizer
    ##sizer=wx.GridSizer(8,3,0,0)
    sizer=wx.FlexGridSizer(10,3,0,0)
    sizer.AddGrowableCol(2)


    sizer.Add(pf_btn_txt,1,wx.BOTTOM |wx.ALIGN_BOTTOM)
    sizer.Add(dummy,1,wx.EXPAND)
    sizer.Add(dummy,1,wx.EXPAND)

    sizer.Add(self.pf_btn,1)
    sizer.Add(self.del_pf_btn,1)
    sizer.Add(self.pf_glist,1,wx.EXPAND)


    sizer.Add(dir_btn_txt,1,wx.BOTTOM |wx.ALIGN_BOTTOM)
    sizer.Add(dummy,1,wx.EXPAND)
    sizer.Add(dummy,1,wx.EXPAND)

    sizer.Add(self.dir_btn,1)
    sizer.Add(self.del_dir_btn,1)
    sizer.Add(self.ts_glist,1,wx.EXPAND)
    sizer.Add(self.ok_btn,1)
    sizer.Add(dummy,1,wx.EXPAND)



    parent.SetSizer(sizer)
#################### CALLBACK ###########################
  def OnAddPf(self,e):
    self.pf_dlg=wx.FileDialog(None,"Select Probefile",style=wx.FD_MULTIPLE)
    if self.pf_dlg.ShowModal() == wx.ID_OK:
      temp_list= self.pf_dlg.GetPaths()
      self.i_list= self.pf_dlg.GetPaths()
      for temp in temp_list:
        self.pf_glist.Append(temp)

  def OnAddDir(self,e):
    self.ts_dlg=wx.DirDialog(None,"Select directories")
    if self.ts_dlg.ShowModal() == wx.ID_OK:
      self.o_dir=self.ts_dlg.GetPath()
      self.ts_dir_list.append(self.ts_dlg.GetPath())
      self.ts_glist.Append(self.ts_dir_list[-1])

  def OnProcess(self,e):
      cvtr=wave2mp3.converter(self.i_list,self.o_dir)
  def OnReset(self,e):
      self.delete_files()


  def OnResetList(self,e,l,gl):
    del l[:]
    gl.Clear()


  def reset_lists(self):
    del self.ts_list[:]
    del self.pf_list[:]
    del self.cl_list[:]






if __name__=="__main__":
  app= wx.App(False)
  dlg = dlg()
  #E=Evaluator()
  #a=list([2,3,3,4])
  #b=list([1,2,3,4])
  #d=list([2,3,3,4])
  #c=list(["1","2","3","4"])
  #E.add_epoch(a,b,c)
  #E.add_epoch(a,d,c)
  #print E.mean_error_rate()
  app.MainLoop()
