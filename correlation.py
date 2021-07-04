# Add the functions in this file
import ast
from math import sqrt

import json
from typing import Tuple

def load_journal(fname):
    f = open(fname, 'r')
    text = f.read()
    return json.loads(text)

def compute_phi(fname, event):
    journal = load_journal(fname)
    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0
    t = 0
    s = 0
    n = len(journal)
    for j in journal:

        if j['squirrel'] == True:
            s = s + 1

        if event in j['events']:
            t = t+1
            if j['squirrel'] == True:
                n3 = n3 + 1
            else:
                n1 = n1 + 1
        else:
            if j['squirrel'] == False:
                n0 = n0 + 1
            else:
                n2 = n2 + 1

    phi = (n3 * n0 - n1 * n2)/sqrt(s * (n - s) * t * (n - t))

    return phi


def compute_correlations(fname):
    journal = load_journal(fname)
    l = []

    [l.append(event) for j in journal for event in j['events'] if event not in l]

    d = {event : compute_phi(fname, event) for event in l}
    
    return d

def diagnose(fname):
    d = compute_correlations(fname)

    d = sorted(d.items(), key = lambda x: x[1], reverse = True)

    return (d[0][0], d[-1][0])



        