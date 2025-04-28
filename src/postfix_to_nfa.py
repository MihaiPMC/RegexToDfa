state_id = 0
all_states = []

class State:
    def __init__(self, id):
        self.id = id
        self.transitions = {}
        self.epsilon = []

    def add_transition(self, symbol, state):
        self.transitions.setdefault(symbol, []).append(state)

    def add_epsilon(self, state):
        self.epsilon.append(state)


def new_state():
    global state_id, all_states
    st = State(state_id)
    state_id += 1
    all_states.append(st)
    return st

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
        self.accept.is_accept = True
        self.states = list(all_states)


def postfix_to_nfa(postfix):
    global state_id, all_states
    state_id = 0
    all_states = []
    stack = []

    for c in postfix:
        if c.isalnum():
            start = new_state()
            accept = new_state()
            start.add_transition(c, accept)
            stack.append(NFA(start, accept))

        elif c == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()

            if hasattr(nfa1.accept, 'is_accept'):
                nfa1.accept.is_accept = False
            if hasattr(nfa2.start, 'is_accept'):
                nfa2.start.is_accept = False

            nfa1.accept.add_epsilon(nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.accept))

        elif c == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()

            if hasattr(nfa1.accept, 'is_accept'):
                nfa1.accept.is_accept = False
            if hasattr(nfa2.accept, 'is_accept'):
                nfa2.accept.is_accept = False

            start = new_state()
            accept = new_state()

            start.add_epsilon(nfa1.start)
            start.add_epsilon(nfa2.start)

            nfa1.accept.add_epsilon(accept)
            nfa2.accept.add_epsilon(accept)

            stack.append(NFA(start, accept))

        elif c == '*':
            nfa = stack.pop()
            if hasattr(nfa.accept, 'is_accept'):
                nfa.accept.is_accept = False

            start = new_state()
            accept = new_state()

            start.add_epsilon(nfa.start)
            start.add_epsilon(accept)

            nfa.accept.add_epsilon(nfa.start)
            nfa.accept.add_epsilon(accept)

            stack.append(NFA(start, accept))

        elif c == '+':
            nfa = stack.pop()

            if hasattr(nfa.accept, 'is_accept'):
                nfa.accept.is_accept = False

            start = new_state()
            accept = new_state()

            start.add_epsilon(nfa.start)
            nfa.accept.add_epsilon(nfa.start)
            nfa.accept.add_epsilon(accept)

            stack.append(NFA(start, accept))

        elif c == '?':
            nfa = stack.pop()

            if hasattr(nfa.accept, 'is_accept'):
                nfa.accept.is_accept = False

            start = new_state()
            accept = new_state()

            start.add_epsilon(nfa.start)
            start.add_epsilon(accept)
            nfa.accept.add_epsilon(accept)

            stack.append(NFA(start, accept))

    return stack[0]


def print_nfa(nfa):
    print("NFA States and Transitions:")
    for st in nfa.states:

        is_accept = ""
        if hasattr(st, 'is_accept') and st.is_accept:
            is_accept = "(Accept)"

        print(f"State {st.id} {is_accept}")
        for symbol, destination in st.transitions.items():
            for d in destination:
                print(f"  {symbol} -> State {d.id}")

        for d in st.epsilon:
            print(f"  ε -> State {d.id}")

if __name__ == "__main__":
    postfix = "ab.*"
    nfa = postfix_to_nfa(postfix)
    print_nfa(nfa)
