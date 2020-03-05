#ANDREAS MATSIAS 3025 cse53025
#============================#
import sys
import json
import copy

array = ['and_tk', 'declare_tk', 'dowhile_tk', 'else_tk', 
         'endfunction_tk', 'exit_tk', 'forcase_tk',
         'function_tk', 'print_tk', 'then_tk',
         'if_tk', 'in_tk', 'inout_tk', 'not_tk', 'endif_tk',
          'program_tk', 'or_tk', 'return_tk', 'while_tk',
         'default_tk','endprogram_tk','inandout_tk','endwhile_tk',
         'loop_tk','endloop_tk','endforcase_tk','enddefault_tk',
         'when_tk','incase_tk','endincase_tk','input_tk','enddowhile_tk']

white_tk = 55  # Leukos
error_tk = -1  # error
id_tk = 32  # metablhth
digit_tk = 33  # pshfio
plus_tk = 34  # +
minus_tk = 35  # -
multi_tk = 36  # *
division_tk = 37  # /
equal_tk = 38  # =
smaller_tk = 39  # <
different_tk = 40  # <>
smallequal_tk = 41  # <=
greater_tk = 42  # >
greatequal_tk = 43  # >=
assign_tk = 44  # :=
x = 45  # :
opcomment_tk = 46  # open comment \*
clcomment_tk = 47  # close comment *\
comma_tk = 48  # ,
semicolon_tk = 49  # ;
opbrac1_tk = 50  # (
clbrac1_tk = 51  # )
opbrac2_tk = 52  # [
clbrac2_tk = 53  # ]
eof_tk = 54  # eof_tk
#Reserved words
and_tk = 0
declare_tk = 1
dowhile_tk = 2
else_tk = 3
endfunction_tk = 4
exit_tk = 5
forcase_tk = 6
function_tk = 7
print_tk = 8
then_tk = 9
if_tk = 10
in_tk = 11
inout_tk = 12
not_tk = 13
endif_tk = 14
program_tk = 15
or_tk = 16
return_tk = 17
while_tk = 18
default_tk = 19
endprogram_tk=20
inandout_tk=21
endwhile_tk=22
loop_tk=23
endloop_tk=24
endforcase_tk=25
enddefault_tk=26
when_tk=27
incase_tk=28
endincase_tk=29
input_tk=30
enddowhile_tk=31
#___________________________________________________________________

class lex_output():
    token = 0
    lektikh_monada = ""
#___________________________________________________________________
return_of_lex=lex_output()
line=1
file_to_compile=open(sys.argv[1], "r+")
#___________________________________________________________________
scope_list=[]
entity_list=[]
argument_list=[]
start_quad=[]
offset=12
entity_count=0
tmp_arr=[]
quad_line=0
count_temp=0
new_tmp = []
types=0
typer=0
strr=''
trueList = []
falseList = []
temp = 0
p = 0
i = 0
qwe = 0
kj = 0
offset_list = []
real_offset = []
frame_length = []
listr = []
quad_array = []
function_name = []
function_name1 = []
dlist=[]
hlist=[]
glist=[]
#==================================================================
ti = 0
si = 0
kkk=0
vi=0
ai=0
jjj=0
parCounter = 0
frCounter = 0
mips = open("test.asm", "w+")
#==================================================================
class Scope():
    entity = [] 
    en_scope = 1
    nest_level = 0  
      
    def create_scope(ggg):
        scope = Scope()
        return scope

class Entity(object):
    name = ""
    entity_type = -1
    n_entity = 1


    def __init__(ggg, name1, type1, n_entity1):
        ggg.name = name1
        ggg.entity_type = type1
        ggg.n_entity = n_entity1

    def create_entity(name1, type1, n_entity1):
        entity = Entity(name1, type1, n_entity1)
        return entity
    
class Argument(object):
    parm = -1  # 1 cv,2 ref,3 copy
    argType = 0  # typos metablhths (int :0)
    nextArg = 1  # deikths

    def __init__(ggg, parm1, type1, next1):
        ggg.parm = parm1
        ggg.argType = type1
        ggg.nextArg = next1

    def create_argument(parm1, type1, next1):
        argument = Argument(parm1, type1, next1)
        return argument

def addScope():
    global entity_count, offset
    if len(scope_list) != 0:
        listr.append(entity_count)
        offset_list.append(offset)
        frame_length.append(offset + 4)
    scope = Scope.create_scope("")
    scope_list.append(scope)
    entity_count = 0
    offset = 12

def delScope():
    global entity_count, qwe, offset
    qwe += 1
    if qwe == 1:
        listr.append(entity_count)
        offset_list.append(offset)
        frame_length.append(offset + 4)
        real_offset.append(offset)
    for i in range(0, listr[len(listr) - 1]):
        entity_list.pop()
    listr.pop()
    scope_list.pop()
    offset_list.pop()
    offset = offset_list[len(offset_list) - 1]
    real_offset.append(offset)

def addEntity(name1, type1, n_entity1):
    global entity_count
    entity_count =entity_count+1
    ent = Entity.create_entity(name1, type1, n_entity1)
    entity_list.append(ent)
    scope_list[len(scope_list)-1].entity.append(ent)

def addArgument(parm1, type1, next1):
    ar = Argument.create_argument(parm1, type1, next1)
    argument_list.append(ar)

def searchEntity(name1):
    for scope1 in scope_list:
        for i in range(0, len(scope1.entity) - 1):
            if scope1.entity[i].name == name1:
                print("-----------------------------------------")
                print("Entity", scope1.entity[i].name, "found!!!")
                print("-----------------------------------------")
                return scope1.entity[i]
    print("-----------------------------------------")
    print("Entity Not Found!")
    print("-----------------------------------------")
#___________________________________________________________________


####################################################################
####HELPFULL SUBROUTINES############################################
def nextquad():
    nextQ = len(quad_array)
    return nextQ

def genquad(op, x, y, z):
    global quad_line
    quad_array.append([])
    quad_array[quad_line].append(op)
    quad_array[quad_line].append(x)
    quad_array[quad_line].append(y)
    quad_array[quad_line].append(z)
    quad_line =quad_line+1

def newtemp():
    global count_temp, offset
    count_temp += 1
    new_tmp.append('T_' + str(count_temp))
    addEntity(new_tmp[temp], 4, len(entity_list) + 1)
    offset = offset + 4

def emptylist():
    trueList = []
    falseList = []

def makelist(l):
    trueList.append(l - 1)
    falseList.append(l)

def merge(list1, list2):
    merged_list = list1 + list2
    return merged_list

