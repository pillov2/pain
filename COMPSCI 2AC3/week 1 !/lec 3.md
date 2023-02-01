# Lecture 3 Notes

[content covers chapter 2 of the textbook]

In this course, we focus on computing binary functions, or the so-called decision problems

Examples of notions of decision problems:  
- is the given number odd?
- is the given string a palindrome?
    - abbccbba (read left or right is the same)

We focus on inputs in the form of a string

---

### Notations for strings, etc :
- a, b, c, d, ... used for symbols/letters
- u,v,w,x,y,z, ... used for strings
- $\alpha, \beta$ ... used for patterns
- A, B, C, D, ... used for sets (of strings)

---

Alphabet, $\Sigma$: a finite set of symbols 
> - $\Sigma = \{0, 1\}$
> - $\Sigma = \{a, b, c, d\}$
> - $\Sigma = \{0, 1, ... , 9\}$

String: a finite sequence of symbols
> - x = abc
> - x = $\epsilon$ (null string, a string of length 0)
> - | x = 3.14159... | not a string because it is infinite

Length of string:
> - | abc | = 3
> - | $\epsilon$ | = 0

> Note: $\triangleq$ is used when a variable is initialized for the first time

Powers of symbols:
- $a^0 \triangleq \epsilon$ 
- $a^{n+1} \triangleq a ... a$ where $a ... a$ is n+1
- $a^* = a^0 \cup a^1 \cup a^2 \cup$

The set of all strings over alphabet $\Sigma$ is denoted by $\Sigma^*$
- $\Sigma = \{\} = \emptyset, \text{  }\emptyset^* = \{\epsilon\}$
> - $abc \in \Sigma^*$ for $\Sigma = \{a, b, c, d\}$
> - $cda \in \Sigma^*, \epsilon \in \Sigma^*, a \in \Sigma^*$
> - $aefg \notin \Sigma^*, aaa \in \Sigma^*$

Concatenation of strings:
> x = abc, y = bd, xy = abcbd  
> $\therefore$ | xy | = | x | + | y |

#a(x): the total number of occurances of $a$ in string $x$
> - #b(abcbb) = 3

Powers of string:
- $x^0 \triangleq \epsilon$
- $x^{n+1} \triangleq x^n x$
> - $x^1 = x = abb$
> - $x^2 = abbabb$

Prefix: we say $x$ is a prefix of $y$ if $x$ is an intial segment of $y$
> - ab is a prefix of abc
> - ab is a prefix of ab
> - $\epsilon$ is a a prefix of any string

Proper prefix: a prefix that is not the string itself
> - ab is not a proper prefix of ab
> - $\epsilon$ is a proper prefix of any string except itself

---

### Operations on sets of strings 
> (usually defined over an alphabet)
> 
> $A \subseteq \Sigma^*, B \subseteq \Sigma^*$  
> $A$: all strings that start with a, for alphabet $\Sigma = \{a, b\}$

~$A$: completion
- ~$A$ = $\Sigma^*$ \ $A$ = $\{x \in \Sigma^*, x \notin A\}$

Set Concatenation: $AB = \{xy: x \in A, y \in B\}$  
> $A = \{aa, b\}, B = \{b, c\}$  
> $\therefore AB = \{aab, bb, aac, bc\}$

Powers of sets: 
- $A^0 \triangleq \{\epsilon\}$
- $A^{n+1} \triangleq A^n A$
> - $A^1 = A$

Usual set operations: 
> - $A \cup B$
> - $A \cap B$

We say a binary operation $\otimes$ is associative if for all A, B, and C, (A $\otimes$ B) $\otimes$ C is equal to A $\otimes$ (B $\otimes$ C)

We say a binary operation $\otimes$ is commutative is for all A and B, A $\otimes$ is equal to B $\otimes$ A

| operation     | associative  | commutative  | identity       |  
| :-------:     | :---------:  | :---------:  | :------:       |
| union         | $\checkmark$ | $\checkmark$ | $\emptyset$    |
| intersection  | $\checkmark$ | $\checkmark$ | $\Sigma^*$     |
| concatenation | $\checkmark$ | X            | $\{\epsilon\}$ |

> Notes:  
> "A" is an identity element for binary operation $\otimes$ if A $\otimes$ B and B $\otimes$ A are both equal to B for all B
>
> $\emptyset \neq \epsilon \neq \{\epsilon\}$
>
> $\emptyset = \{\}$

---

### Thoughts for next lecture:
$A.(B \cup C) = AB \cup AC$ $?$  
$A.(B \cap C) = AB \cap AC$ $?$

<span style="color:blue">some *blue* hello</span>

<span style="background-color: #264CAD">This text is highlighted in blue.</span>