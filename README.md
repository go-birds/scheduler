# scheduler
Script to help create a school schedule by assigning students to their classes in order to maximize overlap with their preferences. 

1. Load in a cost matrix like "upper_school_morning_C.csv". 
2. Use this to determine number of students (rows) and number of class choices (number of columns). 
3. Build standard constraints: all students must be assigned to exactly one class, each class has some capacity. 
4. Add custom constraints e.g., student 5 and student 6 cannot be in the same class ( x_[5,i] + x_[6,i] <= 1 for all i ).
5. Solve.
