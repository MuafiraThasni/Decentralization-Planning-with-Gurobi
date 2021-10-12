# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:47:28 2021

@author: muafira
"""
import pandas as pd
import gurobipy as gp
from gurobipy import GRB

# Defining Input Data 

departments = ['A', 'B', 'C', 'D', 'E']
cities = ['Bristol', 'Brighton', 'London']

# dictionary to capture benefits -in thousands of dollars from relocation.
dc,benefit = gp.multidict({ ('A','Bristol'):10,  ('A','Brighton'):10,  ('A','London'):0,
                           ('B','Bristol'):15,  ('B','Brighton'):20,  ('B','London'):0,
                           ('C','Bristol'):10,  ('C','Brighton'):15,  ('C','London'):0,
                           ('D','Bristol'):20,  ('D','Brighton'):15,  ('D','London'):0,
                           ('E','Bristol'):5,  ('E','Brighton'):15,  ('E','London'):0})
# dictionary to capture communication cost
dcd2c2,communication_cost = gp.multidict({
    ('A','London','C','Bristol'): 13,
    ('A','London','C','Brighton'): 9,
    ('A','London','C','London'): 10,
    ('A','London','D','Bristol'): 19.5,
    ('A','London','D','Brighton'): 13.5,
    ('A','London','D','London'): 15,
    ('B','London','C','Bristol'): 18.2,
    ('B','London','C','Brighton'): 12.6,
    ('B','London','C','London'): 14,
    ('B','London','D','Bristol'): 15.6,
    ('B','London','D','Brighton'): 10.8,
    ('B','London','D','London'): 12,
    ('C','London','E','Bristol'): 26,
    ('C','London','E','Brighton'): 18,
    ('C','London','E','London'): 20,
    ('D','London','E','Bristol'): 9.1,
    ('D','London','E','Brighton'): 6.3,
    ('D','London','E','London'): 7,
    ('A','Bristol','C','Bristol'): 5,
    ('A','Bristol','C','Brighton'): 14,
    ('A','Bristol','C','London'): 13,
    ('A','Bristol','D','Bristol'): 7.5,
    ('A','Bristol','D','Brighton'): 21,
    ('A','Bristol','D','London'): 19.5,
    ('B','Bristol','C','Bristol'): 7,
    ('B','Bristol','C','Brighton'): 19.6,
    ('B','Bristol','C','London'): 18.2,
    ('B','Bristol','D','Bristol'): 6,
    ('B','Bristol','D','Brighton'): 16.8,
    ('B','Bristol','D','London'): 15.6,
    ('C','Bristol','E','Bristol'): 10,
    ('C','Bristol','E','Brighton'): 28,
    ('C','Bristol','E','London'): 26,
    ('D','Bristol','E','Bristol'): 3.5,
    ('D','Bristol','E','Brighton'): 9.8, 
    ('D','Bristol','E','London'): 9.1,
    ('A','Brighton','C','Bristol'): 14,
    ('A','Brighton','C','Brighton'): 5,
    ('A','Brighton','C','London'): 9,
    ('A','Brighton','D','Bristol'): 21,
    ('A','Brighton','D','Brighton'): 7.5,
    ('A','Brighton','D','London'): 13.5,
    ('B','Brighton','C','Bristol'): 19.6,
    ('B','Brighton','C','Brighton'): 7,
    ('B','Brighton','C','London'): 12.6,
    ('B','Brighton','D','Bristol'): 16.8,
    ('B','Brighton','D','Brighton'): 6,
    ('B','Brighton','D','London'): 10.8,
    ('C','Brighton','E','Bristol'): 28,
    ('C','Brighton','E','Brighton'): 10,
    ('C','Brighton','E','London'): 18,
    ('D','Brighton','E','Bristol'): 9.8,
    ('D','Brighton','E','Brighton'): 3.5,
    ('D','Brighton','E','London'): 6.3
    })
# Model Deployment

model = gp.Model('decentralization')
model.params.nonConvex = 2
locate = model.addVars(dc, vtype= GRB.BINARY, name = "locate")

# Constraints

#1. each department can locate at one city only
dep_location = model.addConstrs((gp.quicksum(locate[d,c]for c in cities)==1 for d in departments), name='dep_location')

#2. Maximum of three departmetns at one city

dep_limit = model.addConstrs((gp.quicksum(locate[d,c] for d in departments )<= 3 for c in cities))


# Objective : max(gross margin)
model.setObjective((gp.quicksum(benefit[d,c]*locate[d,c] for d,c in dc)  - gp.quicksum(communication_cost[d,c,d2,c2]*locate[d,c]*locate[d2,c2] for d,c,d2,c2 in dcd2c2) ), GRB.MAXIMIZE)
# Verify model formulation

model.write('decentralizationQA.lp')

# Run optimization engine

model.optimize()





