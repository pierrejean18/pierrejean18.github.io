# Extraction d'informations sur les tanks

pierrejean18.github.io


## Description du projet

Ce projet vise à automatiser l'extraction d'informations sur les tanks à partir d'une page web spécifique, en fournissant un support concret pour le secteur militaire. Les données extraites comprennent le modèle du tank, son état, ainsi que des liens vers des ressources multimédias (images ou vidéos) associées.

## Fonctionnement

Le script Python utilise les bibliothèques `requests` pour récupérer le contenu HTML de la page, et `BeautifulSoup` pour parser et naviguer dans la structure HTML. La fonction principale, `extract_tank_info`, applique des expressions régulières pour identifier et extraire les détails pertinents de chaque modèle de tank.

Le script parcourt toutes les listes non ordonnées (`<ul>`) sur la page et traite chaque élément liste (`<li>`), séparant le modèle du tank de ses caractéristiques additionnelles, comme l'état et les liens multimédias.

## Dictionnaire de données

Les informations collectées sont organisées dans un dictionnaire Python où chaque clé correspond à un modèle de tank, et les valeurs contiennent son état et les liens associés.


