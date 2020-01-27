# Salesken_Assignment
Problem Statement - 1: Matching the misspelt cities.
------------------------------------------------------
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


Problem Statement - 2: Find the Semantic Similarity
-----------------------------------------------------
Part - 1: Given a list of sentences (list_of_setences.txt) write an algorithm which computes the semantic similarity and return the similar sentences together.

Semantic similarity is a metric defined over a set of documents or terms, where the idea of distance between them is based on the likeness of their meaning or semantic content.

For example : "Football is played in Brazil" and "Cricket is played in India". Both these sentences are about sports so they will have a semantic similarity.

Part - 2: Extend the above algorithm in form of a REST API. The input parameter is a list of sentences (refer to the file list_of_setences.txt) and the response is a list of list with the similar sentences.

For example : Say there are 4 sentences as an input list - ["Football is played in Brazil" , "Cricket is played in India", "Traveling is good for health", "People love traveling in winter"]

Output : [["Football is played in Brazil" , "Cricket is played in India"], ["Traveling is good for health", "People love traveling in winter"]]

Implementation:
---------------
1) I used Dandelion API to get the similarity between the the sentences. If the similarity is more than 30% then I am showing those sentences.

