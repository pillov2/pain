# Lecture 8 Notes

>Example: Draw an NFA for $A = \{x \in \{a\}^* | \#a(x) \text{ mod } 3 = 1 \text{ or } \#a(x) \text{ mod } 7 = 1\}$

### Formal Definition of NFA

An NFA is a five tuple $N = (Q, \Sigma, \Delta, S, F)$ where:
- $Q$ - set of states
- $\Sigma$ - alphabet
- $\Delta$: transition function that goes from $Q$ x $\Sigma \rightarrow 2^Q$ 
    - $2^Q \triangleq$ all subsets of Q
    - $2^Q \triangleq$ the powerset of Q
    - $2^Q = \{ A \subseteq Q \}$
- $S \subseteq Q$- set of states
- $F \subseteq Q$ - set of accepted states

### Define $\hat{\Delta}: 2^Q$ x $\Sigma^* \rightarrow 2^Q$:  
> $\hat{\Delta} (A, \epsilon) = A$  
> $\hat{\Delta} (a, xa) = \bigcup_{q \in \hat{\Delta} (A,x)} \Delta (q, a)$  
>  
> Intuitively, $\hat{\Delta}(A, x)$ represents all the states that we can end up with by starting from some $q \in A$ and consuming $x$
>  
> *$N$ accepts a string $x$ if $F \cap \hat{\Delta} (S, x) \notin \emptyset$  
> *$L(N) = \{x \in \Sigma^* | F \cap \hat{\Delta} (S, x) \notin \emptyset \}$  

#### Theorem: $A$ is regular if and only if there is an NFA $N$ such that $L(N) = A$