# SUD_Naija-NSC

# Summary

A Surface Syntactic Universal Dependencies corpus for spoken Naija (Nigerian Pidgin).

# Introduction

The corpus is based on dialogues and monologues and comprises 9,242 sentences and 140,729 tokens.

Sentences are annotated with the following metadata :
+ sent_id (which also indicates the sample file)
+ text
+ text_en (English translation)
+ text_ortho (A simplified version of text where macrosyntactic annotation has been replaced by standard punctuation)
+ speaker_id (from the NaijaSynCor Metadata)
+ sound_url (links to the corresponding sound file, AlignBegin and AlignEnd features give the miliseconds that allow for a positioning in the soundfile)

# Structure

The text has been transcribed mostly following English spelling conventions for lexical words. Grammatical words have been transcribed following consensual conventions elaborated by the annotators.

The text is segmented into illocutionary units. The end of illocutionary units is indicated by a double slash (//). The sentence nucleus containing the predicate is separated from dislocated units by "lesser than" signs (<) from left-dislocated elements, and by "greater than" signs (>) from right-dislocated units. Paradigmatic lists (coordinations, appositions, and disfluencies) are marked with curly breackets, each conjunct being separated by the pipe symbol (|). Further details can be found on the "Macrosyntactic annotation guide".

The treebank is developed in SUD (https://surfacesyntacticud.github.io/) and is converted automatically into [SUD_Naija-NSC](https://github.com/UniversalDependencies/UD_Naija-NSC).

# Acknowledgments

The treebank was created within the NaijaSynCor project, directed by Bernard Caron and funded by the ANR, the French National Research Agency.

This corpus is a pilot for the larger corpus elaborated as part of the NaijaSynCor Project (Projet-ANR-16-CE27-0007). Its main aim is to elaborate and test the annotation and procedures that are used in the ANR-project. It will be part of a larger 500kW corpus that will be projected on prosodic and information structures and analysed for sociolinguistics variation (http://naijasyncor.huma-num.fr/).

The pilot corpus was recorded in various locations in Ibadan (Nigeria) by Bukola Babalola and Opeyemi Lewis. It was transcribed, translated and tagged manually using Elan-Corpa (http://llacan.vjf.cnrs.fr/res_ELAN-CorpA_en.php) by Folakemi Ladoja, Emeka Onwuegbuzia, Biola Oyelere and Samson Tella under the supervision of Bernard Caron. It was converted to CONLL by Mourad Aouini. First annotations were done by Marine Courtin and Sandra Bellato, who developed the guidelines under the supervision of Sylvain Kahane, Bernard Caron, and Kim Gerdes.The final Universal dependencies annotations have been manually checked by Chika Kennedy Ajede, Emeka Onwuegbuzia, and Samson Tella under the supervision of Bernard Caron using the processing chain developed by Kim Gerdes and Bruno Guillaume, based on the Arborator (https://arborator.ilpga.fr) and Grew (http://grew.fr). Marine Courtin, Kim Gerdes, Bruno Guillaume, Kirian Guillier, Sylvain Kahane, Mariam Nakhlé, Yuchen Song, Emmett Strickland, Manying Zhang have helped in the correction process.

