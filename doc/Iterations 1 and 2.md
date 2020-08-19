# Iterations 1 and 2

## Iteration 1
We base our approach for Iteration on the translation relations as 
part of [Wiktionary](https://www.wiktionary.org/).
We exploit these translations between Dutch and English to link
[Referentie Bestand Nederlands](https://ivdnt.org/images/stories/producten/documentatie/rbn_documentatie_nl.pdf)
and English FrameNet version 1.7.

We create a near equivalence link between a Dutch sense as part of RBN and a LU as part of English FrameNet if:
* the lemma and part of speech combination of the RBN sense is monosemous in RBN
* the lemma and part of speech combination of the FrameNet LU is monosemous in FrameNet 1.7 and WordNet 3.0.

## Iteration 2
We exploit the synonyms relations as part of [Open Dutch WordNet](http://wordpress.let.vupr.nl/odwn/)
to also link synonyms to FrameNet LUs for which a link was established in Iteration 1.