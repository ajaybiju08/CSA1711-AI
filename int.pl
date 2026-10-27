sum_to(0,0).

sum_to(N, Sum):-
N>0,
N1 is N-1,
sum_to(N1, PartialSum), 
Sum is N + PartialSum.  