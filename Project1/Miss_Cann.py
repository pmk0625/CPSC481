from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0,0,False)):
        initial = (M,C,True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)


    def isValid(self, state):
        if state[0] < 0 or state[0] > self.initial[0]:
            return False
        elif state[1] < 0 or state[1] > self.initial[1]:
            return False
        elif state[1] > state[0] and state[0] != 0: 
            return False
        elif self.initial[1] - state[1] > self.initial[0] - state[0] and state[0] != self.initial[0]:
            return False
        else:
            return True


    def actions(self, state):
        """ Returns all possible actions for a given state """
        actions = []
        if self.isValid(self.result(state, 'M')):
            actions.append('M')
        if self.isValid(self.result(state, 'MM')):
            actions.append('MM')
        if self.isValid(self.result(state, 'MC')):
            actions.append('MC')
        if self.isValid(self.result(state, 'CC')):
            actions.append('CC')
        if self.isValid(self.result(state, 'C')):
            actions.append('C')

        return actions

    def result(self, state, action):
        """ Given a state and action, returns the results of that action """
        current = list(state)
        if current[2]:
            for c in action:
                if c == 'M':
                    current[0] -= 1
                if c == 'C':
                    current[1] -= 1
        else:
            for c in action:
                if c == 'M':
                    current[0] += 1
                if c == 'C':
                    current[1] += 1
        current[2] = not current[2]

        return tuple(current)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced Cannibals and Missionaries """
        return self.M + self.C

if __name__ == '__main__':
    mc = MissCannibals()

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)


""" 
    print("results")
    print(mc.result((3,2,True), 'M'))
    print(mc.result((3,2,True), 'MM'))
    print(mc.result((3,2,True), 'MC'))
    print(mc.result((3,2,True), 'CC'))
    print(mc.result((3,2,True), 'C'))

    print("isvalidresults")
    print(mc.isValid(mc.result((3,2,True), 'M')))
    print(mc.isValid(mc.result((3,2,True), 'MM')))
    print(mc.isValid(mc.result((3,2,True), 'MC')))
    print(mc.isValid(mc.result((3,2,True), 'CC')))
    print(mc.isValid(mc.result((3,2,True), 'C')))

    print(mc.actions((3,2,True)))
"""


    