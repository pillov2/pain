# Lecture 10 Notes

### Subset Construction Game:  

> Lemma:  
> $\forall A \subseteq Q_N \text{ also can be written as }(\forall A \in Q_M)$  and $\forall x \in \Sigma^*$ :  
> $\hat{\delta}_M (A, x) = \hat{\Delta}_N (A, x)$

Proof: induction on | $x$ |  
(see the book for lengthy proof)

Theorem: $L(M) = L(N)$  
proof:  
$x \in L(M) \Leftrightarrow \hat{\delta} (s_M, x) \in F_M \Leftrightarrow \hat{\delta} (S_N, x) \in \{A \subseteq Q_M : A \cap F_N \neq \emptyset\} \Leftrightarrow \hat{\Delta}_N (S_N, x) \in \{A \subseteq Q_N : A \cap F_N \neq \emptyset \Leftrightarrow \hat{\Delta}_N (S_N, x) \cap F_N \neq \emptyset \Leftrightarrow x \in L(N)$

NFAs with $\epsilon$\_transitions:  
We extend $\Delta : Q$ x $\Sigma \rightarrow 2^Q$ to $\Delta : Q$ x $(\Sigma \cup \{\epsilon\}) \rightarrow 2^Q$ so that the NFA can change its state without even consuming a symbol.

$L(N) = \{abc, bca\} \cdot (\{c\}^* \cup $  
e.g: $abcccccc \in L(N)$,

It turns out that any NFA with $\epsilon$\_transitions can be turned into an equivalent NFA or DFA. We don't prove this.

Claim: Every regular set can be represented by an NFA with $\epsilon$\_transitions where we have:
- only one start state
- only one accept state
- the start state doesn't have any incoming transitions
- the accepted state doesn't have any outgoing transitions

Idea: Add a new start state, add $\epsilon$_transitions from it to all previous start states (old start states will no longer be start states). Add a new accept state...(and repeat the same process?)


If $A$ and $B$ are regular, then $A.B \text{ (concatenation)} = \{xy : x \in A, y \in B\}$ is regular.



i want to go home man i dont understand anything wtf