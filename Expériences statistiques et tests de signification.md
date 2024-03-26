# Expériences statistiques et tests de signification

### TEST A ET B

un pipeline d'inference conciste a formuler une hypothese (medoc A plus eficasse que B) suivi d'une conception de l'experience et d'une collection des données et enfin d'une analyse inferentielle aboutissant a une conclusion.
sujet randomisées : attribution au hasard aux traitements A et B
la difference entre A et B peut etre liée soit a l'effet reelement different de chaque traitment, ou au hasard du tirage qui fait q'un moment donnée un groupe est plus fort que l'autre groupe.

la mesure statistique peut etre binaire ou une valeur continue (moyenne et std)

Pourqupoi un groupe controle ? 
le groupe test et control sont soumisent aux memes conditions de l'experimentation sauf biensur pour la variable etudier. donc sans le temoin, rien ne garantit que toutes choses sont egales par ailleurs

une etude en double aveugle et quand ni l'experimentateur ni les sujets ne savent ce qu'ils recoit comme traitement. car savoir pourait affecter la reponse au traitement.

CCL : 
Les sujets sont répartis dans deux (ou plusieurs) groupes qui sont traités exactement de la même manière, sauf que le traitement étudié diffère d'un groupe à l'autre.
Idéalement, les sujets sont répartis au hasard dans les groupes.

### TESTS D'HYPOTHESE
Savoir si le hasard peut etre a l'origine d'une difference obtenue
Hypothèse nulle : L’hypothèse selon laquelle le hasard est à blâmer.
Hypothèse alternative : Contre point au nul (ce que vous espérez prouver).
Test à sens unique : Le test d'hypothèse qui compte le hasard ne donne que des résultats dans une seule direction.
Test bidirectionnel : Le test d'hypothèse qui compte le hasard donne des résultats dans deux directions.

pourquoi faut il une hypothese ? 
car on sous estime generalement le comportement aleatoir, et on n'anticipe pas les evennement extreme. donc les test d'hypothese protege les chercheurs contre le hasard.

On veut donc pouvoir demontrer que A et B sont plus différents de ce que le hasard pourrait produire.
La nature de l’hypothèse nulle détermine la structure du test d’hypothèse. l'hypothese nul pourrait etre que A et B n'ont pas de difference, ou que A a un effet inferieur que B ...

Si on cherche a demontré une hypothèse alternative directionnelle (B est meilleur que A), on utilise un test d’hypothèse unidirectionnel (ou unilatéral). Cela signifie qu'un hasard extrême entraîne une seule direction dans la valeur p.
A l'inverse si on cherche a se proteger d'un effet de hasard dans les deux sens, on applique un test d'hypothese bilaterale. Cela signifie que les résultats extrêmement aléatoires dans les deux sens comptent dans la valeur p.

CCL : 
Une hypothèse nulle est une construction logique incarnant l’idée que rien de spécial ne s’est produit et que tout effet que vous observez est dû au hasard.
Le test d'hypothèse suppose que l'hypothèse nulle est vraie, crée un « modèle nul » (un modèle probabiliste) et teste si l'effet que vous observez est un résultat raisonnable de ce modèle.


### REECHANTILLONNAGE
échantillonner à plusieurs reprises des observations.
utiliser surtout dans certaint modele d'apprentissage automatique comme les arbres de deision (processus de foret aleatoire)
Il existe deux principaux types de procédures de rééchantillonnage : les tests d'amorçage et de permutation


































