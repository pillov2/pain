# Lecture 12 Notes

Patterns are redundant. We actually don't need all of the atomic patterns or the operators to specify sets. 

We can always replace:
- $\# \text{ with } a + b + c...$
- $\epsilon \text{ with } \emptyset^*$
    - recall that $\emptyset^* = \{\}^* = \{\epsilon\}$
- $\alpha \cap \beta \text{ with }$~$($~$\alpha \cup $~$\beta)$ using DeMorgan's law
- ~ with ??

> ### Exercise:
>  
> $\Sigma = \{a, b\}$. Can you find a pattern that is equivalent to ~$a$ without using complement? What about ~$(b@b@b)?$  
>  
> Note: recall that we have the following operations $*, ., \cap, +, \#, @, \emptyset$
>  
> $\alpha = @\#a@ + @a\#@ + b^*$  
> $\beta = \#\#@ + b^*$  
> $L($~$a) = L(\alpha) = L(\beta)$

## Regular Expressions

A regular expression is a pattern that only uses the following:
- Atomic: $\emptyset, a (a \in \Sigma), \epsilon$
- Operators: $+, ., *$

Regular expressions define equivalency classes:  
$\alpha \equiv \beta$ if $L(\alpha) = L(\beta)$
- Reflexivity: $\alpha \equiv \alpha$
- Symmetry: $\alpha \equiv \beta \Leftrightarrow \beta \equiv \alpha$
- Transitivity: $\alpha \equiv \beta$ and $\beta \equiv \gamma \Rightarrow \alpha \equiv \gamma$  
$\alpha \leq \beta$ if $L(\alpha) \subseteq L(\beta)$  

The order of precendence for the operators is $* > . > +$

> Example:  
> $ca^*b + bc^*a \equiv (c(a^*)b) + (b(c^*)a)$

### Theorem. The following options are all equivalent for any set $A \subseteq \Sigma^*$

$(i) \text{ } A \text{ is regular (has a DFA)}$  
$(ii) \text{ } \exists \text{ an NFA } N \text{ such that } L(N) = A$
$(iii) \text{ } \exists \text{ an NFA } N \text{ with } \epsilon \text{\_transitions, } L(N) = A$  
$(iv) \text{ } \exists \text{ a pattern } \alpha \text{ such that } L(\alpha) = A$  
$(v) \text{ } \exists \text{ a regular expression } \alpha, \text{ such that } L(\alpha) = A$  

$(ii) \rightarrow (i):$ subset construction game  
$(iii) \rightarrow (ii):$ didn't discuss but true  
$(v) \rightarrow (ii):$ if $\alpha$ is atomic, then it has an NFA
-  $L(\emptyset)$
- $L(\alpha)$
- $L(\epsilon)$
- otherwise, we use structural induction:
    - if $L(\alpha)$ and $L(\beta)$ are regular (have DFA's), then:
        - $L(\alpha \beta) = L(\alpha) . L(\beta)$ is regular
        - $L(\alpha + \beta) = L(\alpha) \cup L(\beta)$ is regular
        - $L(\alpha^*) = L(\alpha)^*$ is regular

### Remaining Questions

- Given two regular expressions $\alpha$ and $\beta$, how can we tell if $\alpha \equiv \beta$ ?
- Given regular expressions $\alpha$ and string $x$, how can we tell if $x \in L(\alpha)$ ?
- Can we find a regular expression $\alpha$ such that $L(\alpha) = \{a^nb^n : n \geq 0\}$ ? (impossible??)