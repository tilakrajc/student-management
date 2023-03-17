import re

class Studentbit:
  def __init__(self, sid, sname, marks, fm, fg):
    self.sid  = sid
    self.sname = sname
    self.marks = marks
    self.fm = fm
    self.fg = fg
    self.typ = "BIT"
  def __repr__(self): 
    return f'{self.sid}\t\t{self.sname}\t\t{self.typ}\t\t{round(self.fm,2)}\t\t{self.fg}\n'

class Studentdit:
  def __init__(self, sid, sname, fm, fg):
    self.sid  = sid
    self.sname = sname
    self.fm = fm
    self.fg = fg
    self.typ = "DIT"
  def __repr__(self): 
    return f'{self.sid}\t\t{self.sname}\t\t{self.typ}\t\t {round(self.fm)}\t\t{self.fg}\n'

bitstorage = []
ditstorage = []
storage = []

def stdinputbit():
  
  sid = input("\nEnter student ID:")
  if not re.match("^[A][0-9]{8}$", sid):
    print ("\nError! Invalid student ID!")
    quit()
  
  sname = input("Enter student Name:")
  if not re.match("[A-Za-z]", sname):
    print ("\nError! Only letters a-z allowed for name!")
    quit()
  
  abcnt = 0
  fcnt = 0
  
  marks = [int(x) for x in input("\nEnter student assessment marks (separated by comma):").split(',')]
  for m in marks:
    if m == 0:
      abcnt += 1
    elif m < 50:
      fcnt += 1
    if not re.match("^(?:100(?:[.,]00?)?|\d?\d(?:[.,]\d\d?)?)$", str(m)):
      print ("\nError! Only Numbers allowed for marks!")
      quit()
  
  fm = marks[0]*0.2 + marks[1]*0.4 + marks[2]*0.4
  
  if(abcnt == 0 and fcnt == 1):
    if (marks[0] < 50):
      supp1 = int(input("\nWhat is this student’s supplementary exam mark:"))
      if not re.match("^(?:100(?:[.,]00?)?|\d?\d(?:[.,]\d\d?)?)$", str(supp1)):
        print ("\nError! Only Numbers allowed for marks!")
        quit()
      marks[0] = supp1

    elif (marks[1] < 50):
      supp2 = int(input("\nWhat is this student’s supplementary exam mark:"))
      if not re.match("^(?:100(?:[.,]00?)?|\d?\d(?:[.,]\d\d?)?)$", str(supp2)):
        print ("\nError! Only Numbers allowed for marks!")
        quit()
      marks[1] = supp2
      
    elif (marks[2] < 50):
      supp3 = int(input("\nWhat is this student’s supplementary exam mark:"))
      if not re.match("^(?:100(?:[.,]00?)?|\d?\d(?:[.,]\d\d?)?)$", str(supp3)):
        print ("\nError! Only Numbers allowed for marks!")
        quit()
      marks[2] = supp3
    supp = marks[0]*0.2 + marks[1]*0.4 + marks[2]*0.4

    if supp >= 50:
      fg = 'SP'
    else:
      fg ='F'
  elif(fcnt == 0 and abcnt == 0 and fm<=100 and fm>=85):
    fg = 'HD'
  elif(fcnt == 0 and abcnt == 0 and fm<=84 and fm>=75):
    fg = 'D'
  elif(fcnt == 0 and abcnt == 0 and fm<=74 and fm>=65):
    fg = 'C'
  elif(fcnt == 0 and abcnt == 0 and fm<=64 and fm>=50):
    fg = 'P'
  
      
  else:
    fg = 'AF'
  s = Studentbit(sid, sname ,marks, fm, fg)
  bitstorage.append(s)
  storage.append(s)

