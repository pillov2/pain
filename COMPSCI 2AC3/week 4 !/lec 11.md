# Lecture 11 Notes

head empty no thoughts

Recall that $A^* = A^0 \cup A^1 \cup A^2 \cup A^3 = \{x_1x_2x_3x_4... | x_i \in A\} \cup \{\epsilon\}$  
$A^+ = A^1 \cup A^2 \cup A^3 = \{x_1x_2x_3... | x_i \in A\}$

Given an NFA for $A$, how can we find an NFA (with $\epsilon$\_transitions) for $A^+$ and $A^*$ ?

> TODO

Conclusion: if $A$ and $B$ are regular, then these are regular:  
$A.B, A \cup B, (AB \cup B)^*, ($~$A \cup B)$

## Pattern Matching:
`rm *.txt`  
`grep hello*ld a.txt` - (hello world would match because it has hello and ends with ld)

## Book's Notation for Atomic Patterns

- $a \in \Sigma \rightarrow L(a) = \{a\}$
- $\epsilon \rightarrow L(\epsilon) = \{\epsilon\}$
- $\emptyset \rightarrow L(\emptyset) = \emptyset = \{\}$
- $\# \rightarrow L(\#) = \Sigma$
- $@ \rightarrow L(@) = \Sigma^*$

## Book's Notations for Compound Patterns $(\alpha, \beta, \gamma...$ are used for patterns)

- 

> Note:  
> When we write a pattern, we always have some alphabet $\Sigma$ in mind. The order of operations may also matter, so we cause parantheses.

Examples $( \text{where }\Sigma = \{a, b \})$:  
- $\alpha = @a@a@a@ \rightarrow L(\alpha) = \{\text{all strings in } \Sigma^* \text{ that have at least 3 } a \text{'s}\}^* $
- $\beta = @@@a@@a@^*a@@^* \rightarrow L(\alpha) = L(\beta)$ but this does not mean that $\alpha = \beta$

More Examples $(\text{where } \Sigma = \{a, b, c\})$
- $\alpha = \# \cap $ ~ $a \rightarrow L(\alpha) = \{b, c\} = \{\text{any symbol other than } a\}$ and $L(\#) = \Sigma$ and $L($~$a) = \Sigma^*\_L(\alpha)$
- A pattern $\alpha$ such that: $L(\alpha) = \{\text{all strings in } \{a, b, c\}^* \text{ that don't have any } a\text{'s}\} \rightarrow \alpha = @ \cap ($~$(@a@))$ or $\beta = $~$(@a@)$ or $\gamma = (b+c)^*$ or $\delta = (\# \cap$~$a)^*$ 