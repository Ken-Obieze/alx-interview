#!/usr/bin/python3
"""Module for boxUnlock puzzle."""


def canUnlockAll(boxes):
    """Check if all box can be opened."""
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return (len(unlocked) == len(boxes))
