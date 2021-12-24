# Credit-Card-Validator-using-Luhn-Algorithm

An algorithm to validate a credit card number

### Luhn's Algorithm
Luhn Algorithm, or Modulus 10 Algorithm, is a mathematical formula that helps to determine whether or not a correct identification number has been provided.The Luhn algorithm helps to validate identification numbers, which explains why it’s widely used in electronic payment systems, most notably credit cards.Due to its ability to rapidly identify wrong card numbers, the algorithm typically speeds up electronic payment processing.

### How the Algorithm works
1. Find the sum of odd index values of the credit card.
2. Find the number of even numbers.
3. Calculate the double of even numbers.
4. Find sum of even numbers.
5. Find sum of odd and even numbers if add up to the multiples of 10 then the 
credit card is valid

### Limitations of the Luhn Algorithm
One major limitation is that the Luhn Algorithm can only detect single digit errors, including transpositions of adjacent numbers.What this means is, in the case of a 0 – 9 digit set, transpositions of the ‘09’ to ‘90’ or vice versa won’t be detected by the Luhn Algorithm.
