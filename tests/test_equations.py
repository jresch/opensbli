#!/usr/bin/env python

import os
import pytest

# AutoFD functions
from autofd.problem import *
from autofd.equations import *

def test_expand():
    """ Ensure that an equation is expanded correctly. """

    mass = "Eq(Der(rho,t),- conser(rhou_j,x_j))"
    momentum = "Eq(Der(rhou_i,t) ,-conser(rhou_i*u_j + p* KroneckerDelta(_i,_j),x_j) + Der(tau_i_j,x_j) )"
    energy = "Eq(Der(rhoE,t),-conser((p+rhoE)*u_j,x_j) -Der(q_i,x_i) + Der(u_i*tau_i_j ,x_j) )"
    equations = [mass, momentum, energy]
    substitutions = []
    ndim = 3
    constants = ["c"]
    coordinate_symbol = ["x"]
    metrics = [False, False]
    formulas = ['Eq(u, 2*rho)']

    problem = Problem(equations, substitutions, ndim, constants, coordinate_symbol, metrics, formulas)

    expanded_equations, expanded_formulas = problem.expand()

    d = equations_to_dict([e.expandedeq[0] for e in expanded_equations])

    assert isinstance(d, dict)

    return

if __name__ == '__main__':
    pytest.main(os.path.abspath(__file__))
