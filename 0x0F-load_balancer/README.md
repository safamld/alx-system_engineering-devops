Load balancer
HAProxy Terminology
There are many terms and concepts that are important when discussing load balancing and proxying. You’ll go over commonly used terms in the following subsections.

Before you get into the basic types of load balancing, you should begin with a review of ACLs, backends, and frontends.

Access Control List (ACL)
In relation to load balancing, ACLs are used to test some condition and perform an action (e.g. select a server, or block a request) based on the test result. Use of ACLs allows flexible network traffic forwarding based on a variety of factors like pattern-matching and the number of connections to a backend, for example.

Example of an ACL:

acl url_blog path_beg /blog
This ACL is matched if the path of a user’s request begins with /blog. This would match a request of http://yourdomain.com/blog/blog-entry-1, for example.

For a detailed guide on ACL usage, check out the HAProxy Configuration Manual.

Backend
A backend is a set of servers that receives forwarded requests. Backends are defined in the backend section of the HAProxy configuration. In its most basic form, a backend can be defined by:

which load balance algorithm to use
a list of servers and ports
A backend can contain one or many servers in it. Generally speaking, adding more servers to your backend will increase your potential load capacity by spreading the load over multiple servers. Increased reliability is also achieved through this manner, in case some of your backend servers become unavailable.

Here is an example of a two backend configuration, web-backend and blog-backend with two web servers in each, listening on port 80:

backend web-backend
   balance roundrobin
   server web1 web1.yourdomain.com:80 check
   server web2 web2.yourdomain.com:80 check
   
backend blog-backend
   balance roundrobin
   mode http
   server blog1 blog1.yourdomain.com:80 check
   server blog1 blog1.yourdomain.com:80 check
balance roundrobin line specifies the load balancing algorithm, which is detailed in the Load Balancing Algorithms section.

mode http specifies that layer 7 proxying will be used, which is explained in the Types of Load Balancing section.

The check option at the end of the server directives specifies that health checks should be performed on those backend servers.

Frontend
A frontend defines how requests should be forwarded to backends. Frontends are defined in the frontend section of the HAProxy configuration. Their definitions are composed of the following components:

a set of IP addresses and a port (e.g. 10.1.1.7:80, *:443, etc.)
ACLs
use_backend rules, which define which backends to use depending on which ACL conditions are matched, and/or a default_backend rule that handles every other case
