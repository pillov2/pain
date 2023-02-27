# Lecture 14 Notes

We want to find a regular expression corresponding to a given NFA $N.

$N = N(Q, \Sigma, \Delta, S, F)$ where:  
&emsp;&emsp; $\Delta: Q \times \Sigma \rightarrow 2^Q$  
&emsp;&emsp; $\hat{\Delta}: 2^Q \times \Sigma^* \rightarrow 2^Q$  
&emsp;&emsp; $\hat{\Delta}(A, \epsilon) = A$  
&emsp;&emsp; $\hat{\Delta}(A, xA) = \bigcup_{q \in \hat{\delta}(A, x)}\Delta(q, a)$  

1. How can we find a regular expression $\alpha_{u, v}^R$ such that $L(\alpha_{u, v}^R = A$?
2. Given these regular expressions, how can we give a regular expression $\alpha$ for $N$ (i.e., $L(\alpha) = L(N)$)?

### Let's start with Q2:

First, we assume that there is only one start and one accept state in $N (S = \{s\}, F= \{f\})$ Then:

$\bigcup_{R \in 2^Q} \alpha_{s, f}^R \leftarrow$ initial answer  \
\
$\alpha_{s, f}^Q \leftarrow$ all states in between $s$ and $f$

What if $S = \{s_1, s_2,...,s_m\}$  
&emsp;&emsp;&emsp;&nbsp;$F = \{f_1, f_2,...,f_m\}?$ 

$\alpha_{s_1,f_1}^Q + \alpha_{s1, f2}^Q + ... + \alpha_{s_1, f_n}^Q +$  
$\alpha_{s_2,f_1}^Q + \alpha_{s2, f2}^Q + ... + \alpha_{s_2, f_n}^Q + \alpha_{s_n, f_n}^Q $  
$= \bigcup_{i \in \{1,...n\}, j \in \{1,...n\}} \alpha_{s_i, f_i}^Q$ (big plus instead of big U)

### What about Q1?

Let $a_1, a_2,...a_k$ be those symbols that $v \in \Delta(u, a_i).$  

$\alpha_{u, v}^\emptyset = 
\begin{cases} 
      \epsilon \hspace{45mm} u = v, k = 0\\
      \emptyset \hspace{45mm} u \neq v, k = 0 \\
      a_1+ a_2 + ... + a_k + \epsilon \hspace{15mm} u = v, k > 0\\
      a_1+ a_2 + ... + a_k \hspace{21mm} u \neq v, k > 0
 \end{cases}$

For $\alpha_{u, v}^R$, consider an arbitrary state $q \in R$. We divide strings in $L(\alpha_{u, v}^R)$ into those that "need to pass through $a$" or those that don't.

$\alpha_{u, v}^R = \alpha_{u, v}^{R - \{q\}} + \alpha_{u, q}^R R_{q, v}^R \leftarrow$ it works but we now have to compute it, which is difficult because we did not simplify R

$\alpha_{u, v}^R = \alpha_{u, v}^{R - \{q\}} + \alpha_{u, q}^{R - \{q\}} (\alpha_{q, q}^{R - \{q\}}) \alpha_{q, v}^R \leftarrow$ another answer

