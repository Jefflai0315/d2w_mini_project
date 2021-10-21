

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
    if op == '/':
      op = '//'  

    result = eval(''.join(map(str,[L , op , R])))
    print("processing:  ", L , op , R)
    operand_stack.push(result)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    print("expression",expression)
    print("token", tokens)

    operator = ['*','/','+','-','(',')']

    prev_operand = True   
    #to check if the previous c-character is an operator
    #to account for case eg: 2*-2

    for c in tokens:
      print("char: ",c, "operand stack: ",operand_stack._Stack__items, "operator stack: " , operator_stack._Stack__items)
      
      if c not in operator: #add operand to operand stack
        operand_stack.push(c) 
        prev_operand = True
      
      elif c in '+-':
        
        if  c =='-' and operand_stack.is_empty: #if the first character is "c", add "0-{the rest}" into the equation
          operand_stack.push(0)
          operator_stack.push(c)
        elif c == "-" and prev_operand == False: # this is to account for eg: 2*-2 case
         
          if operator_stack.peek() in ['*','/'] :
            print('when "-" meets "*/"')
            print('pushing "-1" and "*/" into the Operand and Operator Stack respectively')
              
            operand_stack.push('-1') #from eg: 2*-2 
            operator_stack.push('*') # to eg: 2 * [-1] * 2
          
          elif operator_stack.peek() =="(":
            operand_stack.push(0)
            operator_stack.push(c)
        else:
          while (not operator_stack.is_empty) and (operator_stack.peek() not in ['(',')']): #process operator with the conditions
            self.process_operator( operand_stack, operator_stack)
          operator_stack.push(c)
          prev_operand = False
      
      

      elif c in '*/':
        while operator_stack.peek() in ['*','/']:
          self.process_operator( operand_stack, operator_stack)
        operator_stack.push(c)
        prev_operand = False

      elif c == '(':
        operator_stack.push(c)
        prev_operand = False

      elif c == ')':
        while operator_stack.peek() != '(':
          self.process_operator( operand_stack, operator_stack)
        

    print('whats remaining: ' , 'Operand: ', operand_stack._Stack__items, ' Operator: ', operator_stack._Stack__items  )

    while not operator_stack.is_empty and operand_stack.size>1:

      if operator_stack.peek() in '()':
        operator_stack.pop()
      else:
        self.process_operator( operand_stack, operator_stack)

    return operand_stack.pop()













  '''def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    print(expression, tokens)

    operator = ['*','/','+','-','(',')']


    for c in tokens:
      print(c, operand_stack._Stack__items, operator_stack._Stack__items)
      if c not in operator:
        operand_stack.push(c)
      
      elif c in '+-':
        if c == "-":
          if operator_stack.peek() in ['*','/'] and operand_stack.size >= 2:
            while (not operator_stack.is_empty) and (operator_stack.peek() not in '()'):
              print('come in')
              self.process_operator(operand_stack, operator_stack)
              
            operand_stack.push('1') #accomodate the minus
            operator_stack.push('*')
          else:
            operand_stack.push('-1') #accomodate the minus
            operator_stack.push('*')

        else:
          while (not operator_stack.is_empty) and (operator_stack.peek() not in '()'):
            self.process_operator(operand_stack, operator_stack)
          operator_stack.push(c)

      elif c in '*/':
        while operand_stack.size >=2 and operator_stack.peek() in '*/' :
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(c)

      elif c == '(':
        operator_stack.push(c)

      elif c == ')':
        while operator_stack.peek() != '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(c)
        
        if operand_stack.size >=2 and operator_stack.size >2:
          if operator_stack._Stack__items[-1] == ')' and operator_stack._Stack__items[-2] == '(' and operand_stack._Stack__items[-2]== '-1':
            print(operator_stack._Stack__items[-1], operator_stack._Stack__items[-2])
            operator_stack.pop()
            operator_stack.pop()
            R= operand_stack.pop()
            L = operand_stack.pop()
            op = operator_stack.pop()
            result = eval(''.join(map(str,[L ,op, R])))
            print(result)
            operand_stack.push(result)


    print('whats remaining: ' , 'Operand: ', operand_stack._Stack__items, ' Operator: ', operator_stack._Stack__items  )

    while not operator_stack.is_empty:

      if operator_stack.peek() in '()':
        
        operator_stack.pop()

      elif operand_stack.size >=2:
        self.process_operator(operand_stack, operator_stack)
      else:
        print('operand stack < 2 items, cant operate')
    
    if operator_stack.is_empty and operand_stack.size>=2: # if left all negative values
      R = operand_stack.pop()
      L = operand_stack.pop()
      result = eval(''.join(map(str,[L,'+', R])))
    
      operand_stack.push(result)

    return operand_stack.pop()'''



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]






