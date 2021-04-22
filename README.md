# Google OR - Indivisual study

OR-Tools is an open source software suite for optimization, tuned for tackling the world's toughest problems. Will be learning how to implement the OR-Tools provided by google to solve some of the complex problems.

## Installation 
- Python 3.9 is recomended.
- Installation of ortools library using pipenv 
    - ` pipenv install ortools ` 

- Activate the virtual environment 
    - ` pipenv shell `

## 1.GLOP Solver
GLOP linear computational optimization problems are solved using the Google OR-Tools linear optimization solver.
Let us understand from the below example.

- #### linear.py 
  Here's the solution to a sample example of a linear programming problem from google developers website.

  - **Problem Statement**<br />
    Maximize 3x + 4y subject to the following constraints:<br />
    x + 2y	≤	14<br />
    3x – y	≥	0<br />
    x – y	≤	2<br />

  - ##### Execution
    `python linear.py `

## 2.Routing Solver
Here we are trying to solve **Traveling Salesman Problem** using the Google OR-Tools routing model.
Let us understand from the below example.

- ##### routing.py 
  Here's the solution for the traveling salesman problem from google developers website.

  - **Poblem Statement**<br />
    The senario is to find out the minimum cost and path travelled between these cities, such a way that it begins and ends from the same city.<br />
  - **Given** <br />
    '''0. New York - 1. Los Angeles - 2. Chicago - 3. Minneapolis - 4. Denver - 5. Dallas - 6. Seattle - 7. Boston - 8. San Francisco - 9. St. Louis - 10. Houston - 11. Phoenix - 12. Salt Lake City''' <br />

  - ##### Execution
    `python routing.py`

- ##### routing_prob1.py
  - **Problem Statement**<br />

- ##### routing/pickup-capacity.py
  Here's the solution for the pickup with capacity constraint for 4 delivery trucks from google developers website.

  - **Poblem Statement**<br />
    The senario is to find out the path travelled between these given nodes by the 4 delivery truck to pickup the load at each node with capacity contraint of 15.<br />
  - **Given** <br />
    `data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data['vehicle_capacities'] = [15, 15, 15, 15]` <br />

  - ##### Execution
    `python pickup-capacity.py`

- ##### routing/pickup-delivery.py 
  Here's the solution for the pickup delivery from google developers website.

  - **Poblem Statement**<br />
    The senario is to find out the initial solution from the routes and then performs a search starting at the initial solution. The program displays both the initial solution, and the solution found by the search<br />
  - **Given** <br />
    '  data['initial_routes'] = [
        [8, 16, 14, 13, 12, 11],
        [3, 4, 9, 10],
        [15, 1],
        [7, 5, 2, 6],
    ]' <br />

  - ##### Execution
    `python routing.py`


## 3.Scheduling Solver
Here we are trying to solve shift scheduling using the Google OR-Tools scheduling model.
Let us understand from the below example.

- ##### scheduling.py
  Here's the solution for the shift scheduling of the four nurses over a three-day period, subject to the following conditions:<br />
  - **Poblem Statement**<br />
    - Each day is divided into three 8-hour shifts.
    - Every day, each shift is assigned to a single nurse, and no nurse works more than one shift.
    - Each nurse is assigned to at least two shifts during the three-day period.
  
  - ##### Execution
    `python scheduling.py`

## 4. Pickup Routing Solver
Here we are trying to solve capacitated vehicle routing problem (CVRP) is a VRP in which vehicles with limited carrying capacity need to pick up or deliver items at various locations..
Let us understand from the below example.

- ##### pickup/pickup-capacity.py
  Here's the solution for the capacitated vehicle routing problem based on the demand and vechilce capacity:<br />
  - **Given** <br />
    - Demands: Each location has a demand corresponding to the quantity—for example, weight or volume—of the item to be picked up.
    - Capacities: Each vehicle has a capacity: the maximum quantity that the vehicle can hold. As a vehicle travels along its route, the total quantity of the items   it is carrying can never exceed its capacity.

  - ##### Execution
    `python pickup-capacity.py`

- ##### pickup/pickup-delivery.py
  Here's the solution for the VRP in which each vehicle picks up items at various locations and drops them off at others.<br />
  - **Given** <br />
    - pickup location
    - deliverable load capicity 

  - ##### Execution
    `python pickup-delivery.py`










