from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import os


# environment_type can be 'lessthan30' or 'morethan30'
environment_type = "lessthan30"
#environment_num can be in range from 1 to 50 
environment_num = 1
#method can be choosed from ['my_method','my_method_pathplan','constantly_soft','constantly_soft_pathplan','distribute','distribute_pathplan','motorized_joint','motorized_joint_pathplan'], # Here my_method means MRS-CWC with TDT
method = 'constantly_soft_pathplan'

client = RemoteAPIClient()
sim = client.require('sim')
start = 0
sim.setStepping(True)
meth = method
    
script_dir = os.path.dirname(os.path.abspath(__file__)) 
scenePath = os.path.join(script_dir, "coppeliasim_based_benchmark", f"{meth}.ttt")
sim.setStringSignal("method", meth)
env = environment_type
sim.setStringSignal("environment", env)

j = environment_num
sim.setStringSignal("terrain_number", j)
sim.loadScene(scenePath)
time.sleep(1.5) 
sim.startSimulation()
while True:
    sim.step()
    simState = sim.getSimulationState()
    if simState == sim.simulation_paused:
        break
    #time.sleep(0.1)  
print(f"Simulation about {env},{meth},terrain number{j} is done.")    
sim.stopSimulation()