def backpatch(list, z, ff):
    if ff==1:  # true_list
        t=len(list) - 1
        if t>-1:
            while (list[t]!='abc'):
                quad_array[list[t]][3] = z
                t=t-1
                if t<0:
                    break
            del trueList[t:len(trueList)]
    else:#false_list
        t=len(list)-1
        if t>-1:
            while (list[t] != 'abc'):
                quad_array[list[t]][3] = z
                t=t-1
                if t<0:
                    break
            del falseList[t:len(falseList)]

def plus_creator(array):
    global i, temp
    variable = array[0]
    del array[0:2]
    newtemp()
    genquad(array[1], array[0], array[2], new_tmp[temp])
    i += 1
    temp += 1
    del array[0:2]
    while len(array)!=1:
        newtemp()
        genquad(array[1], array[2], new_tmp[temp - 1], new_tmp[temp])#ERROR
        del array[0:2]
        i=i+1
        temp += 1
    genquad(":=", new_tmp[temp - 1], "_",variable )
    return array

def muliply_creator(array):
    variable = array[0]
    del array[0:2]
    global p, temp
    p = 0
    for t in array:
        if array[p] is '*' or array[p] is '/':
            newtemp()
            genquad(array[p], array[p - 1], array[p + 1], new_tmp[temp])
            array[p] = new_tmp[temp]
            temp += 1
            array.pop(p - 1)
            array.pop(p)
        p += 1
    array.insert(0, ":=")
    array.insert(0, variable)
    plus_creator(array)
    return array

def calculator(array):
    if len(array) == 3:
        genquad(array[1], array[2], '_', array[0])
    if len(array) == 4:#
        genquad(array[1], array[2] , '_', array[0])
    if len(array) == 5:
        genquad(array[3], array[2], array[4], array[0])
    if len(array) == 6:#1
        genquad(array[3], array[2] , array[4], array[0])
    if len(array) > 6:
        for l in array:
            if l is "*" or l is "/":
                global types
                types = 1
        if types == 0:
            plus_creator(array)
        elif types == 1:
            muliply_creator(array)

def calculator_of_condition(array):
    global kj
    kj = 0
    array1 = []
    array2 = []
    array3 = copy.deepcopy(array)
    if array3[len(array3) - 1] == ")":
        kj = 1
        array3.pop()
    r = 0
    tmp1 = ''
    tmp2 = ''
    global temp
    while array[r] is not '<' and array[r] is not '>' and array[r] is not '=':
        array1.append(array[r])
        r += 1
    for i in range(r + 1, len(array)):
        array2.append(array[i])
    if array2[0] is '=' or array2[0] is '>':
        array2.pop(0)
    if array2[len(array2) - 1] is ')':
        array2.pop()
    array1.insert(0, ':=')
    newtemp()
    tmp1 = new_tmp[temp]
    array1.insert(0, tmp1)
    temp += 1
    array2.insert(0, ':=')
    newtemp()
    tmp2 = new_tmp[temp]
    array2.insert(0, tmp2)
    temp += 1
    calculator(array1)
    calculator(array2)
    genquad(strr, tmp1, tmp2, '_')

def parenthesis(array):
    global temp
    point = 0
    point1 = 0
    parray = []
    for j in range(0, len(array)):
        if array[j] is '(':
            for h in range(j + 1, len(array)):
                if array[h] != ';' and array[h] != ')':
                    parray.append(array[h])
                else:
                    break
            break
    if len(parray) == 0:
        return
    newtemp()
    nt = new_tmp[temp]
    parray.insert(0, ':=')
    parray.insert(0, nt)
    calculator(parray)
    for r in range(0, len(tmp_arr)):
        if tmp_arr[r] is '(':
            point = r
            break
    for r1 in range(0, len(tmp_arr)):
        if tmp_arr[r1] is ')':
            point1 = r1
            break
    del tmp_arr[point:point1]
    tmp_arr[point] = nt
    parray.clear()
    temp=temp+1
    if tmp_arr[len(tmp_arr) - 1] is ';' or tmp_arr[len(tmp_arr) - 1] is ")":
        tmp_arr.pop()

def int_creator():
    r = open("test.int", "w+")
    i = 0
    r.write("==============================\n")
    r.write("#ANDREAS MATSIAS 3025 cse53025\n")
    r.write("==============================\n")
    for i in range(0, len(quad_array)):
        r.write('L' + str(i) + ': ')
        json.dump(quad_array[i], r)
        r.write('\n')
    r.close()

def c_file_creator():
    global dlist
    i = 1
    b = []
    par = []
    u = open("test.c", "w+")
    k = len(quad_array)
    u.write("//ANDREAS MATSIAS 3025 cse53025\n")
    u.write("int main()\n")
    u.write("{\n")
    u.write("                                                                                                  ")
    u.write("\n")
    u.write("  ")
    u.write("L_0:\n")
    def writer(line, str1):
        y = line[3]
        z = line[2]
        a = line[1]
        e = line[0]
        if str1 is "+" or str1 is "-" or str1 is "*" or str1 is "/":
            u.write(str(y))
            u.write("=")
            u.write(z)
            u.write(str1)
            u.write(a)
            u.write(";")
            u.write(" ")
            u.write("//(")
        elif str1 == "=" or str1 == ">" or str1 == "<" or str1 == "<>" or str1 == ">=" or str1 == "<=":
            u.write("if (")
            u.write(a)
            if str1 == "=":
                u.write(str1)
                u.write(str1)
                u.write(str(z))
                u.write(")")
                u.write(" goto ")
                u.write("L_")
                u.write(str(y))
                u.write(";")
                u.write(" ")
                u.write("//(")
            else:
                u.write(str1)
                u.write(str(z))
                u.write(")")
                u.write(" goto ")
                u.write("L_")
                u.write(str(y))
                u.write(";")
                u.write(" ")
                u.write("//(")
        elif str1 == ":=":
            u.write(str(y))
            u.write("=")
            u.write(str(a))
            u.write(";")
            u.write(" ")
            u.write("//(")
            b.append(str(y))
            [b.remove(elem) for elem in b if elem  in dlist]
        elif str1 == "jump":
            u.write("goto ")
            u.write("L_")
            u.write(str(y))
            u.write(";")
            u.write(" ")
            u.write("//(")
        elif str1 == "Print":
            u.write("print(")
            u.write(str(a))
            u.write(")")
            u.write(";")
            u.write(" ")
            u.write("//(")
        elif str1 == "retV":
            u.write("return(")
            u.write(str(a))
            u.write(")")
            u.write(";")
            u.write(" ")
            u.write("//(")
        elif str1 == "Input":
            u.write("input(")
            u.write(str(a))
            u.write(")")
            u.write(";")
            u.write(" ")
            u.write("//(")
        elif str1 == "Exit":
            u.write("exit()")
            u.write("//(")
        elif str1 == "par":
            par.append(str(a))
        elif str1 == "halt":
            u.write("break")
            u.write(";")
            u.write(" ")
            u.write("//(")         
    while (i < k - 1):
        u.write("  ")
        u.write("L_")
        p = (i).__str__()
        u.write(p)
        u.write(":")
        u.write(" ")
        writer(quad_array[i], quad_array[i][0])
        u.write(str(quad_array[i]))
        u.write(")")
        u.write("\n")
        i += 1
    mylist = []
    [mylist.append(elem) for elem in b if elem not in mylist]
    u.write("  ")
    u.write("L_")
    p = ((k - 1) ).__str__()
    u.write(p)
    u.write(":")
    u.write(" ")
    u.write("{}\n")
    u.write("}\n")
    u.seek(47, 0)
    u.write("int ")
    u.write(dlist[0])
    i = 1
    while (i < len(dlist)):
        u.write(", ")
        u.write(dlist[i])
        i += 1
    u.write(",")
    u.write(mylist[0])
    while (i < len(mylist)):
        u.write(", ")
        u.write(mylist[i])
        i += 1
    u.write(";")
    u.close()
