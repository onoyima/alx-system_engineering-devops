Enhanced Scalability in Web Infrastructure
3-scale_up.png

Description
This upgraded web infrastructure represents a scaled-up version of the previously described architecture, aiming to eliminate single points of failure (SPOFs) and enhance scalability. Each major component - web server, application server, and database server - now resides on separate GNU/Linux servers. Additionally, SSL protection is implemented without termination at the load balancer, and each server's network is fortified with a firewall, accompanied by comprehensive monitoring.

Specifics of the Infrastructure
Firewall Implementation Between Servers: Introducing firewalls between each server fortifies individual servers against unauthorized access, enhancing network security across the infrastructure.
Issues with the Infrastructure
High Maintenance Costs: While the removal of SPOFs and the distribution of components across separate servers enhance reliability and scalability, this scalability comes at a cost. Maintaining multiple servers incurs expenses related to hardware procurement, electricity consumption, and ongoing maintenance. Consequently, increased financial resources are required for server acquisition, operational expenses, and electricity consumption, potentially impacting the company's budget.