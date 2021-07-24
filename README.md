# Crawler En Python
Crawler signifie littéralement « scanner ». Autrement dit, il s’agit d’extraire un maximum d’informations possibles d’un site web. Cette analyse permet ainsi de connaître parfaitement la structure d’un site et de résoudre ses problèmes éventuels. Par exemple, une arborescence mal construite, un maillage interne inadéquat ou encore des balises meta dupliquées.

## Création D'un Projet Crawl 
Avant de créer le projet, il faut s’assurer d’avoir Scrapy installé. Utilisez la ligne de commande suivante pour l’installer :<br>
<code>
pip install scrapy
</code><br>Ou avec conda :<br>
<code>
conda install -c conda-forge scrapy
</code><br>
Maintenant nous pouvons générer notre projet avec la ligne de commande suivante :<br>
<code>scrapy startproject jumia</code><br>
**“jumia”** est le nom du projet, mais on pourrait l'appeler comme bon nous semble.

### Un Dossier jumia est créé.
![arborescence](images/arborescence.png)