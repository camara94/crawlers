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

### scrapy.py
La racine du projet contient le fichier scrapy.cfg qui est un fichier de configuration qui contient des variables telles que le nom du module qui contient les paramètres du projet et d’autres variables de déploiement.
### &#95;&#95;init&#95;&#95;.py
La racine contient un autre dossier datasets qui contient le projet en lui même. Ce dossier qui est un package Python (d’où le __init__.py) contient le package spiders (qui pour l’heure est vide) ainsi que les modules : **items**, **middlewares**, **pipelines** et **settings**.

### Le Fichier middlewares.py 
Le module **middlewares** contient les middlewares du projet. Les middlewares pour les spiders et pour le downloader sont créés par défaut. Mais il est possible d’en créer un nouveau.

### Le Fichier items.py
Le module **items** définit les modèles des données que doivent respecter les items scrapés. Un item est un objet Python style **“clé-valeur”** qui représente un échantillon élémentaire du jeu de données. Si on considère notre jeu de données comme étant au format **CSV**, un item serait une ligne de ce **CSV**.

### Le Fichier pipelines.py
Le module **pipelines** contient les pipelines pour chaque item (modèle de données) défini dans le module items. Ces pipelines permettent de faire des traitements sur l’ensemble des items scrapés. Cela est pratique pour faire du nettoyage de données.

### Le Fichier settings.py
Le fichier **settings.py** contient des variables qui sont utilisées par l’engine et le reste du projet.

## Création D’Un Item
On commence par créer le modèle de données qu’on veut. On fait cela en créant une classe qui hérite de **“scrapy.Item”** et précisant les 3 champs qu’on souhaite avoir.

<pre>
<code>
import scrapy
 
class ReviewsAllocineItem(scrapy.Item):
    designation = scrapy.Field()
    image = scrapy.Field() 
    prix = scrapy.Field()
</code>
</pre>