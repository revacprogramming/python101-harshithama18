

#"""get string input"""
def get_cs():
  str=input('Enter the shortcuts and its reps in form "word=sf"\n')
  return str

#"""convert connected string to list of strings"""
def cs_to_lot(cs,x):
  word=cs.split(';')
  for test in word:
     z=test.split('=')
     y=(z[0],z[1])
     x.append(y)
  return x
    
def main():
  cs = get_cs()
  lot=list()
  lot=cs_to_lot(cs,lot)
  #print(lot)
  #out=dict()
  #for test in lot:
  #   short = test.split('=')
  #    out[short[0]]=short[1]
  print(lot)

process=input('What process are you doing?\n')
if process == 'strsplit':
  main()

