# Nano App

## Getting started

You will need to clone this project, branch and work on/from your own branch.



PART A 
Qn 3 (a) head -1 survey_results.csv | awk -F',' '{print NF}'

Qn 3 (b) csvcut -c "What is the highest level of education" survey_results.csv

Qn 3 (c) awk -F',' 'NR==1 {for (i=1; i<=NF; i++) if ($i ~ /[Aa]ge/) col=i} NR>1 && $col+0 >= 23 {count++} END {print count}' survey_results.csv

Qn 3 (d) csvcut -c "Have you ever received any form of career guidance or counselling?","What areas do you feel you need the most guidance?","What features would you find most useful in an AI-based career guidance system?" survey_results.csv > survey_part.csv

Qn 4 id -u && id -g


PART C 

Qn 5
https://joyce-wandeka-nano-app.onrender.com/
#There are issues with deploying the docker image on render because I discovered an error of failure to access the survey_results.csv file. I hadn't edited its location. I fixed it but it was too late to rebuild , push and deploy the new image.

Qn (6)
A private container/image registry important because it helps with Keeping your images secure, Maintaining control over deployments, Enabling compliance and Supporting efficient CI/CD workflows