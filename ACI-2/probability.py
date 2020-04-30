#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:51:21 2020

@author: klrao
"""
import numpy as np
from collections import defaultdict

class ProbabDist:
    
    def __init__(self,varname='?',freqs=None):
        self.varname = varname
        self.values = []
        self.prob = {}
        
        if freqs:
            for(v,p) in freqs.items():
                print("In Constructor")
                self[v] = p
                
    
    def __getitem__(self,val):
        print("getItem val->",val)
        try:
            return self.prob[val]
        except KeyError:
            return 0;
    
    def __setitem__(self,val,p):
        print("setItem",val,p)
        if val not in self.values:
            self.values.append(val)
        
        self.prob[val] = p
        
    def normalize(self):
    
        total = sum(self.prob.values())
        if not np.isclose(total,1.0):
            for val in self.prob:
                self.prob[val]/= total
                
        return self
    
    def show_approx(self,numfmt='{:.3g}'):
        
        return ', '.join([('{}: ' + numfmt).format(v, p)
                          for (v, p) in sorted(self.prob.items())])
    
    def __repr__(self):
        return "P({})".format(self.varname)
    
class JointProbabDist(ProbabDist):
    def __init__(self,variables):
        print("------------INIT ----------------------- ")
        print("INIT variables:",variables)
        self.prob = {}
        self.variables = variables
        self.vals = defaultdict(list)
        print("INIT self.prob:",self.prob)
        print("INIT self.vals:",self.vals)
        print("Type of prob:",type(self.prob))
        print("Type of variables:",type(self.variables))
        print("Type of vals:",type(self.vals))
        print("------------INIT ----------------------- ")
        
    def __getitem__(self,values):
        print("------------GET ITEM START ----------------------- ")
        print("Before getItem values:",values)
        values = event_values(values,self.variables)
        print("After getItem values:",values)
        print("------------GET ITEM END----------------------- ")
        return ProbabDist.__getitem__(self,values)
    
    def __setitem__(self,values,p):
        print("*************setItem values START********************")
        print("Before setItem values=>",values," len(values)",len(values)," p=>",p)
        print("Before setItem self.variables=>",self.variables," p=>",p)
        values = event_values(values,self.variables)
        self.prob[values] = p
        print("Prob ::self.prob[values]=",self.prob[values])
        print("Print ::self.prob=",self.prob)
        print("After setItem ::Values",values)
        for var,val in zip(self.variables,values):
            if val not in self.vals[var]:
                self.vals[var].append(val)
                
        print("After setItem ::self.vars=",self.vals)
                
        print("*************setItem values END********************")
    
    def values(self, var):
        """Return the set of possible values for a variable."""
        print("------------VALUES START----------------------- ")
        print("var",var," vals[var]",self.vals[var])
        print("------------VALUES END----------------------- ")
        return self.vals[var]
    
    def __repr__(self):
        print("------------REPR START----------------------- ")
        print("P({})".format(self.variables))
        print("------------REPR START----------------------- ")
        return "P({})".format(self.variables)


class vartest:

    def __init__(self,variables):
        self.variables = variables

def event_values(event, variables):
    """Return a tuple of the values of variables in event.
    >>> event_values ({'A': 10, 'B': 9, 'C': 8}, ['C', 'A'])
    (8, 10)
    >>> event_values ((1, 2), ['C', 'A'])
    (1, 2)
    """
    print("IN event_values variables=>",variables)
    print("IN event_values event=>",event)
    if isinstance(event, tuple) and len(event) == len(variables):
        return event
    else:
        return tuple([event[var] for var in variables])
    
def enumerate_joint_ask(X, e, P):
    """
    [Section 13.3]
    Return a probability distribution over the values of the variable X,
    given the {var:val} observations e, in the JointProbDist P.
    >>> P = JointProbDist(['X', 'Y'])
    >>> P[0,0] = 0.25; P[0,1] = 0.5; P[1,1] = P[2,1] = 0.125
    >>> enumerate_joint_ask('X', dict(Y=1), P).show_approx()
    '0: 0.667, 1: 0.167, 2: 0.167'
    """
    assert X not in e, "Query variable must be distinct from evidence"
    Q = ProbabDist(X)  # probability distribution for X, initially empty
    Y = [v for v in P.variables if v != X and v not in e]  # hidden variables.
    for xi in P.values(X):
        Q[xi] = enumerate_joint(Y, extend(e, X, xi), P)
    return Q.normalize()


def enumerate_joint(variables, e, P):
    """Return the sum of those entries in P consistent with e,
    provided variables is P's remaining variables (the ones not in e)."""
    if not variables:
        return P[e]
    Y, rest = variables[0], variables[1:]
    return sum([enumerate_joint(rest, extend(e, Y, y), P) for y in P.values(Y)])

def extend(s, var, val):
    """Copy dict s and extend it by setting var to val; return copy."""
    try:  # Python 3.5 and later
        return eval('{**s, var: val}')
    except SyntaxError:  # Python 3.4
        s2 = s.copy()
        s2[var] = val
        return s2


   
def main():
    '''p = ProbabDist('Flip')
    p['H'] , p['T'] = 0.25,0.75
    print("========Main  1=================")
    print("Main",p,p['H'],p['T'])
    
    print("========Main  1==================")
    
    print("========Main  2=================")
    p1 = ProbabDist('X', {'lo': 125, 'med': 375, 'hi': 500})
    print("Main2",p1,p1['lo'],p1['hi '])
    print("========Main  2==================")
    
    print("========Main  3==================")
    event = {'A': 10, 'B': 9, 'C': 8}
    variables = ['C', 'A']
    print(event_values(event, variables))
    print("========Main  3==================")
    
    print("========Main  4==================")
    PJ = JointProbabDist(['X', 'Y']); 
    PJ[1, 1] = 0.25
    
    print("========Main  5==================")
    
    PJ[dict(X=0, Y=1)] = 0.5
    #print(PJ[0,1])
    #PJ[1,1] = 0.2
    #print(PJ[1,1])
    
    print(PJ.values('X'))'''
    
    print("========JOINT Probability Distributions  BEGIN ==================")
    full_joint = JointProbabDist(['Cavity', 'Toothache', 'Catch'])
    full_joint[dict(Cavity=True, Toothache=True, Catch=True)] = 0.108
    full_joint[dict(Cavity=True, Toothache=True, Catch=False)] = 0.012
    full_joint[dict(Cavity=True, Toothache=False, Catch=True)] = 0.016
    full_joint[dict(Cavity=True, Toothache=False, Catch=False)] = 0.064
    full_joint[dict(Cavity=False, Toothache=True, Catch=True)] = 0.072
    full_joint[dict(Cavity=False, Toothache=False, Catch=True)] = 0.144
    full_joint[dict(Cavity=False, Toothache=True, Catch=False)] = 0.008
    full_joint[dict(Cavity=False, Toothache=False, Catch=False)] = 0.576
    print("========JOINT Probability Distributions END==================")
    
    evidence = dict(Toothache=True)
    variables = ['Cavity', 'Catch'] # variables not part of evidence
    ans1 = enumerate_joint(variables, evidence, full_joint)
    ans1
    
    print("ansswer is ",ans1)
    
    evidence = dict(Cavity=True, Toothache=True)
    variables = ['Catch'] # variables not part of evidence
    ans2 = enumerate_joint(variables, evidence, full_joint)
    print("Answer 2 is ",ans2)
    
    query_variable = 'Cavity'
    evidence = dict(Toothache=True)
    ans = enumerate_joint_ask(query_variable, evidence, full_joint)
    print((ans[True], ans[False]))
if __name__ == '__main__':
    main()
