"""
Parse collda file to json


pycollada
"""
import collada
import sys
import traceback
import numpy as np
from .daeloader import ColladaModel


def load_mixamodae_as_json(dae_f):
    col_model = ColladaModel(dae_f)

    

if __name__ == "__main__":
    load_mixamodae_as_json(sys.argv[1])
