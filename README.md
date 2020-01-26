# Salesken_Assignment
Problem Statement - 1: Matching the misspelt cities.
There are two data files (.csv)

Correct_cities.csv : This file consists of a list of cities and they are spelt correctly. It has three columns "name" which is a city name; "country" where the city belongs to and "id" which is a unique id for each city.

Misspelt_cities.csv : This file consists of city names which are mispelt. Each city name has been misspelt by randomly replacing 20% of the characters by some random characters. It has two columns "misspelt_name" and "country".

Question : Write an algorithm or a group of algorithms to match the misspelt city name with the correct city name and return the list of unique ids for each misspelt city name.

For example : Correct Data -> (Bangalore, India, 101) and say for "Bangalore" the misspelt name is (Banhakorg, India). Then the matching algorithm should return 101 for this example.

Implementation:
---------------
1)Found all city names with same length of misspelt word which belongs to same country.
2)I used edit_distance from nltk package to get the count of disimilar characters.
3)Found the correct word which has minimal number of disimilar characters in compare to misspelt word.
4)Get the City Id by city name from the correct city name.
