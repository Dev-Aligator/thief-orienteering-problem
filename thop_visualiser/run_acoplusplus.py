import os
import ast
import glob
from utils import extract_file_name
def run_acoplusplus(thop_input_file):
    solution_exist, solution_path = search_for_solution(thop_input_file)
    log_file_path = search_for_log(thop_input_file)
    if not solution_exist:
        os.system("../acoplusplus_thop/src/aco++/acothop --mmas --tries 1 --inputfile " + thop_input_file + " --outputfile output.thop.sol --log")
    with open(solution_path, "r") as file:
        thief_route_solution = file.readline()
        thief_route_solution = ast.literal_eval(thief_route_solution)

        thief_packing_plan = file.readline()
        thief_packing_plan = ast.literal_eval(thief_packing_plan)

    log_solution = []
    with open(log_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "found at iteration" in line:
                log_stats = line.strip().split(",")
                for _stat in log_stats:
                    stat = float(_stat.split(" ")[-1])
                    if stat.is_integer():
                        log_solution.append(int(stat))
                    else:
                        log_solution.append(float(_stat.split(" ")[-1]))
                break
    return thief_route_solution, thief_packing_plan, log_solution

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
    return False, "output.thop.sol"

def search_for_log(thop_file_path):
    thop_file_name = extract_file_name(thop_file_path)
    instance_name = thop_file_name.split(".")[0]
    instance_type = instance_name.split("_")[0] + "-thop"
    search_dir = os.getcwd() + "/../acoplusplus_thop/solutions/aco++/" + instance_type
    for file in glob.glob(search_dir + "/*.thop.sol.log"):
        log_instance_filename = extract_file_name(file)
        log_instance_name_split = log_instance_filename.split("_")
        log_instance_name = "_".join(log_instance_name_split[0:5])
    
        if instance_name == log_instance_name:
            return file
    return "output.thop.sol.log"


# run_acoplusplus("/home/aligator/Repositories/Thief-Orienteering-Problem-ThOP/acoplusplus_thop/instances/a280-thop/a280_01_bsc_01_01.thop")