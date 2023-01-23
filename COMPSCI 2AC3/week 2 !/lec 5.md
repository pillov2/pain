# Lecture 5 Notes

FOOD I NEED FOOD

GRR

help

:(

why are we here just to suffer

pain

Regular sets: A set $A \subseteq \Sigma^*$ is regular if there exists a DFA M such that $L(M) = A$
- $\{x \in \{a, b \}^*: \text{ the second to the last symbol is b}\}$ <- regular $\checkmark$
- $\{x \in \{a, b \}^*: \#a(x) = \#b(x)\}$ <- not regular

### How to prove that $L(M) = A$?

> ### Example:  
>   
> $A = \{x \in \{a, b\}^* : \#a(x) \text{ mod } 2 = 1\}$  
> $M = (\{q_0, q_1 \}, \{a, b \}, \delta, q_0, \{q_1 \})$  
>  
> Proof:   
> Define $f(x) = \#a(x) \text{ mod } 2$.  
> It is enough to show that: $\forall x \in \Sigma^*, x \in A \Leftrightarrow x \in L(M)$  
>  
> Observation:  
> It is enough to show $\forall x 'in \Sigma^*, \hat{\delta}(q_0, x) = q_{f(x)}$  
> $(x \in A \Leftrightarrow f(x) = 1 \Leftrightarrow \hat{\delta}(q_0, x) = q_1 \Leftrightarrow \hat{\delta}(q_0, x) \in F \Leftrightarrow x \in L(M))$  
> So the new goal is to prove: $\forall x \in \Sigma^*, \hat{\delta}(q_0, x) = q_{f(x)}$  
> We can prove this using Induction on the length of x.  
> 
> Base case:  
> $|x| = 0 \rightarrow x = \epsilon$  
> $\hat{\delta}(q_0, x) = \hat{\delta}(q_0, \epsilon) = q_0 = q_{f(x)}$  
>  
> Inductive step:  
> For every $x \in \Sigma^* \text{ such that } |x| = n, \text{ we have } \hat{\delta}(q_0, x) = q_{f(x)}$  
> Then, say: $|z| = n + 1$  
> We can then write: $z = x.c$ where $c = {a, b} = \Sigma$  
> $\hat{\delta}(q_0, z) = \hat{\delta}(q_0, xc) = \delta(\hat{\delta}(q_0, x), c)$  
> $= \delta(q_{f(x)}, c) =
> \begin{cases} 
>      q_{[f(x) + 1 \text{ mod } 2]} c = a \\
>      q_{f(x)} c \neq a \\
> \end{cases} =
> \begin{cases} 
>      q_{f(xc)} c = a \\
>      q_{f(x(c))} c \neq a \\
> \end{cases} = q_{f(z)} $
>  
> Note: if $ c \neq a$ then $f(xc) = f(x) = f(z)  
> Also: $f(x) + 1 \text{ mod } 2 = f(xa)$

fuck this bro im lost gg go next

hungy ;c 

### Closure Properties of Regular Sets

Theorem: If a language $A$ is regular, then $~A = \Sigma^* /\ A$ is also regular

head empty no thoughts

> use `finsm.io` to draw FSA diagrams