###################################################################
def lex():
    xx = file_to_compile.read(1)
    
    while (xx == ' ' or xx == "\n" or xx == "\t"):
        if xx is "\n":
            global line
            line += 1
        xx = file_to_compile.read(1)
    while True:
        m = xx
        if xx.isalpha():
            return_of_lex.token = id_tk
            xx = file_to_compile.read(1)
            while xx.isalpha() or xx.isnumeric():
                m += xx
                xx = file_to_compile.read(1)
            file_to_compile.seek(file_to_compile.tell() - 1)
            pl = m
            m += "_tk"
            return_of_lex.lektikh_monada = m
            if return_of_lex.lektikh_monada in array:
                return_of_lex.token = array.index(return_of_lex.lektikh_monada)
            else:
                return_of_lex.lektikh_monada = pl
        elif xx.isnumeric():
            while xx.isnumeric():
                return_of_lex.token = digit_tk
                xx = file_to_compile.read(1)
                if xx.isnumeric():
                    m += xx
                else:
                    if xx.isalpha():
                        return_of_lex.token = error_tk
                        print('===================================================')
                        print("ERROR: not accepted this types of number at line: ", line)
                        print('===================================================')
                        exit()
            file_to_compile.seek(file_to_compile.tell() - 1)
            return_of_lex.lektikh_monada = m
            if int(m) > 32767:
                print('====================================================================')
                print("ERROR: Invalid  number.Number not bigger that 32767 error at line: ", line)
                print('====================================================================')
                exit()
        
        elif xx is '+':
            return_of_lex.token = plus_tk
            return_of_lex.lektikh_monada = m
        elif xx is '-':
            return_of_lex.token = minus_tk
            return_of_lex.lektikh_monada = m
        elif xx is '*':
            return_of_lex.token = multi_tk
            return_of_lex.lektikh_monada = m
        elif xx is '/':
            xx = file_to_compile.read(1)
            if xx is '*':
                while (1):
                    xx = file_to_compile.read(1)
                    if not xx:
                        print('=============================')
                        print("ERROR: Comments did not close")
                        print('=============================')
                        return_of_lex.lektikh_monada = "ERROR"
                        return_of_lex.token = error_tk
                        return return_of_lex
                        exit()

                    if xx is '*':
                        xx = file_to_compile.read(1)
                        if xx is '/':
                            return lex()
                    elif xx is '\n':
                        line += 1
            elif xx is '/':
                while(xx is not '\n'):
                    xx=file_to_compile.read(1)
                line+=1
                return lex()                        
            elif xx is not '/':
                xx= file_to_compile.seek(file_to_compile.tell() - 1)
                return_of_lex.token = division_tk
                return_of_lex.lektikh_monada = m
            else:
                print('=========================================')
                print("ERROR: expected '*' after / or a second /")
                print('=========================================')
                return_of_lex.token = error_tk
                return_of_lex.lektikh_monada = "ERROR"
                return return_of_lex
        elif xx is '[':
            return_of_lex.token = opbrac2_tk
            return_of_lex.lektikh_monada = m
        elif xx is ']':
            return_of_lex.token = clbrac2_tk
            return_of_lex.lektikh_monada = m
        elif xx is '(':
            return_of_lex.token = opbrac1_tk
            return_of_lex.lektikh_monada = m
        elif xx is ')':
            return_of_lex.token = clbrac1_tk
            return_of_lex.lektikh_monada = m
        elif xx is '<':
            xx = file_to_compile.read(1)
            if xx is '=':
                return_of_lex.token = smallequal_tk
                return_of_lex.lektikh_monada = '<='
            elif xx is '>':
                return_of_lex.token = different_tk
                return_of_lex.lektikh_monada = '<>'
            else:
                return_of_lex.token = smaller_tk
                return_of_lex.lektikh_monada = m
                file_to_compile.seek(file_to_compile.tell() - 1)
        
        elif xx is '>':
            xx = file_to_compile.read(1)
            if xx is '=':
                return_of_lex.token = greatequal_tk
                return_of_lex.lektikh_monada = '>='
            else:
                return_of_lex.token = greater_tk
                return_of_lex.lektikh_monada = m
                file_to_compile.seek(file_to_compile.tell() - 1)
        elif xx is '=':
            return_of_lex.token = equal_tk
            return_of_lex.lektikh_monada = m
        elif xx is ',':
            return_of_lex.token = comma_tk
            return_of_lex.lektikh_monada = m
        elif xx is ';':
            return_of_lex.token = semicolon_tk
            return_of_lex.lektikh_monada = m
        elif xx is ':':
            xx = file_to_compile.read(1)
            if xx is '=':
                return_of_lex.token = assign_tk
                return_of_lex.lektikh_monada = ':='
            else:
                return_of_lex.token = x
                return_of_lex.lektikh_monada = ":"
                file_to_compile.seek(file_to_compile.tell() - 1)  # ( : )
        elif xx.isprintable() and xx is '':
            return_of_lex.token = eof_tk  
        else:
            return_of_lex.token = error_tk
            return_of_lex.lektikh_monada = "Invalid character!!: ", line
            sys.exit()
        #print(return_of_lex.lektikh_monada, "==", return_of_lex.token) 
        #print("line :",line)     
        #print("==============================")                  
        return (return_of_lex)
