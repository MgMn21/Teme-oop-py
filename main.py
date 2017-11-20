# THIS IS THE MAIN FILE

import collections  # I used the collections.Counter container in order to implement multisets
import functions

multisetA = collections.Counter()
multisetB = collections.Counter()  # We have 2 sets in order to check the operations

check = '1'

while check != '0':
    print("Please chose an option:\n1 - Create multiset A\n2 - Create multiset B\n3 - Check number of elements\n4 - "
          "Check if the multiset is empty\n5 - Check if an element is in the multiset\n6 - Calculate the support\n7 - "
          "Calculate k(e, M)\n8 - Perform set operations\n9 - Display multiset\n0 - Exit\n")
    check = input("#")
    if check == '1':  # We add elements to A
        functions.createset(multisetA)
    if check == '2':  # We add elements to B
        functions.createset(multisetB)
    if check == '3':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We count the elements in A
            functions.nrofelements(multisetA)
        elif temp == 'B' or temp == 'b':  # We count the elements in B
            functions.nrofelements(multisetB)
        else:
            print("Not a valid input")
    if check == '4':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We check if A is empty
            functions.issetempty(multisetA)
        elif temp == 'B' or temp == 'b':  # We check if B is empty
            functions.issetempty(multisetB)
        else:
            print("Not a valid input")
    if check == '5':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We check if a specified element exists in A
            functions.elementexists(multisetA)
        elif temp == 'B' or temp == 'b':  # We check if a specified element exists in B
            functions.elementexists(multisetB)
        else:
            print("Not a valid input")
    if check == '6':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We calculate the support of A
            functions.supp(multisetA)
        elif temp == 'B' or temp == 'b':
            functions.supp(multisetB)  # We calculate the support of B
        else:
            print("Not a valid input")
    if check == '7':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We calculate k(e, A)
            functions.nrofoccurrances(multisetA)
        elif temp == 'B' or temp == 'b':  # We calculate k(e, B)
            functions.nrofoccurrances(multisetB)
        else:
            print("Not a valid input")
    if check == '8':  # We select the operation we want to perform
        temp = input("Which operation would you like to perform:\n1 - Inclusion(A subset of B)\n2 - Union(A | B)\n3 - "
                     "Subtraction(A - B)\n4 - "
                     "Intersection(A & B)\n5 - Comparrison\n# ")
        if temp == '1':  # We check if A is a subset of B
            functions.inclusion(multisetA, multisetB)
        if temp == '2':  # We unite A and B
            functions.union(multisetA, multisetB)
        if temp == '3':  # We subtract B from A
            functions.subtraction(multisetA, multisetB)
        if temp == '4':  # We intersect A and B
            functions.intersection(multisetA, multisetB)
        if temp == '5':  # We compare A and B
            functions.compare(multisetA, multisetB)
    if check == '9':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We output A
            print("A = ")
            functions.outputset(multisetA)
        elif temp == 'B' or temp == 'b':  # We output B
            print("B = ")
            functions.outputset(multisetB)
        else:
            print("Not a valid input")
