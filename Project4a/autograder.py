import DataInterface
import DecisionTree
import traceback
import sys
import getopt
from os import listdir
import cPickle as pickle
def q1Test(testFile,module=None):
    module = DecisionTree if module is None else module
    testFuncName = testFile.readline().strip()
    getData = getattr(DataInterface, testFuncName)
    testRangeStart = int(testFile.readline().strip())
    testRangeEnd = int(testFile.readline().strip())
    testRangeStart = None if testRangeStart=='None' else int(testRangeStart)
    testRangeEnd = None if testRangeEnd=='None' else int(testRangeEnd)
    examples = getData(start=testRangeStart,end=testRangeEnd)[0]
    if 'Pertinent' in testFile.name:
        attrName = testFile.readline().strip()
        attrValue = testFile.readline().strip()
        solution = module.getPertinentExamples(examples, attrName, attrValue)
    elif 'Class' in testFile.name:
        className = testFile.readline().strip()
        solution = module.getClassCounts(examples, className)
    elif 'Attr' in testFile.name:
        attrName = testFile.readline().strip()
        attrVals = testFile.readline().strip().split(',')
        className = testFile.readline().strip()
        solution = module.getAttributeCounts(examples, attrName, attrVals, className)
    return solution

def q2Test(testFile,module=None):
    module = DecisionTree if module is None else module
    testFuncName = testFile.readline().strip()
    getData = getattr(DataInterface, testFuncName)
    testRangeStart = testFile.readline().strip()
    testRangeEnd = testFile.readline().strip()
    testRangeStart = None if testRangeStart=='None' else int(testRangeStart)
    testRangeEnd = None if testRangeEnd=='None' else int(testRangeEnd)
    examples = getData(start=testRangeStart,end=testRangeEnd)[0]
    if 'Entropy' in testFile.name:
        className = testFile.readline().strip()
        classCounts = module.getClassCounts(examples,className).values()
        solution = module.setEntropy(classCounts)
    elif 'remainder' in testFile.name:
        attrName = testFile.readline().strip()
        attrVals = testFile.readline().strip().split(',')
        className = testFile.readline().strip()
        solution = module.remainder(examples, attrName, attrVals, className)
    elif 'infoGain' in testFile.name:
        attrName = testFile.readline().strip()
        attrVals = testFile.readline().strip().split(',')
        className = testFile.readline().strip()
        solution = module.infoGain(examples, attrName, attrVals, className)
    return solution

def q3Test(testFile,module=None):
    module = DecisionTree if module is None else module
    testFuncName = testFile.readline().strip()
    getData = getattr(DataInterface, testFuncName)
    testRangeStart = testFile.readline().strip()
    testRangeEnd = testFile.readline().strip()
    testRangeStart = None if testRangeStart=='None' else int(testRangeStart)
    testRangeEnd = None if testRangeEnd=='None' else int(testRangeEnd)
    examples = getData(start=testRangeStart,end=testRangeEnd)[0]
    if 'Index' in testFile.name:
        className = testFile.readline().strip()
        classCounts = module.getClassCounts(examples,className).values()
        solution = module.giniIndex(classCounts)
    elif 'Gain' in testFile.name:
        attrName = testFile.readline().strip()
        attrVals = testFile.readline().strip().split(',')
        className = testFile.readline().strip()
        solution = module.giniGain(examples, attrName, attrVals, className)
    return solution

def q4Test(testFile,module=None):
    module = DecisionTree if module is None else module
    testFuncName = testFile.readline().strip()
    getData = getattr(DataInterface, testFuncName)
    testRangeStart = testFile.readline().strip()
    testRangeEnd = testFile.readline().strip()
    testRangeStart = None if testRangeStart=='None' else int(testRangeStart)
    testRangeEnd = None if testRangeEnd=='None' else int(testRangeEnd)
    examples,attrValues,labelName,labelValues = getData(start=testRangeStart,end=testRangeEnd)
    attrFuncName = testFile.readline().strip()
    attrFunc = getattr(module,attrFuncName)
    gainFuncName = testFile.readline().strip()
    gainFunc = getattr(module,gainFuncName)
    tree = module.makeTree(examples, attrValues, labelName, attrFunc, gainFunc)
    #pickle.dump( tree, open( testFile.name+'Tree', "wb" ) )
    return tree

def q5Test(testFile,module=None):
    module = DecisionTree if module is None else module
    varNames = testFile.readline().rstrip().split(',')
    storedTree = pickle.load(open(testFile.name[:-4]+'Tree','r'))
    tree = DecisionTree.Tree(storedTree.root)
    result = []
    for line in testFile:
      vals = line.rstrip().split(',')
      cData = dict(zip(varNames,vals))
      result.append(tree.classify(cData))
    return result

