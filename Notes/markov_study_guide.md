


In simpler terms, a Markov process is a process for
which one can make predictions for its future 
based solely on its present state just as 
well as one could knowing the process's full history.

A markov chain data is a map of <State1, State[n]> 

the chain itself is [Staten1, Staten2]

the tranition for chain links is determined by the probability staten1 turns into staten2

this probability is determined by proximity? random? 


chain just ends on . or determined length


DAY TWO:

Understand - The chain is three parts. s

One part is the "chain" which is collection of elements from the text, initally empty. This is the output. 
The next part is the vocab, or starting states. This is the list of states our chain head can be. 
The final part is the map, or which state transitions are allowed
optionally, i have created a probability distribution shadow of the map, 
in order to determine the likelyhood of certain transitions over others.
