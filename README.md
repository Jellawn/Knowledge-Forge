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

KnowledgeNode
↓
KnowledgeNodeMapper
↓
MarkdownDataValidator
↓
MarkdownExporter
↓
Fichier Markdown

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

- Création de concepts via KnowledgeNode
- Gestion des relations entre concepts
- Centralisation dans KnowledgeGraph
- Mapping des données pour l'export
- Validation des données exportables
- Génération automatique de fichiers Markdown

Prochaines étapes :

- Ingestion automatisée des connaissances
- Génération de plusieurs fiches à partir du graphe
- Enrichissement des métadonnées
- Développement de l'interface utilisateur

