import math
import numpy as np
import torch


def a_identity(state):
    return state


def a_inf(state):
    return 1e5, 1e5


def a_subtract(state):
    return state[0], state[1] - state[0]


def a_mod(state):
    if state[0] == 0:
        return state[0], state[1]
    return state[0], state[1] % state[0]

def a_swp(state):
    return state[1], state[0]


def a_plsy(state, device="cpu"):
    return state @ torch.tensor([[1, 1], [0, 1]],dtype=torch.float).to(device)


def a_suby(state, device="cpu"):
    return state @ torch.tensor([[1, -1], [0, 1]],dtype=torch.float).to(device)


def a_plsx(state, device="cpu"):
    return state @ torch.tensor([[1, 0], [1, 1]],dtype=torch.float).to(device)


def a_subx(state, device="cpu"):
    return state @ torch.tensor([[1, 0], [-1, 1]],dtype=torch.float).to(device)


def UCT_fn(child, C):
    if child.visits == 0:
        return math.inf
    return child.subtree_value + 2 * C * math.sqrt(2 * math.log2(child.parent.visits) / child.visits)
