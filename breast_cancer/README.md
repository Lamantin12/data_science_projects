# Breast cancer lethality project
## Main info about data
Data taken from: [link](https://ieee-dataport.org/open-access/seer-breast-cancer-data)  
*Data contains 4024 rows of women ambulatory medical record cards*  
**The main goal of this research is to estimate their chances to survive  
If women has low chances, doctors can make desperate decisions in order to safe one's life**  
### Columns description:
* **Age** - age of patient at diagnosis
* **Race** - race of patient(White, Black, Other(AK Native, Pacific/Asian Islander))
* **Matrital Status**(Single (never married)/Married (including common law), Separated, Divorced, Widowed)
* **T Stage**
* **N Stage**
* **6th Stage**
* **Grade** (Describing how defferentiated is cancer)
* **A Stage** (If desease is regional or distant(in other organs))
* **Tumor Size**
* **Estrogen Status** (Describes if level of estrogen is high)
* **Progesterone Status** (Describes if level of progesterone is high)
* **Regional Nodes Examined** (Total number of regional lymph nodes that were removed and examined by the pathologist)
* **Regional Nodes Positive** (Exact number of regional lymph nodes examined by the pathologist that were found to contain metastases)
* **Survival Month** (Time from first survey to discharge/death)
* **Status** (Dead/Alive)  

**We'll try to predict status column**

You can find more information about data from [this](https://github.com/Lamantin12/data_science_projects/blob/master/breast_cancer/SEER%20Breast%20Cancer%20Dataset.pdf) pdf.
## Technologies used
    Data parsing and manipulation:
        - pandas
        - numpy  
    Visualization:
        - matplotlib
        - seaborn
    Modeling:  
        - sklearn
        - catboost
        - xgboost
    Dealing with inbalanced data: 
        - SMOTE
        - SMOTENC
        - ADASYN