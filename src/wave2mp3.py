import os
import subprocess
import sys


class converter:
  def __init__(self,ifiles,o_dir):
    self.ifiles=ifiles
    self.o_dir=o_dir
    env=sys.platform
    if(env.find("linux2")==0):
      self.binary="avconv"
    elif(env.find("win32")==0):
      self.binary=os.path.join("..","bin","win32","usr","bin","avconv.exe")

    self.process()
  def process(self):
    for i_f in self.ifiles:
      o=os.path.splitext(i_f)[0]
      o=o+".mp3"
      o=os.path.split(o)[1]
      print o
      o_f=os.path.join(self.o_dir,o)
      print o_f
      subprocess.Popen([self.binary,"-i",i_f,"-y",o_f])

if __name__=="__main__":
  w2p3=wave2mp3()
