import search
from math import(cos, pi)

# A sample map problem
slo_map = search.UndirectedGraph(dict(
   #Portland=dict(Mitchellville=7, Fairfield=17, Cottontown=18),
   #Cottontown=dict(Portland=18),
   #Fairfield=dict(Mitchellville=21, Portland=17),
   #Mitchellville=dict(Portland=7, Fairfield=21),
    SanLuis=dict(AvilaBeach=11, MorroBay=15, Atascadero=18),
    AvilaBeach=dict(SanLuis=11, MorroBay=28, SantaMaria=30),
    Atascadero=dict(Templeton=7, SanLuis=18, MorroBay=23, Cayucos=27),
    MorroBay=dict(Cayucos=8, SanLuis=15, AvilaBeach=28, Atascadero=23),
    SantaMaria=dict(AvilaBeach=30, Nipomo=11),
    Nipomo=dict(SantaMaria=11, SanLuis=25),
    Cayucos=dict(MorroBay=8, Atascadero=27, Templeton=31),
    Templeton=dict(Atascadero=7, Cayucos=31),


))

slo_puzzle = search.GraphProblem('Cayucos', 'SantaMaria', slo_map)

slo_puzzle.label = 'SLO'
slo_puzzle.description = '''
An abbreviated map of San Luis Obispo, CA.
This map is unique, to the best of my knowledge.
'''

romania_map = search.UndirectedGraph(dict(
    A=dict(Z=75,S=140,T=118),
    Z=dict(O=71,A=75),
    S=dict(O=151,R=80,F=99),
    T=dict(A=118,L=111),
    O=dict(Z=71,S=151),
    L=dict(T=111,M=70),
    M=dict(L=70,D=75),
    D=dict(M=75,C=120),
    R=dict(S=80,C=146,P=97),
    C=dict(R=146,P=138,D=120),
    F=dict(S=99,B=211),
    P=dict(R=97,C=138,B=101),
    B=dict(G=90,P=101,F=211),
))

romania_puzzle = search.GraphProblem('A', 'B', romania_map)

romania_puzzle.label = 'Romania'
romania_puzzle.description = '''
The simplified map of Romania, per
Russall & Norvig, 3rd Ed., p. 68.
'''

# A trivial Problem definition
class LightSwitch(search.Problem):
    def actions(self, state):
        return ['up', 'down']

    def result(self, state, action):
        if action == 'up':
            return 'on'
        else:
            return 'off'

    def goal_test(self, state):
        return state == 'on'

    def h(self, node):
        state = node.state
        if self.goal_test(state):
            return 0
        else:
            return 1

#swiss_puzzle = search.GraphProblem('A', 'Z', sumner_map)
switch_puzzle = LightSwitch('off')
switch_puzzle.label = 'Light Switch'

mySearches = [
 #   swiss_puzzle,
   # sumner_puzzle,
    romania_puzzle,
    switch_puzzle,
    slo_puzzle,
]
