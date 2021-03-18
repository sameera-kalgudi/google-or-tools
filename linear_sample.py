from ortools.linear_solver import pywraplp


def main():

    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables x and y.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint, 2x1+ 3x2≤ 34
    ct = solver.Constraint(0, 34, 'ct')
    ct.SetCoefficient(x, 2)
    ct.SetCoefficient(y, 3)

    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function, 3x1+ 5x2≤ 54
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 5)
    objective.SetMaximization()

    solver.Solve()

    #printing solution
    print('Solution:')
    print('Objective value =', objective.Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())

    #advance usage
    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())



if __name__ == '__main__':
    main()