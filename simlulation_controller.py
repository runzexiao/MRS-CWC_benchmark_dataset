from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import os

client = RemoteAPIClient()
sim = client.require('sim')
start = 0
sim.setStepping(True)
# environment = ['lessthan30','morethan30']
environment = ["morethan30"]
#method = ['my_method','my_method_pathplan','constantly_soft','constantly_soft_pathplan','distribute','distribute_pathplan','motorized_joint','motorized_joint_pathplan']
method = ['my_method']
for meth in method:
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    scenePath = os.path.join(script_dir, "coppeliasim_model", f"{meth}.ttt")
    sim.setStringSignal("method", meth)
    for env in environment:
        sim.setStringSignal("environment", env)
        for i in range(0,50):
            j = i + 1
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
       