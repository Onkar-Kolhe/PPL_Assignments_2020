details(toronto,'$50','60min').
details(paris,'$50','60min').
details(toulouse,'$40','30min').
details(london,'$75','80min').
details(barcelona,'$40','30min').
details(madrid,'$75','45min').

f(toronto,london,'Air Canada',500,'360min').
f(toronto,london,'United',450,'420min').
f(london,barcelona,'Iberia',220,'240min').
f(paris,toulouse,'United',35,'120min').
f(barcelona,madrid,'Air Canada',100,'60min').
f(barcelona,madrid,'Iberia',120,'65min').
f(toronto,madrid,'Air Canada',900,'480min').
f(toronto,madrid,'United',950,'540min').
f(toronto,madrid,'Iberia',800,'480min').

/*To list down all airports with their tax , security delay.*/
airport(A,B,C) :- details(A,B,C).

/* To check the availability of any flight from A to B. */
flight_check(A,B) :- f(A,B,_,_,_) ; f(B,A,_,_,_). 

/*To display all the available flights with their cost, duration, flight name.*/    
flight(A,B,C,D,E) :- f(A,B,C,D,E).

/*To check if there exist a cheap flight between city A and B.*/
cheap_flight(A,B,C,D,E) :- (f(A,B,C,D,E) ; f(B,A,C,D,E)) , D < 400.

/*To check if it is possible to reach from A to B in two flights.*/
two_flights(A,B) :- (f(A,X,_,_,_) ; f(X,A,_,_,_)) , (f(X,B,_,_,_) ; f(B,X,_,_,_)).

/*A flight from city A to city B with airline C is preferred if it’s cheap (see (b)) or it’s with Air Canada.*/
prefer(A,B,C,D,E) :- cheap_flight(A,B,C,D,E) ; ((flight(A,B,'Air Canada',F,_);flight(B,A,'Air Canada',F,_)) , (flight(A,B,C,D,E);flight(B,A,C,D,E)) , D < F).

/*If there exists a flight from A to B with 'United' then there exists a flight from A to B with 'Air Canada'.*/
e(A,B) :- (f(A,B,'United',_,_) ; f(B,A,'United',_,_)) , (f(A,B,'Air Canada',_,_) ; f(B,A,'Air Canada',_,_)).
