# Nano App

## Getting started

You will need to clone this project, branch and work on/from your own branch.



PART A 
Qn 3 (a) head -1 survey.csv | awk -F',' '{print NF}'

Qn 3 (b) awk -F',' 'NR==1 {for (i=1; i<=NF; i++) if ($i ~ /[Hh]ighest level of education/) col=i} NR>1 {print $col}' survey.csv

Qn 3 (c) awk -F',' 'NR==1 {for (i=1; i<=NF; i++) if ($i ~ /[Aa]ge/) col=i} NR>1 && $col+0 >= 23 {count++} END {print count}' survey.csv

Qn 3 (d) csvcut -c "Have you ever received any form of career guidance or counselling?","What areas do you feel you need the most guidance?","What features would you find most useful in an AI-based career guidance system?" survey.csv > survey_part.csv