# Knowledge Forge


Knowledge Forge est un projet expérimental dont l'objectif est de faciliter l'apprentissage en structurant les connaissances sous forme de concepts, de relations et de sources.

À terme, le projet vise à devenir un compagnon d'apprentissage capable d'ingérer des connaissances, d'en produire des résumés personnalisés et d'aider l'utilisateur à organiser, suivre et approfondir son parcours d'apprentissage.

Le projet évolue progressivement au rythme de mon apprentissage autour de Python, de l'architecture logicielle, des graphes de connaissances, du Machine Learning et de l'intelligence artificielle.


## Pourquoi ce projet ?


Knowledge Forge est conçu comme un laboratoire personnel permettant de :

- Structurer les connaissances acquises
- Comprendre les mécanismes derrière les systèmes de gestion de connaissances
- Expérimenter des concepts liés à l'intelligence artificielle
- Développer progressivement un outil réellement utile à l'apprentissage quotidien

Chaque nouvelle fonctionnalité est ajoutée dans une logique d'apprentissage et de compréhension des concepts.


## Architecture actuelle


Knowledge Forge repose actuellement sur un pipeline simple permettant de transformer une connaissance en document exploitable :

JSON
↓
JSON Reader
↓
Normalizer
↓
Knowledge Graph
├── KnowledgeNode
└── KnowledgeRelation
↓
Exploration / Export

Les connaissances sont importées depuis des sources externes, normalisées puis intégrées dans un graphe de connaissances composé de concepts (KnowledgeNode) et de relations (KnowledgeRelation). Le graphe constitue désormais le cœur du système et servira de base aux futurs mécanismes d'exploration, de génération de contenu et d'apprentissage personnalisé.

(Un premier système d'export Markdown existe également, mais il devra être réintégré proprement autour du KnowledgeGraph.)


Cette architecture permet de séparer clairement :

- Le domaine métier
- La transformation des données
- La validation
- L'export
- La persistance des fichiers

Chaque composant possède une responsabilité unique afin de faciliter l'évolution future du projet.


### Etat actuel


Version : V0.1

Fonctionnalités validées :

- Lecture de données JSON
- Normalisation des données importées
- Création de concepts via KnowledgeNode
- Création de relations via KnowledgeRelation
- Centralisation des concepts et relations dans KnowledgeGraph
- Import automatisé des relations depuis JSON
- Gestion des doublons de concepts
- Gestion des doublons de relations
- Génération d'un résumé textuel du graphe


Prochaines étapes :

- Ajouter des méthodes d'exploration du graphe
- Améliorer l'import des connaissances
- Introduire des identifiants stables pour les concepts
- Construire les premiers parcours de connaissances
- Réintégrer les mécanismes d'export
- Préparer l'architecture de la future interface utilisateur

