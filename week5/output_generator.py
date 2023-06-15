#!/usr/bin/env python3

from common import format_tour, read_input

import solver_kruskal


CHALLENGES = 7


def generate_output():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        
        tour = solver_kruskal.solve(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_output()
