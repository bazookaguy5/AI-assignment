# input for header
M, N, T = map(int, input().split(' '))

input() # to remove spaceing

# input for state space
state_space = []
for i in range(M):
    state_space.append(tuple(input()[1:-1].split(", ")))

input() # to remove spaceing

# input for rules
rules = []
for i in range(N):
    rules.append(input())

input() # to remove spaceing

# input for transition table
transition_table = []
for i in range(M):
    transition_table.append(list(map(int, input().split(' '))))

input() # to remove spaceing

# input for test cases
test_cases = []
for i in range(T):
    temp = input().split("\t")
    test_cases.append({
        'start': state_space.index(tuple(temp[0][1:-1].split(", "))),
        'end': state_space.index(tuple(temp[1][1:-1].split(", ")))
        })


def print_result(states):
    actions = []

    for i in range(len(states)-1):
        for j in range(N):
            if transition_table[states[i]][j] == states[i+1]:
                actions.append(rules[j])
                break
    print("->".join(actions))

# Actual algorithm
for test_case in test_cases:
    visited = []
    frontier = []
    frontier.append((test_case['start'],))
    visited.append(test_case['start'])

    while (len(frontier) != 0):
        state = frontier.pop(0)
        if (state[-1] == test_case['end']):
            print_result(state)
            break
        else:
            for next_state in transition_table[state[-1]]:
                if next_state not in visited:
                    frontier.append(state + (next_state,))
                    visited.append(next_state)
