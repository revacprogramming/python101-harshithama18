def input_two_numbers():
  x = input('Input: ')
  y = x.split()
  g=y[0]
  h=y[1]
  return g,h

def add(a, b):
  u=int(a)
  v=int(b)
  p= u+v
  return p

def output(a,b,sum):
  print(a,'+',b,'is',sum)

def main():
  a, b = input_two_numbers()
  sum = add(a,b)
  output(a,b,sum)

__name__=input('What are you doing?')
if __name__ == 'addition':
  main()
  """
def add(a, b):
    pass  # ...


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
"""