#===================================================================
def syntax(k):
    addScope()
    def program(k):
        global program_name,offset
        if k.token == program_tk:
            k = lex()
            program_name = k.lektikh_monada
            if k.token == id_tk:
                k = lex()
                y=block(k)
                if len(real_offset) == 0:
                    real_offset.append(offset)
                    offset_list.append(offset)
                    frame_length.append(offset + 4)
                if y.token==endprogram_tk:
                    print('|----------------------------|')
                    print("|Compile was successfull!!!!!|")
                    print('|----------------------------|')
                else :
                    print('-----------------------------------------------------')
                    print("ERROR: The keyword 'endprogram' was expected at line: ", line)
                    print('-----------------------------------------------------')
                    exit()
            else:
                print('-------------------------------------------')
                print("ERROR: Program name was expected at line: ", line)
                print('-------------------------------------------')
                exit()
        else:
            print('---------------------------------------------------')
            print("ERROR: The keyword 'program' was expected at line: ", line)
            print('---------------------------------------------------')
            exit()
        genquad('halt', '_', '_', '_')
        genquad('end_block', program_name, '_', '_')   
    # --------------------------------------------------------------------
    def block(k): 
        global program_name,function_name,function_name1
        y = declarations(k)
        z = subprograms(y)
        if len(function_name1)==0:
            genquad('begin_block', program_name, '_', '_')
        u = statements(z)
        return u
    # --------------------------------------------------------------------
    def declarations(k):      
        global dlist,entity_count,offset
        if k.token == declare_tk:
            k = lex()
            if k.token == id_tk:
                dlist.append(k.lektikh_monada)
                addEntity(k.lektikh_monada, 1, len(entity_list) + 1)
                offset =offset+ 4
                k = lex()
                y = varlist(k) 
                if y.token==semicolon_tk:
                    k=lex()
                else:
                    print('----------------------------------')
                    print("ERROR: ';' was expected at line: ", line)
                    print('----------------------------------')
                    exit()
                return k
            else:
                print('-----------------------------------------------')
                print("ERROR: Variable name was expected at line: ", line)
                print('-----------------------------------------------')
                exit()
        return k
    # ----------------------------------------------------------------------
    def varlist(k):
        global dlist,offset
        while (k.token == comma_tk):
            k = lex()
            if k.token == id_tk:
                dlist.append(k.lektikh_monada)
                addEntity(k.lektikh_monada, 1, len(entity_list) + 1)
                offset=offset+4
                k = lex()
            else:
                print('-------------------------------------------------')
                print("ERROR: Variable name was expected at line: ", line)
                print('-------------------------------------------------')
                exit()
        return k
    # ---------------------------------------------------------------------
    def subprograms(k):
        while (k.token == function_tk):
            k=lex()
            y = subprogram(k)
            return y
        return k
    # --------------------------------------------------------------------
    def subprogram(k): 
        global function_name,function_name1,program_name,kkk
        if k.token == id_tk:
            function_name.append(k.lektikh_monada)
            function_name1.append(k.lektikh_monada)
            addScope()
            addEntity(k.lektikh_monada, 2, len(entity_list) + 1)
            start_quad.append(quad_line)
            genquad('begin_block', function_name[len(function_name) - 1], '_', '_')
            kkk=kkk+1
            k = lex()
            y = funcbody(k)
            if y.token==endfunction_tk:
                delScope()
                k=lex()
                genquad('end_block', function_name[len(function_name) - 1], '_', '_')
                function_name.pop()
                if k.token!=function_tk:
                    subprograms(k)
                if k.token==function_tk:
                    subprograms(k)
                if k.token==endfunction_tk:
                    k=lex()
                if len(function_name)==0:
                    genquad('begin_block',program_name, '_', '_') 
            else:
                print('----------------------------------------------')
                print("ERROR: 'endfunction' was expected at line: ", line)
                print('----------------------------------------------')
                exit()
        else:
            print('------------------------------------------')
            print("ERROR: Function name expected at line : ", line)
            print('------------------------------------------')
            exit()
        return k
    # ------------------------------------------------------------------------
    def funcbody(k):
        y = formalpars(k)
        z = block(y)
        return z
    # ------------------------------------------------------------------------
    def formalpars(k):
        if k.token == opbrac1_tk:
            k = lex()
            y = formalparlist(k)
            if y.token == clbrac1_tk:
                k = lex()
            else:
                print('----------------------------------------------------------------')
                print("ERROR: Parentheses is open. Right parenthesis expected at line: ", line)
                print('----------------------------------------------------------------')
                exit()
        else:
            print('---------------------------------------------------------------------')
            print("ERROR: Parentheses did not open. Left parenthesis expected at line: ", line)
            print('---------------------------------------------------------------------')
            exit()
        return k
    # ------------------------------------------------------------------------
    def formalparlist(k):
        if k.token == in_tk or k.token == inout_tk or k.token==inandout_tk:
            y = formalparitem(k)
            while (y.token == comma_tk):
                k = lex()
                y = formalparitem(k)
            return y
        elif k.token != in_tk or k.token != inout_tk or k.token!=inandout_tk:
            print('------------------------------------------------------------------------------------------')
            print("ERROR: The keyword 'in' or the keyword 'inout' or the keyword 'inandout' expected at line: ", line)
            print('-------------------------------------------------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def formalparitem(k): 
        global offset      
        if k.token == in_tk:
            k = lex()
            addEntity(k.lektikh_monada, 3, len(entity_list) + 1)
            addArgument(1, 0, len(argument_list) + 1)
            offset=offset+4
            if k.token == id_tk:
                k = lex()
            else:
                print('------------------------------------')
                print("ERROR: In name was expected at line: ", line)
                print('------------------------------------')
                exit()
        elif k.token == inout_tk:
            k = lex()  
            addEntity(k.lektikh_monada, 3, len(entity_list) + 1)    
            addArgument(2, 0, len(argument_list) + 1) 
            offset=offset+4    
            if k.token == id_tk:
                k = lex()
            else:
                print('--------------------------------------')
                print("ERROR: Inout name was expected at line: ", line)
                print('--------------------------------------')
                exit()
        elif k.token == inandout_tk:
            k = lex()         
            addEntity(k.lektikh_monada, 3, len(entity_list) + 1)
            addArgument(3, 0, len(argument_list) + 1)
            offset=offset+4   
            if k.token == id_tk:
                k = lex()
            else:
                print('------------------------------------------')
                print("ERROR: Inandout name expected at line: ", line)
                print('------------------------------------------')
                exit()
        else:
            print('----------------------------------------------------------------------------------------')
            print("ERROR: The keyword 'in' or the keyword 'inout' or the keyword 'inandout' expected at line: ", line)
            print('----------------------------------------------------------------------------------------')
            exit()
        return k
    # -------------------------------------------------------------------------
    def statements(k):
        f = 0
        y = statement(k)
        if len(tmp_arr) != 0:
            for n in tmp_arr:
                if n is '(':
                    f=f+1
            for na in range(0, f):
                parenthesis(tmp_arr)
        calculator(tmp_arr)
        tmp_arr.clear()
        while (y.token == semicolon_tk or y.token == id_tk):
            if y.token == semicolon_tk:
                k = lex()
                y = statement(k)
            else:
                y = statement(y)  
            calculator(tmp_arr) 
            tmp_arr.clear()
        return y
    # ----------------------------------------------------------------------
    def statement(k):
        if k.token == id_tk:
            tmp_arr.append(k.lektikh_monada)
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            y = assignment_stat(k)
            return y
        elif k.token == if_tk:
            k = lex()
            y = if_stat(k)
            return y
        elif k.token == while_tk:
            k = lex()
            y = while_stat(k)
            return y
        elif k.token == dowhile_tk:
            k = lex()
            y = do_while_stat(k)
            return y
        elif k.token == loop_tk:
            k = lex()
            y = loop_stat(k)
            return y
        elif k.token == exit_tk:
            y = exit_stat()
            return y
        elif k.token == forcase_tk:
            k = lex()
            y = forcase_stat(k)
            return y
        elif k.token == incase_tk:
            k = lex()
            y = incase_stat(k)
            return y
        elif k.token == return_tk:
            k = lex()
            y = return_stat(k)
            return y
        elif k.token == input_tk:
            k = lex()
            y = input_stat(k)
            return y
        elif k.token == print_tk:
            k = lex()
            y = print_stat(k)
            return y
        return k
    # --------------------------------------------------------------------------
    def assignment_stat(k):
        global function_name1
        if k.token == assign_tk:
            k = lex()
            if k.lektikh_monada in function_name1:
                hlist.append(k.lektikh_monada)
            tmp_arr.append(k.lektikh_monada)
            y = expression(k)
            if k.token==function_tk:#
                subprograms(k)
        else:
            print('-----------------------------------------------------')
            print("ERROR: Assignment operator was expected at line: ", line)
            print('-----------------------------------------------------')
            exit()
        return y
    # ------------------------------------------------------------------------
    def if_stat(k):
        if k.token == opbrac1_tk:
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            trueList.append('abc')
            falseList.append('abc')
            y = condition(k)
            tmp_arr.clear()
            makelist(quad_line)
            if y.token == clbrac1_tk:
                genquad('jump', '_', '_', '_')
                backpatch(trueList, nextquad(), 1)
                k = lex()
                if k.token==then_tk:
                    k = lex()
                    y = statements(k)
                    t = elsepart(y)
                    backpatch(falseList, nextquad(), 0)
                    if t.token==endif_tk:
                        k=lex()
                        return k
                    else:
                        print('-----------------------------------------')
                        print("ERROR: 'endif' was expected at line: ", line)
                        print('-----------------------------------------')
                        exit()
                else:
                    print('---------------------------------------')
                    print("ERROR: 'then' was expected at line: ", line)
                    print('---------------------------------------')
                    exit()
            else:
                print('-----------------------------------------------------------------')
                print("ERROR: Parentheses is open. Right parenthesis expected at line: ", line)
                print('-----------------------------------------------------------------')
                exit()
        else:
            print('--------------------------------------------------------------------')
            print("ERROR: Parentheses did not open. Left parenthesis expected at line: ", line)
            print('--------------------------------------------------------------------')
            exit()
        return k
    # ------------------------------------------------------------------------
    def elsepart(k):
        if k.token == else_tk:
            falseList.append(quad_line)
            genquad('jump', '_', '_', '_')
            k = lex()
            y = statements(k)
            backpatch(falseList, nextquad(), 0)
            return y
        return k
    # -------------------------------------------------------------------------
    def while_stat(k):
        if k.token == opbrac1_tk:
            rt=quad_line-1
            whilel = rt+10
            k = lex()
            trueList.append('abc')
            falseList.append('abc')
            tmp_arr.append(k.lektikh_monada)
            y = condition(k)
            tmp_arr.clear()
            makelist(quad_line)
            if k.token == clbrac1_tk:
                genquad('jump', '_', '_', '_')
                backpatch(trueList, nextquad() , 1)
                k = lex()
                y = statements(k)
                genquad('jump', '_', '_', whilel)
                backpatch(falseList, nextquad() , 0)
                if y.token==endwhile_tk:
                    k=lex()
                    return k
                else:
                    print('------------------------------------------')
                    print("ERROR: 'endwhile' was expected at line: ", line)
                    print('------------------------------------------')
                    exit()
            else:
                print('----------------------------------------------------------------')
                print("ERROR: Parentheses is open. Right parenthesis expected at line: ", line)
                print('-----------------------------------------------------------------')
                exit()
        else:
            print('------------------------------------------------------------------')
            print("ERROR: Parentheses did not open. Left parenthesis expected at line: ", line)
            print('------------------------------------------------------------------')
            exit()
    # --------------------------------------------------------------------------
    def loop_stat(k):
        u=quad_line
        y=statements(k)
        if y.token==endloop_tk:
            genquad('jump', '_', '', u)
            k=lex()
            return k
        else:
            print('------------------------------------------')
            print("ERROR: 'endloop' was expected at line: ", line)
            print('------------------------------------------')
            exit()
    # --------------------------------------------------------------------------
    def do_while_stat(k):
        dowhilel = (quad_line - 1)+ 10
        y = statements(k)
        if y.token == enddowhile_tk:
            k = lex()
            if k.token == opbrac1_tk:
                k = lex()
                trueList.append('abc')
                falseList.append('abc')
                tmp_arr.append(k.charlex)
                y = condition(k)
                tmp_arr.clear()
                makelist(quad_line)
                if y.token == clbrac1_tk:   
                    k = lex()
                    genquad('jump', '_', '_', '_')
                    backpatch(trueList, dowhilel, 1)
                    backpatch(falseList, nextquad(), 1)
                else:
                    print('----------------------------------------------------------------')
                    print("ERROR: Parentheses is open. Right parenthesis expected at line: ", line)
                    print('----------------------------------------------------------------')
                    exit()
            else:
                print('---------------------------------------------------------------------')
                print("ERROR: Parentheses did not open. Left parenthesis expected at line: ", line)
                print('---------------------------------------------------------------------')
                exit()
        else:
            print('-----------------------------------------------------')
            print("ERROR: The keyword 'while' was expected at line: ", line)
            print('-----------------------------------------------------')
            exit() 
        return k
    # --------------------------------------------------------------------------
    def exit_stat():
        genquad('Exit', '_', '_', '_')
        k = lex()
        return k
    #---------------------------------------------------------------------------
    def forcase_stat(k):
        if k.token==when_tk:
            k=lex()
            if k.token==opbrac1_tk:
                k=lex()
                tmp_arr.append(k.lektikh_monada)
                trueList.append('abc')
                falseList.append('abc')
                y=condition(k)
                tmp_arr.clear()
                makelist(quad_line)
                if y.token==clbrac1_tk:
                    genquad('jump', '_', '_', '_')
                    backpatch(trueList, nextquad(), 1)
                    k=lex()
                else:
                    print('------------------------------------------')
                    print("ERROR: ')' was expected at line: ", line)
                    print('------------------------------------------')
                    exit()
                if k.token==x:
                    k=lex()
                    y=statements(k) 
                    backpatch(falseList, nextquad(), 0)
                    if y.token==default_tk:
                        k=lex()
                        if k.token==x:
                            k=lex()
                            y=statements(k)
                            if y.token==enddefault_tk:
                                k=lex() 
                                if k.token==endforcase_tk:
                                    k=lex()
                                    return k
                                else:
                                    print('-----------------------------------------------------')
                                    print("ERROR: 'endforcase' was expected at line: ", line)
                                    print('-----------------------------------------------------')
                                    exit()
                            else:
                                print('-------------------------------------------')
                                print("ERROR: 'enddefault' was expected at line: ", line)
                                print('-------------------------------------------')
                                exit()   
                        else:
                            print('---------------------------------------')
                            print("ERROR: ':' was expected at line: ", line)
                            print('---------------------------------------')
                            exit()         
                else:
                    print('-------------------------------------------')
                    print("ERROR: ':' was expected at line: ", line)
                    print('-------------------------------------------')
                    exit()
            else:
                print('-------------------------------------------')
                print("ERROR: '(' was expected at line: ", line)
                print('-------------------------------------------')
                exit()
    #---------------------------------------------------------------------------
    def incase_stat(k):
        if k.token==when_tk:
            k=lex()
            if k.token==opbrac1_tk:
                k=lex()
                tmp_arr.append(k.lektikh_monada)
                trueList.append('abc')
                falseList.append('abc')
                y=condition(k)
                tmp_arr.clear()
                makelist(quad_line)
                if y.token==clbrac1_tk:
                    genquad('jump', '_', '_', '_')
                    backpatch(trueList, nextquad(), 1)
                    k=lex()
                else:
                    print('------------------------------------------')
                    print("ERROR: ')' was expected at line: ", line)
                    print('------------------------------------------')
                    exit()
                if k.token==x:
                    k=lex()
                    y=statements(k)  
                    backpatch(falseList, nextquad(), 0)
                    if y.token==endincase_tk:
                        k=lex()
                        return k
                    else:
                        print('--------------------------------------------')
                        print("ERROR: 'endincase' was expected.(LINE): ", line)
                        print('--------------------------------------------')
                        exit()            
                else:
                    print('------------------------------------')
                    print("ERROR: ':' was expected.(LINE): ", line)
                    print('------------------------------------')
                    exit()
            else:
                print('------------------------------------')
                print("ERROR: '(' was expected.(LINE): ", line)
                print('------------------------------------')
                exit()
    # --------------------------------------------------------------------------
    def return_stat(k):
            global temp
            newtemp()
            tmp_arr.append(new_tmp[temp])
            tmp_arr.append(':=')
            tmp_arr.append(k.lektikh_monada)
            y = expression(k)
            calculator(tmp_arr)
            genquad('retV', new_tmp[temp], '_', '_')
            temp += 1
            tmp_arr.clear()
            
            return y
    # --------------------------------------------------------------------------
    def print_stat(k):
        genquad('Print', k.lektikh_monada, '_', '_')
        y=expression(k)
        return y
    # --------------------------------------------------------------------------
    def input_stat(k):
        if k.token == id_tk:
            genquad('Input', k.lektikh_monada, '_', '_')
            k = lex()
            return k
        else:
            print('-----------------------------------------------------')
            print("ERROR: input id name was expected at line: ", line)
            print('-----------------------------------------------------')
            exit()
    # --------------------------------------------------------------------------
    def actualpars(k):
        if k.token == opbrac1_tk:
            k = lex()
            y = actualparlist(k)
            if y.token == clbrac1_tk:
                k = lex()
            else:
                print('-----------------------------------------------------')
                print("ERROR: Parentheses is open. Right parenthesis expected at line: ", line)
                print('-----------------------------------------------------')
                exit()
        else:
            print('----------------------------------------------------------------------')
            print("ERROR: Parentheses did not open. Left parenthesis expected at line: ", line)
            print('----------------------------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def actualparlist(k):
        global hlist
        if k.token == in_tk or k.token == inout_tk or k.token==inandout_tk:
            y = actualparitem(k)
            genquad('call','_' , '_', hlist[0])
            hlist.pop()
            while (y.token == comma_tk):
                k = lex()
                y = actualparitem(k)
            return y
        elif k.token != in_tk or k.token != inout_tk or k.token!=inandout_tk:
            print('------------------------------------------------------------------------------------------------')
            print("ERROR: The keyword 'in' or the keyword 'inout' or the keyword 'inandout' expected at line: ", line)
            print('------------------------------------------------------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def actualparitem(k):
        if k.token == in_tk:
            k = lex()
            genquad('par', k.lektikh_monada, 'CV', '_')
            y = expression(k)
            return y
        elif k.token == inout_tk:
            k = lex()
            genquad('par', k.lektikh_monada, 'REF', '_')
            if k.token == id_tk:
                k = lex()
            else:
                print('------------------------------------------')
                print("ERROR: Inout name was expected at line: ", line)
                print('------------------------------------------')
                exit()
            return k
        elif k.token == inandout_tk:
            k = lex()
            genquad('par', k.lektikh_monada, 'COPY', '_')
            if k.token == id_tk:
                k = lex()
            else:
                print('-----------------------------------------------------')
                print("ERROR: Inandout name was expected at line: ", line)
                print('-----------------------------------------------------')
                exit()
            return k
        else:
            print('------------------------------------------------------------------------------------------------')
            print("ERROR: The keyword 'in' or the keyword 'inout'or the keyword 'inandout' was expected at line: ", line)
            print('------------------------------------------------------------------------------------------------')
            exit()
    # --------------------------------------------------------------------------
    def condition(k):
        y = boolterm(k)
        while (y.token == or_tk):
            tmp_arr.clear()
            makelist(quad_line)
            genquad('jump', '_', '_', quad_line + 1)
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            y = boolterm(k)
        return y
    # --------------------------------------------------------------------------
    def boolterm(k):
        y = boolfactor(k)
        calculator_of_condition(tmp_arr)
        while (y.token == and_tk):
            tmp_arr.clear()
            makelist(quad_line)
            genquad('jump', '_', '_', '_')
            backpatch(trueList, nextquad() , 1)
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            y = boolfactor(k)
            calculator_of_condition(tmp_arr)
        return y
    # --------------------------------------------------------------------------
    def boolfactor(k):
        if k.token == not_tk:
            k = lex()
            if k.token == opbrac2_tk:
                k = lex()
                y = condition(k)
                if y.token == clbrac2_tk:
                    k = lex()
                else:
                    print('------------------------------------------------------------')
                    print("ERROR: Bracket is open. Right bracket expected at line: ", line)
                    print('------------------------------------------------------------')
                    exit()
            else:
                print('--------------------------------------------------------------------')
                print("ERROR: Bracket did not open. Left bracket expected at line: ", line)
                print('--------------------------------------------------------------------')
                exit()
            return k
        elif k.token == opbrac2_tk:
            k = lex()
            y = condition(k)
            if y.token == clbrac2_tk:
                k = lex()
            else:
                print('-----------------------------------------------------------------')
                print("ERROR: Bracket is open. Right bracket was expected at line: ", line)
                print('-----------------------------------------------------------------')
                exit()
            return k
        else:
            y = expression(k)
            z = relational_oper(y)
            u = expression(z)
            return u
        return k
    # --------------------------------------------------------------------------
    def expression(k):
        y = optional_sign(k)
        z = term(y)
        while (z.token == plus_tk or z.token == minus_tk):
            y = add_oper(k)
            z = term(y)
        return z
    # --------------------------------------------------------------------------
    def term(k):
        y = factor(k)
        while (y.token == multi_tk or y.token == division_tk):
            d = mul_oper(y)
            z = factor(d)
            return z
        return y
    # --------------------------------------------------------------------------
    def factor(k):
        if k.token == digit_tk:
            k = lex()
            if k.token == digit_tk or (k.token >= 3 and k.token <= 12) or k.token == 22:
                tmp_arr.append(k.lektikh_monada)   
        elif k.token == opbrac1_tk:
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            y = expression(k)
            if y.token == clbrac1_tk:
                k = lex()     
                tmp_arr.append(k.lektikh_monada) 
            else:
                print('----------------------------------------')
                print("ERROR: Close parenthesis at line: ", line)
                print('----------------------------------------')
                exit()
        elif k.token == id_tk:
            k = lex()
            tmp_arr.append(k.lektikh_monada)
            k = idtail(k)
        else:
            print('-----------------------------------------------------')
            print("ERROR: digit or '(' or id was expected at line: ", line)
            print('-----------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def idtail(k):
        if k.token==opbrac1_tk:
            y = actualpars(k)
            return y
        return k
    # --------------------------------------------------------------------------
    def relational_oper(k): 
        global typer, strr
        typer = 0
        strr = ''
        if k.token == equal_tk:
            strr = k.lektikh_monada
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == smaller_tk:
            strr = k.lektikh_monada
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == smallequal_tk:
            typer = 1
            strr = k.lektikh_monada
            tmp_arr.pop()
            tmp_arr.append('<')
            tmp_arr.append('=')
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == different_tk:
            typer = 1
            strr = k.lektikh_monada
            tmp_arr.pop()
            tmp_arr.append('<')
            tmp_arr.append('>')
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == greatequal_tk:
            typer = 1
            strr = k.lektikh_monada
            tmp_arr.pop()
            tmp_arr.append('>')
            tmp_arr.append('=')
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == greater_tk:
            strr = k.lektikh_monada
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        else:
            print('-----------------------------------------------------')
            print("ERROR: Relational operator was expected at line: ", line)
            print('-----------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def add_oper(k):
        if k.token == plus_tk:
            tmp_arr.append(k.lektikh_monada)
            k = lex() 
            tmp_arr.append(k.lektikh_monada)  
        elif k.token == minus_tk:
            tmp_arr.append(k.lektikh_monada)
            k = lex()   
            tmp_arr.append(k.lektikh_monada)
        else:
            print('-----------------------------------------------------')
            print("ERROR: Add or Minus operator was expected at line: ", line)
            print('-----------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def mul_oper(k):
        if k.token == multi_tk:
            tmp_arr.append(k.lektikh_monada)
            k = lex()
            tmp_arr.append(k.lektikh_monada)
        elif k.token == division_tk:
            tmp_arr.append(k.lektikh_monada)
            k = lex()  
            tmp_arr.append(k.lektikh_monada)
        else:
            print('----------------------------------------------------------')
            print("ERROR: Multiply or division operator was expected at line: ", line)
            print('----------------------------------------------------------')
            exit()
        return k
    # --------------------------------------------------------------------------
    def optional_sign(k):
        if k.token == plus_tk or k.token == minus_tk:
            y = add_oper(k)
            return y
        return k
    # --------------------------------------------------------------------------
    program(k)
k = lex()
syntax(k)
#==========mips file creator=======================================================================

def mips_file_creator(array):
    global ti ,si,vi,ai, parCounter, frCounter,offset
    li = 1
    fpar=0
    arxi = 0
    telos = 0
    callName = ""
    mips.write("==============================\n")
    mips.write("#ANDREAS MATSIAS 3025 cse53025\n")
    mips.write("==============================\n")
    if kkk>=1:
        mips.write("\tL:\n")
        mips.write("\t\tj Lmain\n")
    mips.write("\tL0:\n")
    mips.write("\t\tsw $ra,($sp)\n")
    for i in range(0, len(array)):
        if array[i][0] != "begin_block" and array[i][0] != "end_block":
            mips.write("\tL" + str(li) + ": \n")
        #if array[i][0] == "begin_block":
            #mips.write("sw $ra,($sp)\n")
        #-------[:=]
        if array[i][0] == ":=":
            li = li + 1
            if array[i][1].isdigit():
                mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n")
                mips.write("\t\tsw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")    
            else:
                mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")
                mips.write("\t\tsw $t" + str(ti) + ",-"+str(offset)+"($sp)\n" )
            si=si+1
            ti=ti+1
        #--------[+,-,*,/]
        elif array[i][0] == "+" or array[i][0] == "-" or array[i][0] == "*" or array[i][0] == "/":
            li = li + 1
            ti = ti+1
            si = si+1
            if array[i][1].isdigit():
                mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n")
            else:
                mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")  
            if array[i][0] == "+":
                mips.write("\t\taddi $t" +str(ti) + ","+"$t"+ str(ti) + ","+"$t"+ str(ti+1)+"\n")
            elif array[i][0] == "-":
                mips.write("\t\tsubi $t" +str(ti) + ","+"$t"+ str(ti) + ","+"$t"+ str(ti+1)+"\n")
            elif array[i][0] == "*":
                mips.write("\t\tmuli $t" +str(ti) + ","+"$t"+ str(ti) + ","+"$t"+ str(ti+1)+"\n")
            elif array[i][0] == "/":
                mips.write("\t\tdivi $t" +str(ti) + ","+"$t"+ str(ti) + ","+"$t"+ str(ti+1)+"\n")
            mips.write("\t\tsw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")
        #--------------[jump]
        elif array[i][0] == "jump":
            mips.write("\t\tj L" + str(int(array[i][3])) + "\n")
            li = li + 1
        #----------------[<>,<=,<,>=,>,=]
        elif array[i][0] == "<" or array[i][0] == "<=" or array[i][0] == ">" or array[i][0] == ">=" or array[i][0] == "=" or array[i][0] == "<>":
            if array[i][1].isdigit():
                mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n") 
            else:
                mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")           
            if array[i][0] == "<":
                mips.write("\t\tblt $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            elif array[i][0] == "<=":
                mips.write("\t\tble $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            elif array[i][0] == ">":
                mips.write("\t\tbgt $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            elif array[i][0] == ">=":
                mips.write("\t\tbge $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            elif array[i][0] == "=":
                mips.write("\t\tbeq $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            elif array[i][0] == "<>":
                mips.write("\t\tbne $t" +str(ti) + ","+"$t"+ str(ti+1) + ", L" + str(int(array[i][3])) + "\n")
            si=si+1
            ti=ti+1
            li = li + 1
        #---------------[out]
        elif array[i][0] == "Print":
            mips.write("\t\tli $v" + str(vi) + ",1\n")
            mips.write("\t\tli $a" + str(ai) + ","+ array[i][1]+ "\n")
            mips.write("\t\tsyscall\n")
            vi = vi + 1
            ai = ai + 1
            li = li + 1
        #------------[input]
        elif array[i][0] == "Input":
            mips.write("\t\tli $a" + str(ai) + ","+ array[i][1] +"\n")
            mips.write("\t\tsyscall\n")
            ai=ai+1
            li = li + 1
        #-------------[return]
        elif array[i][0] == "retV":
            if array[i][1].isdigit():
                    mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n")
            else:
                    mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n") 
            mips.write("\t\tlw $t" + str(ti) + ",-8($sp)\n")
            mips.write("\t\tsw $t" + str(ti+1) + ",-"+str(offset)+"($sp)\n" )
            li = li + 1
        #-------------[parameters]
        elif array[i][0] == "par":
            if fpar==0:
                mips.write("addi $fp,$sp,"+frame_length+"\n")
            fpar=fpar+1
            parCounter += 1
            li = li + 1
            #-------{CV}
            if array[i][2] == "CV":
                if array[i][1].isdigit():
                    mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n")
                else:
                    mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")
                mips.write("\t\tsw $t" + str(ti) + ",-"+str(12+4*parCounter)+"($fp)\n")  
            #-------{REF}
            elif array[i][2] == "REF":
                for ib in range(i, len(array)):
                    if array[ib][0] == "call":
                        callName = array[ib][1]
                        break
                for ic in range(0, len(array)):
                    if array[ic][0] == "begin_block" and array[ic][1] == callName:
                        arxi = ic
                    if array[ic][0] == "end_block" and array[ic][1] == callName:
                        telos = ic
                if ib > arxi and ib < telos:
                    mips.write("\t\tlw $t" + str(ti) + ",-4($sp)\n")
                    mips.write("\t\tsw $t" + str(ti) + ",-"+str(12+4*parCounter)+"($fp)\n")
                else:
                    mips.write("\t\tlw $t" + str(ti) + ",-4($sp)\n")
                    mips.write("\t\tadd $t" + str(ti) +",$t" + str(ti) + ",-"+offset+"\n")
                    mips.write("\t\tadd $t" + str(ti) +",$t" + str(ti)+"\n")
                    mips.write("\t\tsw $t" + str(ti) + ",-"+str(12+4*parCounter)+"($fp)\n")
            #---------------{COPY}
            elif array[i][2] == "COPY":
                if array[i][1].isdigit():
                    mips.write("\t\tli $t" + str(ti) + "," + str(array[i][1]) + "\n")
                else:
                    mips.write("\t\tlw $t" + str(ti) + ",-"+str(offset)+"($s" + str(si) + ")\n")
                mips.write("\t\tsw $t" + str(ti) + ",-"+str(12+4*parCounter)+"($fp)\n")
            frCounter += 1
            ti += 1
        #----------------
        elif array[i][0] == "halt":
            li = li + 1
            mips.write("li $v0,10 ")
            mips.write("\t\tsyscall\n")
        elif array[i][0] == "end_block":
            ti = 0
            li = li + 1
            mips.write("\t\tjr $ra\n")
            
#=================================================================================
real_offset[len(real_offset) - 1] = offset
real_offset.reverse()
print("===========================")
print("real_offset:", real_offset)
print("===========================")
print("start_quad:", start_quad)
print("===========================")
print("frame_length:", frame_length)
print("===========================")
int_creator()
c_file_creator()
mips_file_creator(quad_array)
#====================================================================
q = input("Do you want to search for an Entity?(yes or no) ")
if q=='yes'or q=='y'or q=='YES'or q=='Y':
    r= input("types the entity for search: ")
    searchEntity(r)
else:
    exit()
#======================================================================