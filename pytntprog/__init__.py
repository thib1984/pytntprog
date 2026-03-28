"""
pytntprog init
"""


from pytntprog.args import compute_args
from pytntprog.pytntprog import find

def pytntprog():
    """
    pytntprog entry point
    """
    compute_args()
    find()
