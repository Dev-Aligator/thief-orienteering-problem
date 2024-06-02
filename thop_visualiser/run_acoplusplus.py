import os
import ast
import glob
from utils import extract_file_name
def run_acoplusplus(thop_input_file):
    solution_exist, solution_path = search_for_solution(thop_input_file)
    if not solution_exist:
        os.system("../acoplusplus_thop/src/aco++/acothop --mmas --tries 1 --inputfile " + thop_input_file + " --outputfile output.txt")
    with open(solution_path, "r") as file:
        thief_route_solution = file.readline()
        thief_route_solution = ast.literal_eval(thief_route_solution)

        thief_packing_plan = file.readline()
        thief_packing_plan = ast.literal_eval(thief_packing_plan)
    return thief_route_solution, thief_packing_plan

def search_for_solution(thop_file_path):
    thop_file_name = extract_file_name(thop_file_path)
    instance_name = thop_file_name.split(".")[0]
    instance_type = instance_name.split("_")[0] + "-thop"
    search_dir = os.getcwd() + "/../acoplusplus_thop/solutions/aco++/" + instance_type
    for file in glob.glob(search_dir + "/*.thop.sol"):
        solution_instance_filename = extract_file_name(file)
        solution_instance_name_split = solution_instance_filename.split("_")
        solution_instance_name = "_".join(solution_instance_name_split[0:5])

        if instance_name == solution_instance_name:
            return True, file
    return False, "output.txt"
