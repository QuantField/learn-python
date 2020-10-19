valtests = [0, 1, '', ' ', True, 'str', 23, -1, None]
print("exprssion in [0, 1, '', ' ', True, 'str', 23, -1, None]")
print()

print("Statement : if expression:")
print("--------------------------")
for exp in valtests:
  if exp:
    print(exp, 'Resolves to True')
  else:
    print(exp, 'Resolves to False')

print()
print("Statement : if expression == True:")
print("--------------------------")
for exp in valtests:
  if exp == True:
    print(exp, 'Resolves to True')
  else:
    print(exp, 'Resolves to False')

print()
print("Statement : if expression is True:")
print("--------------------------")
for exp in valtests:
  if exp is True:
    print(exp, 'Resolves to True')
  else:
    print(exp, 'Resolves to False')

========================================
exprssion in [0, 1, '', ' ', True, 'str', 23, -1, None]

Statement : if expression:
--------------------------
0 Resolves to False
1 Resolves to True
 Resolves to False
  Resolves to True
True Resolves to True
str Resolves to True
23 Resolves to True
-1 Resolves to True
None Resolves to False

Statement : if expression == True:
--------------------------
0 Resolves to False
1 Resolves to True
 Resolves to False
  Resolves to False
True Resolves to True
str Resolves to False
23 Resolves to False
-1 Resolves to False
None Resolves to False

Statement : if expression is True:
--------------------------
0 Resolves to False
1 Resolves to False
 Resolves to False
  Resolves to False
True Resolves to True
str Resolves to False
23 Resolves to False
-1 Resolves to False
None Resolves to False