def q9Test(testFile,module=None):
    module = DecisionTree if module is None else module
    testFuncName = testFile.readline().strip()
    getData = getattr(DataInterface, testFuncName)
    testRangeStart = testFile.readline().strip()
    testRangeEnd = testFile.readline().strip()
    testRangeStart = None if testRangeStart=='None' else int(testRangeStart)
    testRangeEnd = None if testRangeEnd=='None' else int(testRangeEnd)
    examples,attrValues,labelName,labelValues = getData(start=testRangeStart,end=testRangeEnd)
    attrFuncName = testFile.readline().strip()
    attrFunc = getattr(module,attrFuncName)
    gainFuncName = testFile.readline().strip()
    gainFunc = getattr(module,gainFuncName)
    tree = module.makePrunedTree(examples, attrValues, labelName, attrFunc, gainFunc, 0.05)
    #pickle.dump( tree, open( testFile.name+'Tree', "wb" ) )
    return tree
  
def getFile(name, q):
    return open('test_cases/'+q+'/'+name)

def runTests(q,points=2):
    total = 0
    possible = 0
    testFunc = globals()[q+'Test']
    correct=False
    print 'Running %s tests\n'%q
    for fileName in [name for name in listdir('test_cases/'+q) if 'test' in name]:
        possible+=1
        print 'Running test %s'%fileName
        
        try:
            solFile = open('test_cases/'+q+'/'+fileName.replace('.test','.solution'))
            solution = solFile.read().split(';')
        except Exception,e:
            print 'No solution file found'
            continue
        
        try:
            result = testFunc(getFile(fileName,q))
            exec(solution[0].strip())
        except Exception,e:
            print 'You broke something:'
            print traceback.format_exc()
            continue
        if correct:
            total+=1
            print 'Correct answer!'
        else:
            print 'Your answer is incorrect'
            print 'Your answer: %s'%str(result)
            print 'Correct answer: %s\n'%str(solution[1].strip())
    
        print '--------------------------------------------------------------------'
    if total==possible:
        print 'All tests passed - score %d/%d'%(points,points)
        print 'Done\n____________________________________________________________________\n'
        return (points,points)
    else:
        print 'Not all tests passed - score 0/%d'%points
        print 'Done\n____________________________________________________________________\n'
        return (0,points)

def runTest(test,questions):
    try:
        solFile = open(test.replace('.test','.solution'))
        solution = solFile.read().split(';')
        q = None
        for question in questions:
            if question in test:
                q = question
        testFunc = globals()[q+'Test']
        result = testFunc(open(test))
        correct = False
        exec(solution[0].strip())
        if correct:
            print 'Correct answer!'
        else:
            print 'Your answer is incorrect'
            print 'Your answer:\n %s'%str(result)
            print 'Correct answer:\n %s\n'%str(solution[1].strip())
    except Exception,e:
        print 'No solution file found for test %s, or you broke something'%test

def sameList(list1,list2,error=0.00001):
    return list1==list2

def makeSolutionsFiles(q, floatDif = 0.00001,ordered=True):
    testFunc = globals()[q+'Test']
    for fileName in [name for name in listdir('test_cases/'+q) if 'test' in name]:
        print 'Creating solution file for test %s'%fileName
        solution = testFunc(getFile(fileName,q))
        solFile = open('test_cases/'+q+'/'+fileName.replace('.test','.solution'),'w')
        if isinstance(solution,float):
            solFile.write('correct=abs(result-%f)<%f;\n%f'%(solution,floatDif,solution))    
        else:
            solFile.write('correct=result=="""%s""";\n%s'%(str(solution),str(solution)))    
        print 'Solution is \n%s\n'%str(solution)

def q1Tests():
    return runTests('q1',2)

def q2Tests():
    return runTests('q2',2)

def q3Tests():
    return runTests('q3',2)

def q4Tests():
    return runTests('q4',4)

def q5Tests():
    return runTests('q5',2)

def q9Tests():
    return runTests('q9',2)

help_string = 'Usage: autograder.py [options]\n\
\
Run public tests on student code\n\
\
Options:\n\
  -h, --help            show this help message and exit\n\
  -t RUNTEST, --test=RUNTEST\n\
                        Run one particular test.  Relative to test root.\n\
  -q GRADEQUESTION, --question=GRADEQUESTION\n\
                        Grade one particular question.'

def main():
	args = sys.argv
	questions = ['q1','q2','q3','q4','q5']
	if len(args)==1:
	    sumTotal= 0
	    sumPossible = 0
	    for q in questions:
	        func = globals()[q+'Tests']
	        total, possible = func()
	        sumTotal+=total
	        sumPossible+=possible 
	    print '\nAutograder finished. Final score %d/%d'%(sumTotal,sumPossible)
	else:
	    opts, args = getopt.getopt(args[1:],"q:t:h",["q=","test=","help"])
	    for opt, arg in opts:
	        if opt=='-q' or opt=='--q':
	            if arg in questions or arg=='q9':
	                func = globals()[arg+'Tests']
	                func()
	        elif opt=='-t' or opt=='--test':
	            runTest(arg,questions)
	        elif opt=='-h' or opt=='--telp':
	          print help_string
	          break

if __name__=='__main__':
    #makeSolutionsFiles('q1')
    main()
