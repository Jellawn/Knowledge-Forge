# Knowledge Forge

Knowledge Forge est un projet expérimental visant à construire progressivement un graphe de connaissances à partir de contenus ingérés.

L’objectif de la V0.1 est simple : représenter des concepts, leurs relations, leurs sources, puis préparer une base saine pour un futur moteur d’ingestion plus avancé.

## Objectif de la V0.1

Cette première version pose les fondations métier du système :

* représenter un concept avec `KnowledgeNode`
* représenter une relation entre deux concepts avec `KnowledgeRelation`
* gérer progressivement un graphe de connaissances avec `KnowledgeGraph`
* conserver les sources associées aux connaissances
* éviter les doublons grâce à la normalisation des noms

## Structure actuelle

```txt
app/
└── domain/
    ├── knowledge_node.py
    ├── knowledge_relation.py
    └── knowledge_graph.py
```

## Principes travaillés

Ce projet sert aussi de support d’apprentissage autour de :

* la modélisation orientée métier
* les responsabilités entre objets
* les données primaires et dérivées
* la validation métier
* la normalisation des données
* la conception progressive d’un système maintenable

## Statut

Projet en cours de développement.

Version actuelle : V0.1 — fondations du domaine métier.
