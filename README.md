# Collatz_Scribbles

# WELCOME TO COLLATZ SCRIBBLES
A site where one can explore the math magic of Collatz Conjecture and explore the collatz sequence for any number between(1-10000)
## Collatz Conjecture 
It states that any positive number would end up as 1 if the following operations are repeatedly applied:

if number is odd then do 3*(number)+1
if number is even then do (number)/2

This is one of the most notorious unsolved problem in mathematics which looks simple but is deceiving


This repository contains code for the site Collatz_Scribbles based on Collatz Sequence Generation for any number between(1-10000) based on Collatz Conjecture 

The code involves the following main files:
index.html - (Interface/landing page) Generated through BOLT AI by constructing a highly specialised prompt based on self thought design through claude
Collatz.py-Self written code to compute collatz sequence for graph nodes that would be displayed for input number
Graph_Structure.py-Self written code to compute exact positions of graph nodes for accurate collatz graph representation and accurate positioning of edges
Collatz_Sequence_Graph.py- Self written code along with some help from claude for node,edges and graph design based on nodes and edges as well as code for generating graph html file for display on site from above Collatz.py and Graph_Structure.py
app.py-Backend code to serve the generated graph html file on the site

### Main Packages used:
pyvis
networkx
flask

