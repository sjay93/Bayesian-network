import sys
from Bayesian_Network import *
from copy import *

def main(args):

    final_ans = 0.00
    first_val, second_val = evaluateInput(args)
    bay_net = Bayesian_Network()
    table = create_Row_TT([],first_val)
    for i in table:
        final_ans += bay_net.calculateProbability(i[0],i[1],i[2],i[3],i[4],second_val)

    print 'Probability of given combination of events given any other combination of events is ::'+str('%.5f'%final_ans)

def evaluateInput(args):
    ip_array = args[1:]
    B = None
    E = None
    A = None
    J = None
    M = None
    cond = []

    for i in args:
        if i[0] == 'B' and i[1] == 't':
            B = True
        elif i[0] == 'B' and i[1] == 'f':
            B = False

        if i[0] == 'E' and i[1] == 't':
            E = True
        elif i[0] == 'E' and i[1] == 'f':
            E = False

        if i[0] == 'A' and i[1] == 't':
            A = True
        elif i[0] == 'A' and i[1] == 'f':
            A = False

        if i[0] == 'J' and i[1] == 't':
            J = True
        elif i[0] == 'J' and i[1] == 'f':
            J = False

        if i[0] == 'M' and i[1] == 't':
            M = True
        elif i[0] == 'M' and i[1] == 'f':
            M = False

    givenConditionIndex = 0
    if ip_array.count('given'):
        givenConditionIndex = ip_array.index('given')
        for j in range(givenConditionIndex+1,len(ip_array)):
            cond.append(ip_array[j][0])

    return ([B,E,A,J,M],cond)

def create_Row_TT(truth_table,input_con):
    if input_con.count(None) != 0:
        index_none = input_con.index(None)
        Tr = deepcopy(input_con)
        Tr[index_none] = True
        create_Row_TT(truth_table,Tr)
        Fa = deepcopy(input_con)
        Fa[index_none] = False
        create_Row_TT(truth_table,Fa)
        return truth_table
    else:
        truth_table.append(input_con)
        return truth_table

if __name__ == '__main__':
    main(sys.argv)
