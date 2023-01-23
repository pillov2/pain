# Lecture 6 Notes

## Closure Properties of Regular Sets

### Theorem: If a language $A$ is regular, then ~$A = \Sigma^* /\ A$ is also regular

> ### Proof:
>  
> $A$ is regular, so let:
>  
> $M = (Q, \Sigma, \delta, s, F)$ be a DFA such that $L(M) \text{ (the language of M)} = A$
>  
> Now consider:
>  
> $M' = (Q, \Sigma, \delta, s, Q / F)$
>  
> We claim that $L(M') = $~$A$ and therefore ~$A$ is regular:
>  
> $x \in L(M') \Leftrightarrow \hat{\delta}(s, x) \in Q / F \Leftrightarrow \hat{\delta}(s, x) \notin F \Leftrightarrow x \notin L(M) \Leftrightarrow x \in $ ~$A$ where we use the fact that $\hat{\delta}$ of the two machines is the same

### Theorem: If $A$ and $B$ are regular sets, then $A \cap B$ is also regular

> ### Example:
>  
> $A = \{x \in \{a, b, c \}^* | \#a(x) = 1 \}$  
> $B = \{x \in \{a, b, c \}^* | \#b(x) = 1 \}$  
>  
> Find a DFA for $A \cap B$:
>  
> More general approach to reuse DFA's for $A$ and $B$

About the theorem:  
$A = L(M_1) \text{ where } M_1(Q_1, \Sigma, \delta_1, s_1, F_1)$  
$B = L(M_2) \text{ where } M_2(Q_2, \Sigma, \delta_2, s_2, F_2)$ 

Let $M_3 = (Q_1 \text{ x } Q_2, \Sigma, \delta_3, (s_1, s_2), F_1, \text{ x } F_2)$ where $\delta_3((P, q), a) = (\delta_1 (P, a), \delta_2(q, a))$

Claim: $L(M_3) = A \cap B$

> ### Back to our example: 


i want to go home :(