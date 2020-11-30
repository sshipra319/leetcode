# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:05:01 2020

@author: leosh
"""

def maxEvents(arrival, duration):
    events = [0]
    arr_sorted, dur_sorted = zip(*sorted(zip(arrival, duration)))
    for i in range(len(arrival)-1):
        if arr_sorted[events[-1]]+dur_sorted[events[-1]] <= arr_sorted[i+1]:
            events.append(i+1)
        elif arr_sorted[events[-1]]+dur_sorted[events[-1]] >= arr_sorted[i+1]+dur_sorted[i+1]:
            events.pop()
            events.append(i+1)

    return len(events)

arrival = [1,3,5]
duration = [2,2,2]
print(maxEvents(arrival, duration))

    