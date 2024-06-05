# Precedent-Analysis
This application allows legal practitioners to extract citations or precedents for a given case description.

Paper: https://arxiv.org/abs/2406.01609

## Project:
The ability to accurately and efficiently identify relevant legal cases is critical for lawyers and legal professionals. This application aims to improve the efficiency and accuracy of legal research by using text similarity algorithms to identify potentially relevant cases for a given legal opinion. It involves extracting citations from the text of a legal opinion, computing the similarity between the extracted citations and a database of legal cases, ranking the citations by similarity, and selecting the closest matches as potential citations for the opinion. It has the potential to improve the efficiency and accuracy of legal research, potentially reducing the time and cost needed to conduct legal research, while also increasing accessibility to legal information. It has the potential to benefit lawyers, legal professionals, and individuals who need to conduct legal research. The proposed methodology can be applied in various contexts, such as drafting legal documents, advising clients, developing policies, and conducting academic research, among others.

## Motivation:
Traditionally, legal research involved manually reviewing legal documents and databases, such as court opinions, statutes, regulations, and law reviews. Lawyers and legal professionals would typically start with a broad search, using keywords and phrases related to the legal issue they are researching, and then refine their search based on the results. This process can be time-consuming and may require reviewing large volumes of legal materials to find relevant cases. Additionally, lawyers and legal professionals may consult with other lawyers or legal experts in the field to get guidance on which cases are most relevant or to identify cases that they may have missed in their initial search.

## Result:

https://github.com/AkshatMittu/Precedent-Analysis/assets/77678378/b8a06dac-deea-4984-a04b-b7bc8f7f2b8c

The final result should be the precedents of the case description that was entered along with the best citation for that case (Using Cosine Similarity) and 4 more citations that are most relevant to the case description. There is also a relevance bar that shows how much the case description is relevant to the precedents.



## About Repository:
This repository contains only the final method that was implemented for better results of the application.

-The dataset used was SCOTUS (Supreme Court of The United States), 
  Link: https://www.kaggle.com/datasets/gqfiddler/scotus-opinions
  
-The frontend part was done using Streamlit, the files generate_pdf is the code used to download the case details in a pdf format.

-The utils file has all the required modules and functions used to build this project.

- While downloading make sure the directory structure is like this:
  
        -pages
            2_Register.py
            3_Case.py
            4_About Us.py
        -1_Login.py

## Methodologies:
Methods used in this application are given below, the accuracy scores depict that the sentence embeddings performed better than all the other methods, therefore the Python files in the project contain only the code related to the best performer (Universal Sentence Encoder with Support Vector Machines).

<img src="https://github.com/AkshatMittu/Precedent-Analysis/assets/77678378/027d87cc-1c74-425f-bd56-ac763dd49da6" width="300" height="150" />
<img src="https://github.com/AkshatMittu/Precedent-Analysis/assets/77678378/67bc3709-b463-4776-8e96-32172170750b" width="400" height="150" />



