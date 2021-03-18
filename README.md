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

## 3.Scheduling Solver
Here we are trying to solve shift scheduling using the Google OR-Tools scheduling model.
Let us understand from the below example.

- ##### scheduling.py
  Here's the solution for the shift scheduling of the four nurses over a three-day period, subject to the following conditions:<br />

    - Each day is divided into three 8-hour shifts.
    - Every day, each shift is assigned to a single nurse, and no nurse works more than one shift.
    - Each nurse is assigned to at least two shifts during the three-day period.






