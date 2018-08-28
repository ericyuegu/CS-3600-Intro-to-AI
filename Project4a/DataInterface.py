def getConnect4Dataset(start = None, end = None):
  """
  Reads in and parses through the Connect4 dataset.
  
  Args:
    start (int): optional line number to start dataset at
    end (int): optional line number to end dataset at
  Returns:
    tuple<list<dictionary<str,str>>,
          dictionary<str,list<str>>,
          str,
          list<str>>
    
    List of examples as dictionaries, a dictionary mapping each
    attribute to all of its possible values, the name of the label
    in the example dictionaries, and the list of possible label values.
  """
  examples=[]
  attrValues={}
  data = open("datasets/connect4-data.txt")
  cols = ['a','b','c','d','e','f','g']
  rows = ['1','2','3','4','5','6']
  labelValues = ['win','loss','draw']
  for col in cols:
    for row in rows:
      attrValues[col+row]=['o','x','b']
  for line in data:
    dict = {}
    examples.append(dict)
    count=0
    for val in line.split(','):
      if count==42:
        dict['label']=val[:-1]
      else:
        dict[cols[count/6]+rows[count%6]]=val
      count+=1
  if start is not None and end is None:
    examples = examples[start:]
  elif start is None and end is not None:
    examples = examples[:end]
  elif start is not None and end is not None:
    examples = examples[start:end]
  return (examples,attrValues,'label',labelValues)

def getCarDataset(start = None, end = None):
  """
  Reads in and parses through the Car dataset.
  
  Args:
      start (int): optional line number to start dataset at
      end (int): optional line number to end dataset at
  Returns:
    tuple<list<dictionary<str,str>>,
          dictionary<str,list<str>>,
          str,
          list<str>>
      
  List of examples as dictionaries, a dictionary mapping each
  attribute to all of its possible values, the name of the label
  in the example dictionaries, and the list of possible label values.
  """
  examples=[]
  attrValues={}
  data = open("datasets/cars-data.txt")
  attrs = ['buying','maint','doors','persons','lug_boot','safety']
  attr_values = [['vhigh', 'high', 'med', 'low'],
                 ['vhigh', 'high', 'med', 'low'],
                 ['2','3','4','5more'],
                 ['2','4','more'],
                 ['small', 'med', 'big'],
                 ['high', 'med', 'low']]
  labelValues = ['unacc','acc','good','vgood']
  for index in range(len(attrs)):
    attrValues[attrs[index]]=attr_values[index]
  for line in data:
    dict = {}
    examples.append(dict)
    count=0
    for val in line.split(','):
      if count==6:
        dict['label']=val[:-1]
      else:
        dict[attrs[count]]=val
      count+=1
  if start is not None and end is None:
    examples = examples[start:]
  elif start is None and end is not None:
    examples = examples[:end]
  elif start is not None and end is not None:
    examples = examples[start:end]
  return (examples,attrValues,'label',labelValues)

# Dustiata Set #1: Simple Binary Classification with Binary Attributes
# Attributes: 10, Binary
# Labels: 1, 0
# Training Examples: 20
# Test Examples: 20

# Each list is an example, with each index corresponding to a feature
# The label for each example is below
data1TrainingExamples = [[0,1,1,0,0,1,0,1,0,1],
                         [0,0,1,1,0,1,1,0,0,1],
                         [1,1,1,1,0,1,0,0,1,0],
                         [1,0,1,0,1,0,1,1,1,1],
                         [0,0,1,0,0,0,0,0,0,1],
                         [1,0,0,0,1,0,0,0,0,0],
                         [1,0,0,0,0,1,1,1,1,0],
                         [1,0,0,0,0,0,1,0,1,0],
                         [1,1,0,1,1,1,1,1,1,1],
                         [0,0,0,0,1,1,0,1,1,0],
                         [1,0,1,0,1,1,0,0,0,1],
                         [1,0,0,1,1,1,1,0,1,1],         
                         [1,1,0,1,0,1,0,0,0,0],
                         [0,1,0,0,1,0,1,0,1,1],
                         [1,0,0,0,0,1,1,1,1,1],
                         [0,1,0,1,1,0,1,1,1,0],
                         [0,0,0,1,0,0,1,1,1,0],
                         [1,0,1,1,0,0,0,0,0,1],
                         [0,1,1,0,1,0,0,1,0,0],
                         [1,0,1,0,0,0,1,1,1,0]]

data1TrainingLabels = [0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1]

data1TestExamples = [[0,1,0,0,0,0,1,1,0,0],
                     [1,1,1,1,1,1,0,1,1,0],
                     [0,1,0,0,0,0,1,0,1,0],
                     [1,1,0,1,0,0,1,0,0,1],
                     [0,1,1,1,0,1,0,0,1,1],
                     [0,0,0,0,0,0,1,0,0,1],
                     [1,1,1,1,0,0,1,0,0,1],
                     [1,1,0,0,1,0,1,1,1,0],
                     [0,1,0,0,0,0,0,0,1,0],
                     [0,0,1,1,0,1,1,1,0,1],
                     [1,0,0,1,0,0,0,0,0,1],
                     [0,1,1,1,1,1,0,1,1,1],
                     [0,1,0,0,0,0,1,0,0,0],
                     [1,1,0,0,1,0,1,1,0,1],
                     [1,1,1,1,0,1,0,1,1,1],
                     [1,0,0,1,1,1,1,0,0,1],
                     [1,1,1,0,1,1,1,1,1,1],
                     [0,1,1,0,1,1,1,1,0,0],
                     [1,0,1,1,0,1,0,0,1,0],
                     [1,0,0,1,0,1,0,0,1,1]]

