Data Encryption Standard in Python
---
<br>

> See [Wikipedia](https://en.wikipedia.org/wiki/Data_Encryption_Standard)

<br>

### What is currently implemented?

```diff
+ 1. Get User Input
+ 2. Convert to 64 Bit Blocks
- 3. Initial Permutation
+ 4. Split Block

! 5. Feistel
!   5.1. Sub Key Generation (Key Schedule)
+   5.2. Expansion
-   5.3. Key Mixing
-   5.4. Substitution
-   5.5. Permutation

+ 6. XOR L ^ R
+ 7. Add X & R
```

### To decrypt, it simply applies the same function(s) again in reverse order
