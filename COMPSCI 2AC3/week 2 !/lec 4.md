# Lecture 4 Notes

Quiz:  
> $A(B \cup C) = AB \cup AC$ 
> - induction 
> - $AB \cup AC \subseteq A(B \cup C) \subseteq AB \cup AC$

> $A(B \cap C) = AB \cap AC$
> - $A = \{a, aa\}, B = \{b\}, C = \{ab\}$

## Finite State Automata

A finite state machine (automaton) has a finite number of **states**

The machine is initialized in a certain state, and "consumes" a sequence of characters one by one

The state **gets updated** after consuming each symbol based on the **current state** and the consumed symbol

Once the whole inputted string is consumed, the machine terminates and accepts/rejects the string based on the final state

> $A = \{x \in \{a, b\}^* | \#a(x) = 1 \}$  
> INSERT IMAGE THAT I DID NOT DRAW  
> $q_0, q_1, q_2$ : are all states  
> initial state: ($q_0$) is represented by the arrow at the beginning of the diagram  
> $q_1$ "we have consumed one a"  
> accepted states: $\{q_1\}$
>  
> Example:  
> x = abbabb  
> ADD STATE TRANSITION IMAGES

## Deterministic Finite Automaton (DFA)

A DFA is a structure $M = (Q, \Sigma, \delta, s, F)$ where:
- $Q$ : set of states
- $\Sigma$ : Alphabet
- $\delta$ : $Q$ x $\Sigma \rightarrow Q$ : transition function
    - "what will be the next state if we are in $q \in Q$ and consume some $a \in \Sigma$
- $s \in Q$ : start state
- $F \subseteq Q$ : set of accepted states

Informally: $M$ accepts string x if the final state after consuming x is an accepted state (otherwise it will reject it)

### Book Notation for DFA Diagrams

- uses dots to indicate states and circled dots to indicate final states

> Example: what does the following DFA do?  
> -- TODO ADD IMAGE  
> $A = \{x \in \{a, b\}^* : \#a(x) \text{ is odd}\}$  
>  
> But how do we prove this?  
> Sometimes it's impossible to prove (?? bro im so lost)

### Formal Definition of "What is Accepted by machine $M$"

Multi-step transition function: $\hat{\delta}$ : $Q$ x $\Sigma^* \rightarrow Q$ where $\hat{\delta}$ is defined by:
- $\forall q \in Q$ , $\hat{\delta} (q, \epsilon) \triangleq q$
- $\hat{\delta} (q, xa) \triangleq \delta (\hat{\delta}(q, x), a)$

Intuitively $\hat{\delta}$ tells us what will be the state we end up with if we start at some state and consume a string x

An input string x is accepted by $M = (Q, \Sigma, \delta, s, F)$ if and only if $\hat{\delta} (s, x) \in F$

Language corresponding to $M$:
- $L(M) = \{x \in \Sigma^* | \hat{\delta} \}$