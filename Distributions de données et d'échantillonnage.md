

### Échantillonnage aléatoire et biais d'échantillonnage

Échantillon : Un sous-ensemble d'un ensemble de données plus vaste.
N ( n ) : La taille de la population (échantillon).
Échantillonnage aléatoire : Dessiner des éléments dans un échantillon au hasard (ou chaque échantillonnée a une chance égale d'être choisi )
Échantillonnage stratifié : Diviser la population en strates et échantillonner au hasard dans chaque strate.
Strate (pl., strates) : Sous-groupe homogène d’une population présentant des caractéristiques communes.
Échantillon aléatoire simple : L'échantillon qui résulte d'un échantillonnage aléatoire sans stratification de la population .
Biais : Erreur systématique.
Biais de l'échantillon : Un échantillon qui dénature la population.

un biais d'autoselection : est quand l'echantillonage se fait de maniere automatique non pas par l'experimentateur mais pas l'chantilon lui meme. c'est
l'exemple des avis sur les restaurant. En effet les gens qui depose un avis en general ont souvent soit eu des mauvaise experience, soit en lien avec le resto, soit une personne differents de la plus
part des genes. 

biais statistique : erreur d'echantillonage
erreur du au hasard vs erreur due a un biais
l'objective d'un echantillonage est de parvenir a une representativité (en jouant sur la qualité de chaque element sous plusieur critére dont l'exactitude)

Dans l'échantillonnage stratifié , la population est divisée en strates et des échantillons aléatoires sont prélevés dans chaque strate.

CCL : 
Même à l’ère du Big Data, l’échantillonnage aléatoire reste une flèche importante dans le carquois du data scientist.
Un biais se produit lorsque les mesures ou les observations sont systématiquement erronées parce qu'elles ne sont pas représentatives de l'ensemble de la population.
La qualité des données est souvent plus importante que leur quantité, et l’échantillonnage aléatoire peut réduire les biais et faciliter une amélioration de la qualité qui autrement serait d’un coût prohibitif.

### Biais de séléction

Biais de séléction : Biais résultant de la manière dont les observations sont sélectionnées.
Surveillance des données : Recherche approfondie à travers les données à la recherche de quelque chose d'intéressant.
Vaste effet de recherche : Biais ou non-reproductibilité résultant d'une modélisation répétée des données ou d'une modélisation de données avec un grand nombre de variables prédictives.

La régression vers la moyenne est la conséquence d’une forme particulière de biais de sélection
exemple, une victoire est due principalement a la competence et a la chance. mais souvent la chance n'est pas au rendez vous, donc le nombre de victoire a tendance a regresser au fur et a mesure.

NB : La régression vers la moyenne, c'est-à-dire « revenir en arrière », est distincte de la méthode de modélisation statistique de régression linéaire, dans laquelle une relation linéaire est estimée entre des variables prédictives et une variable de résultat.

Ccl : 
Spécifier une hypothèse, puis collecter des données selon les principes de randomisation et d'échantillonnage aléatoire garantit l'absence de biais.
Toutes les autres formes d'analyse de données courent le risque de biais résultant du processus de collecte/d'analyse des données (exécution répétée de modèles dans l'exploration de données, surveillance des données dans la recherche et sélection après coup d'événements intéressants).


### Distribution d'échantillonnage d'une statistique

Exemple de statistique : Une métrique calculée pour un échantillon de données tiré d’une population plus large.
Distribution des données : La distribution de fréquence des valeurs individuelles dans un ensemble de données.
Distribution d'échantillonnage : Distribution de fréquence d'une statistique d'échantillon sur de nombreux échantillons ou ré-échantillons.
Théorème central limite : Tendance de la distribution d’échantillonnage à prendre une forme normale à mesure que la taille de l’échantillon augmente.
Erreur standard : La variabilité (écart type) d'une statistique d'échantillon sur de nombreux échantillons (à ne pas confondre avec l'écart type , qui en lui-même fait référence à la variabilité des valeurs de données individuelles ).

la distribution d'echantillonage a souvent une forme en cloche qui est plus etroite  à condition que la taille de l'échantillon soit suffisamment grande et que l'écart des données de la normalité n’est pas trop grand.
elle est calculer a des fins d'inference, c'est a dire les intervalles de confiance et les test d'hypothese

l'erreur standard = l'écart type s des valeurs de l'échantillon / racine de n
donc a mesure que la taille de l'ech augmente, l'erreur std dimiunue
regle de la racine carrée de n : pour réduire l’erreur type d’un facteur 2, la taille de l’échantillon doit être augmentée d’un facteur 4.
cette approche de minimisation de l'erreur std est trés couteuse. a la place, nous pouvons simplement faire un re echantillonage boostrap

CCL : 
La distribution de fréquence d'une statistique d'échantillon nous indique comment cette métrique se révélerait différemment d'un échantillon à l'autre.
Cette distribution d'échantillonnage peut être estimée via le bootstrap, ou via des formules qui s'appuient sur le théorème central limite.
Une mesure clé qui résume la variabilité d’une statistique d’échantillon est son erreur type.

### Le boostrap












