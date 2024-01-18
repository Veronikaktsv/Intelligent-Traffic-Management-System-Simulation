# Intelligent-Traffic-Management-System-Simulation
## Overview
The research article "Enhancing Traffic Management through Multi-Agent Systems and Coordination Mechanisms" by Veronika Katsevych provides a Python implementation of an intelligent traffic management system simulation. Using a Multi-Agent System (MAS) technique, the model represents the cooperation of many traffic agents, such as autonomous cars, pedestrians, and traffic lights.

## Implementation
The code is organized into classes, such as Transport, Walker, and PedestrianLight, that represent multiple kinds of traffic agents. The modeling process is managed by the VehicleSystem class, which combines baseline and MAS techniques. Since the baseline method enforces specified speed reductions, the MAS traffic managing mechanism dynamically modifies vehicle speeds.

## How to Run
Use the run_model function in the main script and pass in the approach ('MAS' or 'Baseline') as an argument to start the modeling process.  The model executes for a certain amount of time steps, and the console prints results, which include congestion occurrences and emergency response times.

## Dependencies
Python 3 is required for the model to operate.  

## Testing
A testing in the code verifies that the provided model is functioning. Unit tests encompass a wide range of scenarios, such as emergency situations, agent interactions, and diverse traffic circumstances. The traffic simulation's accuracy and dependability are guaranteed by the testing procedure.

##
This project is licensed under the License MIT - see the LICENSE file for details.
