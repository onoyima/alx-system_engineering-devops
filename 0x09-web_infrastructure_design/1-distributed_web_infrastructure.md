Distributed Web Infrastructure Overview
1-distributed_web_infrastructure.PNG

Visit Board

Description
This distributed web infrastructure aims to alleviate traffic on the primary server by distributing workload to a replica server, managed by a load balancer.

Specifics of the Infrastructure
Load Balancer's Distribution Algorithm: The HAProxy load balancer employs the Round Robin distribution algorithm. This method cycles through servers based on their weights, ensuring equitable distribution of processing time. It allows dynamic adjustment of server weights.

Setup Enabled by Load Balancer: The HAProxy load balancer facilitates an Active-Passive setup instead of Active-Active. In an Active-Active setup, workloads are distributed across all nodes to prevent overload. Conversely, in Active-Passive, not all nodes are actively processing requests; the passive node becomes active if the preceding one fails.

Primary-Replica Database Cluster: This configures one server as the Primary and another as the Replica. The Primary handles read/write requests while the Replica handles only read requests. Data synchronization occurs when the Primary executes write operations.

Difference Between Primary and Replica Nodes: The Primary node manages write operations, while the Replica node handles read operations, reducing read traffic on the Primary.

Issues with the Infrastructure
Single Points of Failure (SPOF): Several components, including the Primary MySQL database server, the load balancer server, and the application server connecting to the primary database, pose risks of complete system failure if any one of them goes down.

Security Concerns: Data transmitted over the network lacks SSL encryption, exposing it to potential interception by hackers. Additionally, the absence of a firewall leaves servers vulnerable to unauthorized access.

Lack of Monitoring: Without server monitoring, there's no visibility into their status, hindering proactive maintenance and issue resolution.