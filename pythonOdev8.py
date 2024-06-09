import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1)Dosyayı okuyalım.
df = pd.read_csv("StudentsPerformance.csv")
print(df)
df.head()
df.info()
print("**********")

#2)Kadın-erkek sayısına bakalım.
gender_counts = df["gender"].value_counts()
print(gender_counts)
print("**********")

#3)Kadın-erkek sayısına histogram grafiği ile bakalım.
plt.figure(figsize=(8, 6))
gender_counts.plot(kind='bar')

plt.title("Kadın ve Erkek Sayısı")
plt.xlabel("Cinsiyet")
plt.ylabel("Sayı")
plt.xticks(rotation=0)
plt.show()
print("**********")

#4)Race/ethnicity sütununda kaç farklı grup olduğuna bakalım.
race_counts = df["race/ethnicity"].value_counts()
print(race_counts)
print("**********")

#5)Yukarıda bulduğumuzu görselleştirelim.
plt.figure(figsize=(8, 8))
race_counts.plot(kind='bar')
plt.title("Race/Ethnicity Gruplarının Dağılımı")
plt.xlabel("Gruplar")
plt.ylabel("Sayı")
plt.xticks(rotation=45)
plt.show()
print("**********")

#6)Parental level of education sütunundaki eşsiz değerleri bulalım.
parental_level_of_education = df["parental level of education"].unique()
print(parental_level_of_education)
print("**********")

#7)Lunch sütununda eşsiz değerlere ulaşalım.
lunch = df["lunch"].unique()
print(lunch)
print("**********")

#8)Lunch türlerinde kaçar kişi olduğunu bulalım.
lunch_counts = df["lunch"].value_counts()
print(lunch_counts)
print("**********")

#9)Gender sütunundaki değerler için ortalama math score,reading score,writing score değerlerini bulalım.
gender_score = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
print(gender_score)
print("**********")

#10)Race/ethnicity sütunundaki değerler için ortalama math score,reading score,writing score değerlerini bulalım.
race_score = df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean()
print(race_score)
print("**********")

#11)Parental level of education sütunundaki değerler için ortalama math score,reading score,writing score değerlerini bulalım.
parental_level_of_education_score = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
print(parental_level_of_education_score)
print("**********")

#12)Lunch sütunundaki değerler için ortalama math score, reading score, writing score değerlerini bulalım.
lunch_score = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean()
print(lunch_score)
print("**********")

#13)Test preparation course sütunundaki değerler için ortalama math score,reading score,writing score değerlerini bulalım.
test_preparation_score = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean()
print(test_preparation_score)
print("**********")

#14
a1 = df[(df["race/ethnicity"]=="group A")&(df["test preparation course"]=="none")&(df["writing score"] > 70)]
print(a1)
print("**********")

#15
max_reading_score = df["reading score"].max()
min_reading_score = df["reading score"].min()
print(max_reading_score)
print(min_reading_score)