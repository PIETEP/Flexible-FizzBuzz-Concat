import sys
import re

def main(argv):

  final=len(argv)-1
  m=int(argv[final])
  answer=""
  list=[]
  slist=[]
  
  for i in range(final):
    place=argv[i].index(':')
    divide=int(argv[i][0:place])
    if m%divide==0:
      list.append(int(argv[i][0:place]))
      slist.append(argv[i][place+1:])
     
  
  copylist=list.copy()
  list.sort()

  for i in range(len(list)):
    Basyo=copylist.index(list[i])
    answer=answer+slist[i]
  if not answer:
    print(m)
  else:
    print(answer)

if __name__ == '__main__':
  main(sys.argv[1:])