ditstorage = []
def stdinputdit():
  sid = input("\nEnter student ID:")
  if not re.match("^[A][0-9]{8}$", sid):      
    print ("\nError! Invalid student ID!")
    quit()
  
  sname = input("\nEnter student Name:")
  if not re.match("[A-Za-z]", sname):
    print ("\nError! Only letters a-z allowed for name!")
    quit()
  
  fm = int(input("\nEnter student assessment marks:"))
  if fm >= 50 and fm <= 100:
    fg = 'CP'

  elif fm >= 0 and fm <= 49:
    fm = int(input("\nWhat is this student’s supplementary exam mark:"))

    if fm >= 50 and fm <= 100:
      fg = 'CP'
    elif fm >= 0 and fm <= 49:
      fg = 'F'
    else:
      print("\nINVALID INPUT!")
      quit()
      
  else:
    print("\nINVALID INPUT!")
    quit()
  
  s = Studentdit(sid, sname, fm, fg)
  ditstorage.append(s)
  storage.append(s)

def printinfo():
  for person in storage:
    print(person)

def printstats():
  totalStudents = len(storage)
  studentsPassed = len([x for x in storage if x.fg=="HD" or x.fg == "D" or x.fg=="C" or x.fg =="P" or x.fg == "SP" or x.fg=="CP"])
  totalStudentsAdjusted = totalStudents - len([x for x in storage if x.fg=="AF"])
  bitl = len(bitstorage)
  a1 = 0
  a2 = 0
  a3 = 0
  af = 0
  for x in bitstorage:
    a1 += x.marks[0]
    a2 += x.marks[1]
    a3 += x.marks[2]
    af += x.fm
  if totalStudents == 0:
    print("\nThere is no data!")
    mainmenu()
  else:
    print("Total number of students " + str(totalStudents))
    print("Number of DIT students " + str(len(ditstorage)))
    print("Number of BIT students " + str(len(bitstorage)))
    print("Students pass rate " + str(round(studentsPassed/totalStudents, 2)))
    print("Students pass rate(adjusted) " + str(round(studentsPassed/totalStudentsAdjusted, 2)))
    print("Average Marks for Assessment 1 " + str(round(a1/bitl,2)))
    print("Average Marks for Assessment 2 " + str(round(a2/bitl,2)))
    print("Average Marks for Assessment 3 " + str(round(a3/bitl,2)))
    print("Average Final Marks " + str(round(af/totalStudents,2)))
    print("Number of HDs " +  str(len([x for x in storage if x.fg=="HD"])))
    print("Number of Ds " +  str(len([x for x in storage if x.fg=="D"])))
    print("Number of Cs " +  str(len([x for x in storage if x.fg=="C"])))
    print("Number of Ps " +  str(len([x for x in storage if x.fg=="P"])))
    print("Number of SPs " +  str(len([x for x in storage if x.fg=="SP"])))
    print("Number of CPs " +  str(len([x for x in storage if x.fg=="CP"])))
    print("Number of Fs " +  str(len([x for x in storage if x.fg=="F"])))

  mainmenu()

def mainmenu():
  
  cmd = input("\n>>> Choose one of the following options:\n>>> 1 - Enter student grade information \n>>> 2 - Print all student grade information \n>>> 3 - Print class performance statistics \n>>> 4 - Exit\n")
  
  if cmd == '1':
    menu1() 

  elif cmd == '2':
    menu2()

  elif cmd == '3':
    printstats()
  
  elif cmd == '4':
    quit()
  
  else:
    print("\nINVALID INPUT!")

def menu1():
  cmd = input("\n>>> Choose one of the following options:\n>>> 1.1 - Enter a BIT student information\n>>> 1.2 - Enter a DIT student information\n>>> 1.3 - Go back to the main menu\n")
    
  if cmd == '1.1':
    stdinputbit()
    mainmenu()

  elif cmd == '1.2':
    stdinputdit()
    mainmenu()

  elif cmd == '1.3':
    mainmenu()
    
  else:
    print("\nINVALID INPUT!")
    quit()

def menu2():
  cmd = input("\n>>> Choose one of the following options:\n>>> 2.1 – Print all student grade information ascendingly by final mark\n>>> 2.2 – Print all student grade information descendingly by final mark\n>>> 2.3 – Go back to the main menu\n")
    
  if cmd == '2.1':
    storage.sort(key=lambda x: x.fm, reverse=True)
    printinfo()
    mainmenu()

  elif cmd == '2.2':
    storage.sort(key=lambda x: x.fm, reverse=False)
    printinfo()
    mainmenu()

  elif cmd == '2.3':
    mainmenu()
    
  else:
    print("\nINVALID INPUT!")
    quit()

mainmenu()