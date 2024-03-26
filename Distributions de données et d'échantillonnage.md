

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

Exemple d'amorçage : Un échantillon prélevé avec remplacement à partir d’un ensemble de données observées.
Rééchantillonnage : Le processus de prélèvement d’échantillons répétés à partir de données observées ; comprend à la fois les procédures d'amorçage et de permutation (réorganisation).

L'algorithme de rééchantillonnage bootstrap de la moyenne, pour un échantillon de taille n , est le suivant :

- Dessinez un exemple de valeur, enregistrez-le, puis remplacez-le.
- Répétez n fois.
- Enregistrez la moyenne des n valeurs rééchantillonnées.
- Répétez les étapes 1 à 3 R fois.
- Utilisez les résultats R pour :
    - Calculez leur écart type (cela estime l’erreur type moyenne de l’échantillon).
    - Produisez un histogramme ou un boxplot.
    - Trouvez un intervalle de confiance.

le Bagging : l'execution plusieur fois d'un arbe de decision (classifier ou regressor) sur des echantillon boostrap

Donc le BOOSTRAP nous informe simplement du comportement d’un grand nombre d’échantillons supplémentaires s’ils étaient tirés d’une population comme notre échantillon d’origine.

CCL : 
Le bootstrap (échantillonnage avec remplacement à partir d’un ensemble de données) est un outil puissant pour évaluer la variabilité d’une statistique d’échantillon.
Le bootstrap peut être appliqué de la même manière dans une grande variété de circonstances, sans étude approfondie des approximations mathématiques des distributions d'échantillonnage.
Cela nous permet également d'estimer les distributions d'échantillonnage pour les statistiques pour lesquelles aucune approximation mathématique n'a été développée.
Lorsqu’elle est appliquée aux modèles prédictifs, l’agrégation de plusieurs prédictions d’échantillons bootstrap (bagging) surpasse l’utilisation d’un seul modèle.

### Intervalles de confiance
permet de comprendre l'erreur potentielle dans une estimation d'echantillon

Un niveau de confiance : Pourcentage d’intervalles de confiance, construits de la même manière à partir de la même population, qui devraient contenir la statistique d’intérêt.
Points de terminaison de l'intervalle : Le haut et le bas de l’intervalle de confiance.

IC : sont dans un niveau de couverture exprimé en %
eg, un IC de 90% est un interval qui englobe les 90% centraux de la distribution d'echantillonnage boostrap d'un echantillon statistique

niveau de confiance est le % associé à l'intervalle de confiance. plus ce niveau est elevé, plus l'interval est large, et donc plus l'incertitude est grande. cela va de meme avec une petite taille de l'echantillon

les datasientist voudront connaitre l'IC pour savoir si un echantillon plus large est necessaire.

CLL :
Les intervalles de confiance constituent la manière habituelle de présenter des estimations sous forme de plage d'intervalles.
Plus vous disposez de données, moins une estimation d’échantillon sera variable.
Plus le niveau de confiance que vous pouvez tolérer est bas, plus l’intervalle de confiance sera étroit.
Le bootstrap est un moyen efficace de construire des intervalles de confiance.

### Distribution normale

sous forme de clochela
erreur : difference entre un point de données et une valeur predite ou moyenne
standardiser : soustraire la moyenne et diviser par l'ecart type. Conversion des données en scores z
score z : resultat de la normalisation d'un point de donnée individuel
norme normal : distribution normale avec moyenne = 0 et ecart type = 1
qq-plot : Un tracé pour visualiser à quel point une distribution d'échantillon est proche d'une distribution spécifiée, par exemple la distribution normale.

L'utilité de la distribution normale découle du fait que de nombreuses statistiques sont normalement distribuées dans leur distribution d'échantillonnage.
La distribution normale est également appelée distribution gaussienne en l'honneur de Carl Friedrich Gauss
les unité dans l'axe des x sont exprimées en termes d'ecart type par rapport a la moyenne

le qq plot classe les scores z de bas en haut et les traces sur l'axe des y. Si les points se situent à peu près sur la ligne diagonale, la distribution de l'échantillon peut alors être considérée comme proche de la normale
 
CCL :
La distribution normale était essentielle au développement historique des statistiques, car elle permettait une approximation mathématique de l'incertitude et de la variabilité.
Bien que les données brutes ne soient généralement pas distribuées normalement, des erreurs le sont souvent, tout comme les moyennes et les totaux dans les grands échantillons.
Pour convertir des données en scores z , vous soustrayez la moyenne des données et divisez par l'écart type ; vous pouvez ensuite comparer les données à une distribution normale.

