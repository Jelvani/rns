# Residue Number System (RNS) Arithmetic

This repo contains an implementation of an rns class for performing tests of multi-modular arithmetic. 

[Read more about residue number systems](https://en.wikipedia.org/wiki/Residue_number_system)


## Chinese Remainder Theorem (CRT)

This is what makes a RNS possible. More preciseley, given a list of coprime integers `[n_1, n_2, ..., n_i]`, by the CRT we can write some decimal `x` in the range `0 < x < (n_1 * n_2 * ... * n_i)` as the system of equations:
```
  x ≡ a_1 mod n_1
  x ≡ a_2 mod n_2
  ...
  x ≡ a_i mod n_i
```
where `[a_1, a_2, ..., a_i]` is a unique list (called residues) for each value of `x`. This list is the RNS representation of some decimal integer `x` with bases `[n_1, n_2, ..., n_i]`

To solve the system of equations above (this is needed when we convert from RNS form to decimal form) we use a [Satisfiability modulo theories solver](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories) such as Z3.
