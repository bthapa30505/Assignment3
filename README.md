# Assignment3
This repository contains the follwing files.
1) hash_table.py
   This python file contains the code implementation for  hash table using chaining for collision resolution.
2) randomized_quicksort.py
   This python file contains the code implementation for the randomized quick sort. 
3) report.pdf 
   This file contains the analysis of both randomized quicksort analysis as well as hash table analysis.
4) Readme.md
   This file gives the general overview about the contents of this repository and overall finding of the project

# Running the code
  In order the run the python programs, following steps need to be followed.
  1) Clone the github repository to your system.
  2) Open the project directory on your terminal.
  3) Run the program using following command:
     a) python3 hash_table.py
     b) python3 randomized_quicksort.py

# Overall Finding
  To sum up above two projects gave a very good understanding of the necessity of randomization in various types of algorithms. For the randomized quicksort, the overall run time of the sorting algorithm was decreased to O(n.logn) for some of the edge cases. We did the comparision between the runtime of deterministic vs randomized quicksort for two different sample size. This helped better understand how performance is big issue when data volume increased. 
  
  In the same way, we used a randomized hash function from a universal hash function to randomize the solution. This randomness helped to ensure that the keys are distributed more uniformly across buckets. Doing this also decreased the chances of worst-case collisions and improved performance on average.

