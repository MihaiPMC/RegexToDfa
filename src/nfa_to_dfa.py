class DFAState:
    def __init__(self, nfa_states, id):
        self.id = id
        self.nfa_states = nfa_states
        self.transitions = {}
        self.is_accept = any(getattr(s, 'is_accept', False) for s in nfa_states)

class DFA:
    def __init__(self, start_state):
        self.start = start_state
        self.states = [start_state]
        self.state_map = {frozenset(start_state.nfa_states): start_state}
        self.alphabet = set()

    def add_state(self, nfa_states):
        ns_frozen = frozenset(nfa_states)
        if ns_frozen in self.state_map:
            return self.state_map[ns_frozen]
        new_state = DFAState(nfa_states, len(self.states))
        self.states.append(new_state)
        self.state_map[ns_frozen] = new_state
        return new_state

def epsilon_closure(nfa_state, visited=None):
    if visited is None:
        visited = set()
    if nfa_state in visited:
        return visited
    visited.add(nfa_state)
    for next_state in nfa_state.epsilon:
        epsilon_closure(next_state, visited)
    return visited

def epsilon_closure_set(nfa_states):
    closure = set()
    for state in nfa_states:
        closure.update(epsilon_closure(state))
    return closure

def move(nfa_states, symbol):
    result = set()
    for state in nfa_states:
        if symbol in state.transitions:
            result.update(state.transitions[symbol])
    return result

def nfa_to_dfa(nfa):
    alphabet = set()
    for state in nfa.states:
        alphabet.update(state.transitions.keys())
    start_closure = epsilon_closure_set({nfa.start})
    start_dfa = DFAState(start_closure, 0)
    dfa = DFA(start_dfa)
    dfa.alphabet = alphabet

    unmarked = [start_dfa]
    processed = set()
    while unmarked:
        current = unmarked.pop()
        processed.add(current.id)
        for symbol in alphabet:
            next_nfa_states = move(current.nfa_states, symbol)
            if not next_nfa_states:
                continue
            next_closure = epsilon_closure_set(next_nfa_states)
            next_dfa = dfa.add_state(next_closure)
            current.transitions[symbol] = next_dfa
            if next_dfa.id not in processed and next_dfa not in unmarked:
                unmarked.append(next_dfa)
    return dfa

def print_dfa(dfa):
    print("DFA States and Transitions:")
    for state in dfa.states:
        start_mark = " (Start)" if state == dfa.start else ""
        accept_mark = " (Accept)" if state.is_accept else ""
        nfa_ids = sorted(str(s.id) for s in state.nfa_states)
        print(f"State {state.id}{start_mark}{accept_mark} [{','.join(nfa_ids)}]")
        for sym in sorted(dfa.alphabet):
            if sym in state.transitions:
                target = state.transitions[sym]
                print(f"  {sym} -> State {target.id}")

def simulate_dfa(dfa, input_string):
    current = dfa.start
    for symbol in input_string:
        if symbol not in current.transitions:
            return False
        current = current.transitions[symbol]
    return current.is_accept

