Disaster Response & Relief Coordination System
==============================================

### **DCIT 403: Designing Intelligent Agent Labs**

1\. Project Overview
--------------------

This project implements a decentralized multi-agent system (MAS) designed to coordinate emergency response operations during disasters like floods, fires, or earthquakes. The system focuses on distributed decision-making and resilience where centralized control is unavailable.

+2

### **Core Agent Types**

*   **SensorAgent**: Detects disaster events and reports environmental conditions.
    
*   **CoordinatorAgent**: Assigns tasks, sets priorities, and coordinates agent activities.
    
*   **RescueAgent**: Executes rescue operations based on assigned tasks.
    
*   **LogisticsAgent**: Manages supplies and relief items.
    

2\. Technical Stack
-------------------

*   **Language**: Python 3.9+.+1
    
*   **Framework**: SPADE (Smart Python Agent Development Environment).+1
    
*   **Communication**: XMPP (Extensible Messaging and Presence Protocol) using the FIPA-ACL standard.+1
    
*   **Environment**: GitHub Codespaces.+1
    

3\. Laboratory Progression (1–4)
--------------------------------

### **Lab 1: Environment & Platform Setup**

*   **Focus**: Establishing infrastructure and verifying connectivity.
    
*   **Outcome**: Deployment of a basic SPADE agent capable of authenticating with an XMPP server.
    

### **Lab 2: Perception & Environment Modeling**

*   **Focus**: Implementing agent sensing capabilities.
    
*   **Outcome**: The SensorAgent periodically monitors the environment and logs "percepts" such as disaster types and damage severity levels.
    

### **Lab 3: Reactive Behavior (FSM)**

*   **Focus**: Modeling goals and event-triggered behaviors.
    
*   **Outcome**: Implementation of a **Finite State Machine (FSM)** that allows agents to switch states (e.g., from _Monitoring_ to _Alert_) based on sensor reports.
    

### **Lab 4: Inter-Agent Communication**

*   **Focus**: Enabling standardized message exchange using FIPA-ACL.
    
*   **Outcome**: A coordinated 3-agent chain where the SensorAgent informs the Coordinator, who then requests action from the RescueAgent.
    

4\. How to Run
--------------

1.  **Start XMPP Server**: Ensure your server (local or remote like xmpp.jp) is active.
    
2.  Bashpip install spade
    
3.  Bashpython lab4.py
    