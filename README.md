## How to load data from GDC ? (tcga_data_download.R)
<div style="display: flex;">
    <img src="https://github.com/dinaOuahbi/Statistical-issues/blob/main/results/methData.png" width="350" height="400">
    <img src="https://github.com/dinaOuahbi/Statistical-issues/blob/main/results/mafData.png" width="350" height="400">
</div>

## Survival analysis (KM_survival.R)
La proba pour que des patients survivent apres un certains temps t qui est le temps consacré à l'etude de ses patients. 
nous cherchons les variables qui peuvent influencer la survie globale ou sans progression
calcule du taux d'occurence d'un evennement (la mort par exemple) durant un delai

### A quoi repend on dans une analyse de survie ? 
- la proba pour qu'un patient survie apres 5 ans
- quel sont les facteurs qui influence la survie
- quel est le traitement le plus efficasse en comparant deux groupes de patients ayant pris deux trt differents
- quel sont les facteurs qui ont contribuer a differentier la survie entre differents subtype de cancer


### La censure
un type de données manquantes
un patient est censurer quand nous n'avons pas de données sur sa survie
car l'evennement etudier (la mort) peut ne pas etre observer chez certains patients (le patient a quitté l'etude, ...)
la censure est importante car elle influence sur l'estimation de la survie ainsi que le hazard ratio

### les differents evennement
- la mort
- la progression
- la rechute
- les metastases
- l'hospitalisation

  ### les methode de l'analyse de survie
  - km : visualiser la courbe de survie
  - log rank test : compare deux courbe de survie de deux groupes de patients
  - cox ph : decrit l'effet d'une variable sur la survie
 
  ### comment lire une curbe KM
  ![KM explanation](https://github.com/dinaOuahbi/Statistical-issues/blob/main/data/1-s2.0-S0022202X15373292-gr2_lrg.jpg)

### Notre question relative au script {}
Est ce qu'une expression elevée de TP53 influence le pronostique chez des patients atteint de cancer de sein ? 



































  
