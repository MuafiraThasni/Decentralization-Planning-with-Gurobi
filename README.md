

# Decentralization-Planning-with-Gurobi

Mathematical Optimization Modeling challenge by Gurobi optimizer. 
# Problem Description
A large company wants to move some of its departments out of London. Doing so will result in reduced costs in some areas (such as cheaper housing, government incentives, easier recruitment, etc.), and increased costs in other areas (such as communication between departments). The cost implications for all possible locations of each department have been calculated. The goal is to determine where to locate each department in order to maximize the total difference between the reduced costs from relocating and the increased communication costs between departments.

The company comprises five departments (A, B, C, D and E). The possible cities for relocation are Bristol and Brighton, or a department may be kept in London. None of these cities (including London) may be the location for more than three of the departments.

# Model Formulation
Parameters:

cities = c :{Bristol, Brighton, Japan}

departments = d: {A,B,C,D,E}

increased cost : communication cost for communicating between departments. So if two departments under communication are relocated, it will affect the communication cost of both departments.

reduced cost : benefit for relocating d to c

So, benefit_dc  =Benefit -in thousands of dollars per year, derived from relocating department  d  to city  c .
and communication_cost_dcd2c2 = Communication cost -in thousands of dollars per year, derived from relocating department  d  to city  c  and relocating department  d2  to city  c2 .

where dcd2c2 belongs to {departmetn x cities x department x cities : for all communication_cost_dcd2c2 > 0}

Decision Variables:

binary varibale for deciding whether the departmetn is in city c or not : located,c∈{0,1} : This binary variable is equal 1, if department d is located at city c, and 0 otherwise

yd,c,d2,c2=located,c∗located2,c2∈{0,1} : This auxiliary binary variable is equal 1, if department  d  is located at city  c  and department  d2  is located at city  c2 , and 0 otherwise.

Constraints:

One departmetn at only one location, no more than three departments at one city, 
logical constraints: If  yd,c,d2,c2=1  then  located,c=1  and  located2,c2=1 . and If  located,c=1  and  located2,c2=1  then  yd,c,d2,c2=1 .

Objective function:

maximize the gross margin,