### Distributions à longue traine
Queue : Partie longue et étroite d'une distribution de fréquence, où des valeurs relativement extrêmes se produisent à basse fréquence.
Fausser : Où une queue d’une distribution est plus longue que l’autre.

La distribution normal est importante mais ne caracterise pas les données brutes qui sont parfois tres asymetrique
Ces données brute auront donc un qq plot avec des points en dessous et en dessus de la ligne pour des valeur faible et forte respectivement.

CCL : 
La plupart des données ne sont pas normalement distribuées.
Supposer une distribution normale peut conduire à une sous-estimation des événements extrêmes (« cygnes noirs »).

### Distribution de Student (en T)
La distribution t est en fait une famille de distributions ressemblant à la distribution normale mais avec des queues plus épaisses.
Plus l’échantillon est grand, plus la distribution t prend une forme normale.
La distribution t est largement utilisée comme base de référence pour la distribution des moyennes d'échantillon, les différences entre deux moyennes d'échantillon, les paramètres de régression, etc.


### Distribution binomiale
Procès : Un événement avecun résultat discret (par exemple, un tirage au sort).
Succès : Le résultat intéressant pour un procès
Binôme : Avoir deux résultats.
Essai binomial : Un essai avec deux résultats.
Distribution binomiale : Répartition du nombre de réussites dans x essais (Distribution de Bernoulli)

Par exemple, lancer une pièce de monnaie 10 fois est une expérience binomiale avec 10 essais, chaque essai ayant deux résultats possibles (pile ou face)
Il est classique en statistique d’appeler le résultat « 1 » le résultat de la réussite ; il est également courant d’attribuer « 1 » aux résultats les plus rares

exemple de question auquel repond une distribution de Bernoulli : Si la probabilité qu'un clic se transforme en vente est de 0,02, quelle est la probabilité d'observer 0 vente en 200 clics ?

CCL : 
Les résultats binomiaux sont importants à modéliser, car ils représentent, entre autres, des décisions fondamentales (acheter ou ne pas acheter, cliquer ou ne pas cliquer, survivre ou mourir, etc.).
Un essai binomial est une expérience avec deux résultats possibles : l’un avec une probabilité p et l’autre avec une probabilité 1 – p .
Avec n grand et à condition que p ne soit pas trop proche de 0 ou 1, la distribution binomiale peut être approximée par la distribution normale.

### Distribution du chi carré
statistique du chi carré. Il s'agit de la différence entre les valeurs observées et attendues, divisée par la racine carrée de la valeur attendue, au carré, puis additionnée pour toutes les catégories.
 Il est utile pour déterminer si plusieurs traitements (un « test A/B/C… ») diffèrent les uns des autres dans leurs effets.
si chi2 est petite, cela indique que l'ensemble de compte suit de près la distribution attendue

CCL : 
La distribution du chi carré concerne généralement le nombre de sujets ou d'éléments entrant dans des catégories.
La statistique du chi carré mesure l’ampleur de l’écart par rapport à ce à quoi on s’attendrait dans un modèle nul.

### Distribution F
imaginant si on compare differents traitements sur differents champs (qui sont nos groupes) on prend une mesure moyenne pour chaque groupe qui est sous forme de valeur continue, puis on compare ces moyennes entres elles (dans quelle mesure la difference entre deux moyenne est supperieur a une variation aleatoire normal) cette statistique generée est appelé valeur F. cette comparaison est appelé analyse de variance ANOVA.

CCL : 
La distribution F est utilisée avec des expériences et des modèles linéaires impliquant des données mesurées.
La statistique F compare la variation due aux facteurs d’intérêt à la variation globale.

### Distribution de poisson
Lambda : La vitesse (par unité de temps ou d'espace) à laquelle les événements se produisent dans un interval de temps ou d'espace specifié
La distribution de Poisson nous indique la distribution des événements (survenu d'une infection) par unité de temps ou d'espace lorsque nous échantillonnons plusieurs de ces unités

la variance d'une distribution de poisson c'est le parametre Lambda.

### Distribution exponentielle
mesure le temps entre deux evennement. 
eg, temps entre les visites d'un site Internet ou entre les voitures arrivant à un poste de péage

### Estimation du taux d'échec
Dans de nombreuses applications, le taux d'événements,lambda est connu ou peut être estimé à partir de données antérieures.

CCL : 
Pour les événements qui se produisent à un rythme constant, le nombre d'événements par unité de temps ou d'espace peut être modélisé sous la forme d'une distribution de Poisson.
Vous pouvez également modéliser le temps ou la distance entre un événement et le suivant sous forme de distribution exponentielle.
Un taux d'événements changeant au fil du temps (par exemple, une probabilité croissante de défaillance d'un appareil) peut être modélisé avec la distribution de Weibull.

























