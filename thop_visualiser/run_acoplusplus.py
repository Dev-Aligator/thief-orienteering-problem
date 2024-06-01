import os
import ast
def run_acoplusplus(thop_input_file):
    os.system("../acoplusplus_thop/src/aco++/acothop --mmas --tries 1 --inputfile " + thop_input_file + " --outputfile output.txt")
    with open("output.txt", "r") as file:
        thief_route_solution = file.readline()
        thief_route_solution = ast.literal_eval(thief_route_solution)
    return thief_route_solution