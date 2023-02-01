# Lecture 9 Notes

> Example: $A = \{x \in \{a, b\}^* | \text{ second right most symbol of } x \text{ is } a\}$  
> - $\hat{\Delta} (\{q_0\}, a) = \{q_0, q_1\}$  
> - $\hat{\Delta} (\{q_0\}, ab) = \{q_0, q_2\}$
> - $\hat{\Delta} (\{q_0\}, abbb) = \{q_0\}$  
> - $\hat{\Delta} (\{q_0, q_1\}, b) = \{q_0, q_2\}$
> - $\hat{\Delta} (\{\}, ab) = \{\}$
> - $\hat{\Delta} (\{q_0\}, a) = \{q_0, q_1\}$


The subset construction game for creating DFAs out of NFAs

### Theorem: if $A = L(N)$ for some NFA N, then A is regular

Assume $N = Q_n, \Sigma, \Delta_N, S_N, F_N$,  
Then take $M = Q_M, \Sigma, \delta_M, s_M, F_M$  
where:
- $Q_M = 2^{Q_N}$
- $\delta_M(A, x) = \hat{\Delta}$

Example: 