data1TestLabels = [1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0]

def convertListsToDictionary(examples,labels):
  """Helper method"""
  dictionaries = []
  for index in range(len(examples)):
    dict = {}
    for attrNum in range(len(examples[index])):
      dict[attrNum] = examples[index][attrNum]
    dict['label'] = labels[index]
    dictionaries.append(dict)
  return dictionaries

def getDummyDataset1(start=None,end=None,test=False):
  """
  Reads in and parses through the first dummy dataset.
  
  Args:
    start (int): optional line number to start dataset at
    end (int): optional line number to end dataset at
    test (bool): whether to return the test set, or the trainig set
  Returns:
    tuple<list<dictionary<str,str>>,
          dictionary<str,list<str>>,
          str,
          list<str>>
    
    List of examples as dictionaries, a dictionary mapping each
    attribute to all of its possible values, the name of the label
    in the example dictionaries, and the list of possible label values.
  """
  if test:
    dictionaries = convertListsToDictionary(data1TestExamples,data1TestLabels) 
  else:
    dictionaries = convertListsToDictionary(data1TrainingExamples,data1TrainingLabels)
  attrValues = {}
  labelValues = ['0','1']
  for attr in dictionaries[0].keys():
    if attr!='label':
      attrValues[attr]=[0,1]
  if start is not None and end is None:
    dictionaries = dictionaries[start:]
  elif start is None and end is not None:
    dictionaries = dictionaries[:end]
  elif start is not None and end is not None:
    dictionaries = dictionaries[start:end]
  return (dictionaries,attrValues,'label',labelValues)

def getDummyDataset2(start=None,end=None,test=False):
  """
  Reads in and parses through the second dummy dataset.
  
  Args:
    start (int): optional line number to start dataset at
    end (int): optional line number to end dataset at
    test (bool): whether to return the test set, or the trainig set
  Returns:
    tuple<list<dictionary<str,str>>,
          dictionary<str,list<str>>,
          str,
          list<str>>
    
    List of examples as dictionaries, a dictionary mapping each
    attribute to all of its possible values, the name of the label
    in the example dictionaries, and the list of possible label values.
  """
  if test:
    dictionaries = convertListsToDictionary(data2TestExamples,data2TestLabels)
  else:
    dictionaries = convertListsToDictionary(data2TrainingExamples,data2TrainingLabels)
  attrValues = {}
  labelValues = ['0','1']
  for attr in dictionaries[0].keys():
    if attr!='label':
      attrValues[attr]=[0,1]
  if start is not None and end is None:
    dictionaries = dictionaries[start:]
  elif start is None and end is not None:
    dictionaries = dictionaries[:end]
  elif start is not None and end is not None:
    dictionaries = dictionaries[start:end]
  return (dictionaries,attrValues,'label',labelValues)
  
# Data Set #2: Binary Classification with Binary Attributes
# Attributes: 10, Binary
# Labels: T, F
# Training Examples: 20
# Test Examples: 20

data2TestExamples = [[1,0,1,1,0,1,1,0,1,1],
                     [1,0,1,1,0,0,1,1,0,0],
                     [0,0,0,0,1,0,0,0,1,1],
                     [0,1,1,1,0,1,0,0,1,0],
                     [1,0,0,1,1,1,1,1,0,1],
                     [0,0,0,1,0,0,1,0,1,1],
                     [0,1,1,0,0,0,1,1,0,0],
                     [1,0,0,1,0,1,0,1,0,0],
                     [0,1,1,0,1,1,0,0,0,1],
                     [0,1,0,1,0,0,0,0,0,0],
                     [1,0,0,1,1,0,0,0,1,1],
                     [0,1,1,1,0,0,0,1,1,0],
                     [1,1,1,1,1,1,0,0,1,0],
                     [1,1,1,0,1,0,1,0,1,1],
                     [1,0,1,0,1,1,0,1,1,1],
                     [1,0,0,1,0,1,1,1,1,0],
                     [0,1,0,1,1,0,1,1,1,0],
                     [0,0,1,1,0,1,1,1,1,0],
                     [0,1,1,1,1,0,1,1,0,1],
                     [1,0,1,1,1,1,1,0,0,1]]

data2TrainingLabels = [1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1]

data2TrainingExamples = [[1,1,1,1,0,1,1,1,0,1],
                         [0,0,0,0,1,0,1,0,1,1],
                         [0,1,1,1,0,1,0,0,1,1],
                         [0,1,0,1,1,0,0,0,0,1],
                         [0,1,0,0,1,0,0,0,0,0],
                         [1,0,0,1,1,0,1,0,1,0],
                         [1,1,1,0,1,0,1,1,1,0],
                         [1,1,0,0,1,0,1,1,0,0],
                         [1,1,1,1,0,0,1,1,1,1],
                         [1,1,1,0,0,0,0,0,0,1],
                         [0,1,0,0,1,0,0,0,0,0],
                         [1,0,1,1,0,1,1,1,0,1],
                         [0,0,0,1,0,0,1,0,1,1],
                         [0,1,1,1,0,1,1,0,0,1],
                         [0,0,0,0,0,1,0,0,1,0],
                         [0,1,1,1,0,1,0,0,1,1],
                         [0,0,0,1,0,1,1,1,1,0],
                         [1,1,0,1,0,0,1,1,1,0],
                         [0,1,1,0,0,1,1,1,1,0],
                         [1,0,1,0,1,1,1,0,0,1]]

data2TestLabels = [1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
