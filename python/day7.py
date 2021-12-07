from scipy.optimize import minimize_scalar
import math

with open("day7.txt") as f:
    pos = [int(x) for x in f.read().split(",")]

def addup(k):
    return int((1 + k) * k /2)

def cost1(p):
    return sum([abs(x - p) for x in pos])

def cost2(p):
    return sum([addup(abs(x - p)) for x in pos])

k = minimize_scalar(cost1)
print(min(cost1(math.floor(k.x)), cost1(math.ceil(k.x))))
k = minimize_scalar(cost2)
print(min(cost2(math.floor(k.x)), cost2(math.ceil(k.x))))