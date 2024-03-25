
## EDA

l'inference : tirer des ccl sur de grandes populations a partir de petites echantillons

Les données sont généralement classées dans les logiciels par type.

Les types de données incluent les valeurs numériques (continues, discrètes) et catégorielles (binaire, ordinale ).

La saisie de données dans un logiciel agit comme un signal au logiciel sur la manière de traiter les données.

La structure de données de base en science des données est une matrice rectangulaire dans laquelle les lignes sont des enregistrements et les colonnes sont des variables (caractéristiques).

La terminologie peut prêter à confusion ; il existe une variété de synonymes issus des différentes disciplines qui contribuent à la science des données (statistiques, informatique et technologies de l'information).

### Estimation de la localisation 

moyenne : La somme de toutes les valeurs divisée par le nombre de valeurs.
Moyenne pondérée : La somme de toutes les valeurs multipliée par un poids divisée par la somme des poids.
Médian : La valeur telle que la moitié des données se trouve au-dessus et en dessous.
Centile : La valeur telle que P pour cent des données se situe en dessous.
Moyenne tronquée : La moyenne de toutes les valeurs après suppression d’un nombre fixe de valeurs extrêmes.
Robuste : Insensible aux valeurs extrêmes.
Valeur aberrante : Une valeur de données très différente de la plupart des données.

Attention : la moyenne ne represente pas toujours le meilleurs choix de la tendence centrale

En stat on parle de estimation, tandis que en data sience on parle de mesure. En effet en statistique, on donne beaucoup d'importance a l'incertitude
Une moyenne tronquée élimine l’influence des valeurs extrêmes
interet d'une moyenne pondérer : 
- donnée plus d'importance aux valeur sous representé
- sous pondérer les valeur qui sont intrinsequement plus variables que d'autres

l'interet de la mediane est d'empecher les valeurs qui dont tres elevé ou trés faibles (par rapport au reste ) d'influencer la tendance centrale. Or, elle ne s'interesse qu'au deux valeur qui se trouve au milieu d'une liste trié
la mediane pondérée resiste aux valeurs aberante

les valeurs aberrantes sont souvent mais pas forcement le resultat d'eereurs de mesures

CCL :
la moyenne tronquée est a la fois resustante au valeur aberrante et utilise d'avantage de données pour calculer l'estimation de l'emplacement. 
La mesure de base de la localisation est la moyenne, mais elle peut être sensible aux valeurs extrêmes (valeur aberrante).
D'autres mesures (médiane, moyenne tronquée) sont moins sensibles aux valeurs aberrantes et aux distributions inhabituelles et sont donc plus robustes.

### Estimation de la variabilité (dispersion)
Déviations : La différence entre les valeurs observées et l'estimation de l'emplacement (ou la tendance centrale)
Variance : La somme des carrés des écarts par rapport à la moyenne divisée par n – 1 (DDL), où n est le nombre de valeurs de données.
Écart-type : La racine carrée de la variance.
norme Manhattan (norme l1 ou MAE) : La moyenne des valeurs absolues des écarts par rapport à la moyenne.
Écart absolu médian par rapport à la médiane : La médiane des valeurs absolues des écarts par rapport à la médiane.
Gamme : La différence entre la plus grande et la plus petite valeur d’un ensemble de données.
Statistiques de rang : Métriques basées sur les valeurs de données triées de la plus petite à la plus grande.
Gamme interquartile (IQR): La différence entre le 75e centile et le 25e centile.

NB : on calcule l'ecart absolue pour evité que celui ci ne s'anule avec les ecarts negative
Mathématiquement, travailler avec des valeurs carrées est bien plus pratique que des valeurs absolues, notamment pour les modèles statistiques (donc l'ecart type est preferé de la MAE)

Le ddl est utiliser a la place de n dans la formule de la variance pour empeche que l'on sous estime celle ci a l'echelle de la population. cela nous emmene a une estimation biaisée

Mediane absolute deviation n'est pas influencé par les valeurs aberantes
Il existe aussi l'ecart type tronquée

parmis les estimations de l'ecart basée sur le percentil : 
- l'etendu (tres sensible aux valeur aberantes)
- examiner la plage des données aprés avoir tronquer
- interval interquartile : difference entre le 25e et 75e centile
formelement, le centile est la moyenne penderée. ou le poid w est compris entre 0 et 1

CCL :
La variance et l’écart type sont les statistiques de variabilité les plus répandues et les plus couramment rapportées.
Les deux sont sensibles aux valeurs aberrantes.
Les mesures plus robustes incluent l’écart absolu moyen, l’écart absolu médian par rapport à la médiane et les centiles (quantiles).


### Explorer la distributio des données
Boîte à moustaches : Un tracé présenté par Tukey comme moyen rapide de visualiser la distribution des données. il est basé sur les percentiles
Tableau des fréquences : Un décompte du nombre de valeurs de données numériques qui tombent dans un ensemble d'intervalles (bacs).
Histogramme : Un tracé du tableau de fréquences avec les cases sur l'axe des x et le nombre (ou la proportion) sur l'axe des y. Bien que visuellement similaires, les graphiques à barres ne doivent pas être confondus avec les histogrammes
Graphique de densité : Une version lissée de l'histogramme, souvent basée sur une estimation de la densité du noyau .

au niveau d'un boxplot : 
- barre hz : mediane
- trait en pointié : plage de valeur les plus abandant (IQR)
- point en cercle : valeurs aberrantes en dessue du 75e centile et en dessous du 25e centile

un histo est un moyen de visualiser un tableau de frequences avec les bacs dans l'axe des x et la proportion dans l'axe des y
les histo incluent les bacs vide
les bacs sont de meme largeur
le nombre de bacs depends de l'user et iles sont toujours contigues.

L'asymétrie indique si les données sont asymétriques vers des valeurs plus grandes ou plus petites
l'aplatissement indique la propension des données à avoir des valeurs extrêmes.

l'histo peut etre associer a un estimateur de densité qui montre la distrib sous forme de ligne continue

CCL :
Un histogramme de fréquence trace les décomptes de fréquence sur l'axe des y et les valeurs des variables sur l'axe des x ; cela donne une idée de la répartition des données en un coup d'œil.
Un tableau de fréquences est une version tabulaire des décomptes de fréquences trouvés dans un histogramme .
Un diagramme en boîte (avec le haut et le bas de la boîte aux 75e et 25e percentiles, respectivement) donne également une idée rapide de la distribution des données ; il est souvent utilisé dans les affichages côte à côte pour comparer les distributions.
Un tracé de densité est une version lissée d'un histogramme ; cela nécessite une fonction pour estimer un tracé basé sur les données (plusieurs estimations sont possibles, bien sûr).

### Explorer les données binaires et categorielles
Mode : La catégorie la plus courante ou une valeur dans un ensemble de données
Valeur attendue : Lorsque les catégories peuvent être associées à une valeur numérique, cela donne une valeur moyenne basée sur la probabilité d'occurrence d'une catégorie.
Diagramme à barres : La fréquence ou la proportion pour chaque catégorie, représentée sous forme de barres.
Camemberts  La fréquence ou la proportion pour chaque catégorie, représentée sous forme de quartiers dans un diagramme.

nb : La conversion de données numériques en données catégorielles est une étape importante et largement utilisée dans l'analyse des données car elle réduit la complexité (et la taille) des données

la valeur attendu est la somme des des valeur multiplier chacune par sa proba d'occurence

CCL :
Les données catégorielles sont généralement résumées dans des proportions et peuvent être visualisées dans un graphique à barres.
Les catégories peuvent représenter des éléments distincts (pommes et oranges, hommes et femmes), des niveaux d'une variable factorielle (faible, moyen et élevé) ou des données numériques regroupées.
La valeur attendue est la somme des valeurs multipliée par leur probabilité d'occurrence, souvent utilisée pour résumer les niveaux de variables factorielles.


### Corrélation
entre deux variables numeriques

Coefficient de corrélation : Métrique qui mesure dans quelle mesure les variables numériques sont associées les unes aux autres (allant de –1 à +1).
Matrice de corrélation : Un tableau dans lequel les variables sont affichées à la fois sur les lignes et les colonnes, et les valeurs des cellules sont les corrélations entre les variables.
Nuage de points : Un tracé dans lequel l'axe des x est la valeur d'une variable et l'axe des y la valeur d'une autre.

comment mesurer la correlation 
- domme vectorielle des produits
- le coeff de coorelation : entre deux variable sur une meme echelle : multiplier les ecart de chaque variable par rapport a sa moyenne, puis en faire la somme et la divisée par le produit des ecart types. On divise le resultat par le DDL pour avoir une valeur comprise en -1 et +1
  
la matrice de coorelation est caracterisée par :
- une diagonale de 1
- une redondance des information

coefficients de corrélation classique : Pearson 
le coef de coorelation Pearson est sensible au valeurs aberrante, cependant il existe des alternative en R et python plus robuste. eg, covRob (avec R) et sklearn.covariance

coefficients de corrélation basés sur le rang des données sont plus robuste envers les valeurs aberrantes (le rho de Spearman ou le tau de Kendall)

les nuage de point sont moins informative a mesure que la taille des données augmente. on peut tout fois ajouté la transparence sur ces points de nuage

CCL : 
Le coefficient de corrélation mesure dans quelle mesure deux variables appariées (par exemple, la taille et le poids des individus) sont associées l'une à l'autre.
Lorsque des valeurs élevées de v1 vont avec des valeurs élevées de v2, v1 et v2 sont positivement associés .
Lorsque des valeurs élevées de v1 vont avec des valeurs faibles de v2, v1 et v2 sont associés négativement .
Le coefficient de corrélation est une mesure standardisée, de sorte qu'il va toujours de –1 (corrélation négative parfaite) à +1 (corrélation positive parfaite).
Un coefficient de corrélation de zéro indique l'absence de corrélation, mais sachez que des arrangements aléatoires de données produiront à la fois des valeurs positives et négatives pour le coefficient de corrélation, par simple hasard.

### Explorer deux variables o uplus
Tableau de contingence : Un décompte entre deux ou plusieurs variables catégorielles.
Classement hexagonal : Un tracé de deux variables numériques avec les enregistrements regroupés en hexagones.
Tracé de contour : Un tracé montrant la densité de deux variables numériques comme une carte topographique.
Intrigue du violon : Semblable à un boxplot mais montrant l’estimation de la densité.

un tableau de contingeance est equivalent a un nuage de point mais pour deux variables categorielles

CCL : 
Le regroupement hexagonal et les tracés de contour sont des outils utiles qui permettent d'examiner graphiquement deux variables numériques à la fois, sans être submergé par d'énormes quantités de données.
Les tableaux de contingence sont l'outil standard pour examiner le nombre de deux variables catégorielles.
Les boxplots et les violon plots vous permettent de tracer une variable numérique par rapport à une variable catégorielle.











