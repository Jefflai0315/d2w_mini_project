

def mergesort(array, byfunc=None):


  if len(array) >1:
    n = len(array)//2
    L = mergesort(array[0:n],byfunc)
    R = mergesort(array[n:],byfunc)
    nleft = len(array[0:n]) 
    nright = len(array[n:])
    left = 0 
    right = 0
    dest = 0
    while left <nleft and right<nright:
        if byfunc(L[left]) <= byfunc(R[right]):
            array[dest] = L[left]  
            left += 1

        else:
            array[dest] = R[right]
            right += 1
        dest += 1
    while left <nleft :
        array[dest] = L[left]
        left += 1
        dest+= 1
    while right < nright :
        array[dest]  =  R[right] 
        right += 1
        dest+= 1
  return array


class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        assert item is not None
        self.__items.append(item)
        return self.__items

    def pop(self):
        if len(self.__items) ==0: 
            return None
        else:
            
            return self.__items.pop(-1)

    def peek(self):
        if len(self.__items) ==0: 
            return None
        else:
            return self.__items[-1]

    @property
    def is_empty(self):
        return len(self.__items) ==0
            

    @property
    def size(self):
        if len(self.__items) !=0:
            return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '

  def __init__(self, string=""):
    self._expr = string
    

  @property
  def expression(self):
    return self._expr

  @expression.setter
  def expression(self, new_expr):
    for c in new_expr:
      if c not in EvaluateExpression.valid_char:
        self._expr = ""
        print(self._expr + " is wrong ")
        return str(self._expr)


    self._expr = new_expr
    
    return self._expr

  def insert_space(self):
    ls = []

    for i in range(len(self._expr)):
      if self._expr[i] in "+-*/()" :
        ls.extend((' ',self._expr[i],' '))
      else:
        ls.append(self._expr[i])
    
    string = ''.join(ls)
    
    return string

  def process_operator(self, operand_stack, operator_stack):
    R = operand_stack.pop()
    L = operand_stack.pop()
    op = operator_stack.pop()
    print(op)
    if op == '/':
      op = '//'  

    result = eval(''.join(map(str,[L , op , R])))
    
    operand_stack.push(result)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    print(expression, tokens)
    
    for c in tokens:
      if c not in '*/+-()':
        if operand_stack.peek() == '-':
          minus = operand_stack.pop()
          to_add = minus + c
          operand_stack.push(to_add)
        else: 
          operand_stack.push(c)
        print('1',operand_stack._Stack__items,operator_stack._Stack__items)


      if c in '+-':

        if c in '-':
          operand_stack.push(c)
          
        else:
          while (not operator_stack.is_empty) and (operator_stack.peek() not in '()'):
            R = operand_stack.pop()
            L = operand_stack.pop()
            op = operator_stack.pop()
            print(op)
            if op == '/':
              op = '//'  

            result = eval(''.join(map(str,[L , op , R])))
            print(result)
            operand_stack.push(result)
            
          operator_stack.push(c)
          print('2',operand_stack._Stack__items,operator_stack._Stack__items)


      if c in "*/" :
        print("this is the token in if c in '/*'", c)
        while operator_stack.peek() is not None and operator_stack.peek() in '*/':
          
          
          R = operand_stack.pop()
          L = operand_stack.pop()
          op = operator_stack.pop()
          print(op)
          if op == '/':
            op = '//'  

          result = eval(''.join(map(str,[L , op , R])))
          operand_stack.push(result)
        operator_stack.push(c)
        print('3',operand_stack._Stack__items,operator_stack._Stack__items)


      if c == '(':
        operator_stack.push(c)

      if c ==')':
        while operator_stack.peek() != '(':
          R = operand_stack.pop()
          L = operand_stack.pop()
          op = operator_stack.pop()
          print(op)
          if op == '/':
            op = '//'  

          result = eval(''.join(map(str,[L , op , R])))
          operand_stack.push(result)
        print('4',operand_stack._Stack__items,operator_stack._Stack__items)


    print(operand_stack._Stack__items,operator_stack._Stack__items)

    while  operator_stack.peek() != None:
      if operator_stack.peek() == '(' and operator_stack.size >1:
        print("operator_stack.peek() == '(' and operator_stack.size >1")
        R = operand_stack.pop() 
        L = operand_stack.pop()
        operator_stack.pop()
        op = '*'
        result = eval(''.join(map(str,[L , op , R])))
        operand_stack.push(result)
      
      
        just_pop = operator_stack.pop()
        print(just_pop)

      if operator_stack.peek() != None:
        R = operand_stack.pop() 

        L = operand_stack.pop()
        op = operator_stack.pop()
        print(op,L,R)
        if op == '/':
          op = '//'  

        result = eval(''.join(map(str,[L , op , R])))
        operand_stack.push(result)
        print(operand_stack.peek())
      

    result1 = operand_stack.pop()
    print(result1)
    return result1



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]






