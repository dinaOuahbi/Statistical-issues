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

#### test de permutation 
permuter : changer d'ordre d'un ensemble de valeurs (incarnation de l'hypothese null : pas de difference entre A et B) puis tirrage aleatoire avec remplacement
Si la différence observée se situe bien dans l’ensemble des différences permutées, alors nous n’avons rien prouvé : la différence observée se situe dans la gamme de ce que le hasard pourrait produire.
Deux variante de test de permutation : 
- exhaustif :  nous déterminons toutes les manières possibles de les diviser (applicable sur echantillon petite taille)
- boostrap : tirage aleatoire avec remplacement

CCL : 
Dans un test de permutation, plusieurs échantillons sont combinés puis mélangés.
Les valeurs mélangées sont ensuite divisées en rééchantillons et la statistique d'intérêt est calculée.
Ce processus est ensuite répété et la statistique rééchantillonnée est tabulée.
La comparaison de la valeur observée de la statistique à la distribution rééchantillonnée vous permet de juger si une différence observée entre les échantillons peut se produire par hasard.

### Signification statistique et valeurs p

p value : C’est la fréquence à laquelle le modèle aléatoire produit un résultat plus extrême que le résultat observé
alpha :  Étant donné un modèle aléatoire, quelle est la probabilité d'un résultat aussi extrême ? 

Même si un résultat est statistiquement significatif, cela ne signifie pas qu’il a une signification pratique. Une petite différence qui n’a aucune signification pratique peut être statistiquement significative si elle résulte d’échantillons suffisamment grands. De grands échantillons garantissent que de petits effets non significatifs peuvent néanmoins être suffisamment importants pour exclure le hasard comme explication. Exclure le hasard ne rend pas comme par magie important un résultat qui, par essence, est sans importance.

erreur de type 1 : on conclut a tort qu'un effet est reel (en realité in est du au hasard)
erreur de type 2 : un effet non significative qui est en realité un effet réel (taille d'ech trop ptite en generale)

les test d'hypo sont structuré pour minimiser l'ereur de type 1

pour la data science les valeurs p sont parfois utilisées comme entrées intermédiaires dans certains modèles statistiques ou d'apprentissage automatique : une fonctionnalité peut être incluse ou exclue d'un modèle en fonction de sa valeur p.

### t test
developper pour approximer la distribution d'une moyenne d'échantillon unique
Avant l’avènement des ordinateurs, les tests de rééchantillonnage n’étaient pas pratiques et les statisticiens utilisaient des distributions de référence standard.
Une statistique de test pourrait alors être standardisée et comparée à la distribution de référence .
L’une de ces statistiques standardisées largement utilisées est la statistique t.

### Tests multiples
Plus vous ajoutez de variables ou plus vous exécutez de modèles, plus la probabilité que quelque chose apparaisse comme « significatif » par hasard est grande.
Taux de fausses découvertes : Sur plusieurs tests, taux de commission d’une erreur de type 1.
Inflation alpha : Le phénomène de tests multiples, dans lequel alpha , la probabilité de commettre une erreur de type 1, augmente à mesure que vous effectuez davantage de tests.

pour la data science,  le risque d'obtenir un modèle illusoire dont l'efficacité apparente est en grande partie le produit du hasard est atténué par la validation croisée

CCL : 
La multiplicité dans une étude de recherche ou un projet d'exploration de données (comparaisons multiples, nombreuses variables, nombreux modèles, etc.) augmente le risque de conclure que quelque chose est significatif par hasard.
Pour les situations impliquant de multiples comparaisons statistiques (c'est-à-dire plusieurs tests de signification), il existe des procédures d'ajustement statistique.
Dans une situation d'exploration de données, l'utilisation d'un échantillon d'exclusion avec des variables de résultat étiquetées peut aider à éviter des résultats trompeurs.

### Degrés de liberté
utilisé dans les calcules de variance et d'ecart type. cela est consomé par les test d'hypothese (test t, test F, etc ...) car les statistiques d'echantillonage sont standardiser avant d'etre utiliséses dans les tests.
Lorsque vous utilisez un échantillon pour estimer la variance d’une population, vous obtiendrez une estimation légèrement biaisée à la baisse si vous utilisez n au dénominateur. Si vous utilisez n – 1 au dénominateur, l’estimation sera exempte de ce biais.

Pour la data science, la taille des données est généralement suffisamment grande pour que cela fasse rarement une réelle différence. donc le degré de liberté n'est pas important. 
Il existe cependant un contexte dans lequel cela est pertinent en sience de donnée : l’utilisation de variables factorisées dans la régression.

### ANOVA (analyse de variance)
comparaison de plusieur groupes deux par deux
La statistique F est basée sur le rapport entre la variance entre les moyennes des groupes (c'est-à-dire l'effet du traitement) et la variance due à l'erreur résiduelle. 
Plus le résultat est statistiquement significatif.

si un facteur qui varie (le groupe par exemple) on parle d'ANOVA unidirectionnelle ou a un seul facteur
ANOVA a deux facteurs : par exemple groupe A le week-end, groupe A en semaine, groupe B le week-end, etc
dans ce cas on identifie l'effet general d'interaction puis on depare les observation du weekend et de la semaine. 


### Test du chi 2
Le test du chi carré est utilisé avec les données de comptage
Statistique du chi carré : Une mesure de la mesure dans laquelle certaines données observées s'écartent des attentes.
La distribution du chi carré est généralement asymétrique, avec une longue queue vers la droite 
Plus la statistique observée est éloignée de la distribution du chi carré, plus la valeur p est faible.

quand les comptes sont extremement faible (< 5 en generale), nous pouvons determiner a quel point (lors de la permutation) le resultat obsérvé est extreme, c'est ce qu'on appelle le test exact de Fisher


### Puissance de la taille de l'echantillon

un resultat de test d'hupothese depend non seulement de l'effet reel entre deux groupe mais aussi du tirage au sort
en general, plus la difference entre ces deux groupe est petite, plus il faudra d'echantillon pour la detecter
La puissance est la probabilité de détecter une taille d’effet spécifiée avec des caractéristiques d’échantillon spécifiées (taille et variabilité).
L’utilisation la plus courante des calculs de puissance consiste à estimer la taille d’un échantillon dont vous aurez besoin.




































