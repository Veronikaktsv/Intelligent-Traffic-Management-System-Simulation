import random
import time

class Agent:
    def __init__(self, agent_type):
        self.agent_type = agent_type

class Transport(Agent):
    def __init__(self):
        super().__init__('Transport')
        self.speed = random.uniform(20, 60)  

class Walker(Agent):
    def __init__(self):
        super().__init__('Walker')

class PedestrianLight(Agent):
    def __init__(self):
        super().__init__('PedestrianLight')
        self.state = 'Green'

class VehicleSystem:
    def __init__(self, approach):
        self.approach = approach
        self.emergency_response_time = 0
        self.agents = []
        self.congestion_occurrence = 0

    def model_traffic(self):
        for _ in range(1000): 
            self.spawn_agents()
            self.manage_traffic()
            self.manage_emergency()
            time.sleep(0.1)  

    def spawn_agents(self):
        
        if random.random() < 0.01:  
            agent_type = random.choice(['Transport', 'Walker', 'PedestrianLight'])
            new_agent = globals()[agent_type]()
            self.agents.append(new_agent)

    def manage_traffic(self):
        
        if self.approach == 'MAS':
            self.manage_mas_traffic()
        elif self.approach == 'Baseline':
            self.manage_baseline_traffic()

    def manage_emergency(self):
        
        if random.random() < 0.005:  
            start_time = time.time()
            response_time = self.manage_emergency_response()
            end_time = time.time()
            self.emergency_response_time += response_time

    def manage_mas_traffic(self):
       
        for agent in self.agents:
            if isinstance(agent, Transport):
                agent.speed = self.adaptive_speed_control(agent)


    def adaptive_speed_control(self, Transport):

        base_speed = random.uniform(20, 60)
        if self.has_right_of_way(Transport):
            return base_speed
        else:
            return max(base_speed - random.uniform(0, 10), 20)

    def has_right_of_way(self, Transport):
        return random.choice([True, False])


    def manage_baseline_traffic(self):
        
        for agent in self.agents:
            if isinstance(agent, Transport):
                agent.speed = max(agent.speed - random.uniform(0, 5), 20)  

    def manage_emergency_response(self):
        
        return random.uniform(1, 5)  


def run_model(approach):
    traffic_system = VehicleSystem(approach)
    traffic_system.model_traffic()
    return traffic_system.emergency_response_time, traffic_system.congestion_occurrence

if __name__ == "__main__":
    mas_response_time, mas_congestion = run_model('MAS')
    baseline_response_time, baseline_congestion = run_model('Baseline')

    print(f"MAS Emergency Response Time: {mas_response_time:.2f} seconds")
    print(f"MAS Congestion Occurrence: {mas_congestion} times")

    print(f"Baseline Emergency Response Time: {baseline_response_time:.2f} seconds")
    print(f"Baseline Congestion Occurrence: {baseline_congestion} times")

    
