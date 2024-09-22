# 1. Exploratory Data Analysis (EDA):
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500)

# Veriyi Excel dosyasından okuma
df = pd.read_excel('side_effect_data 1.xlsx')

# Dataframe'in ilk ve son beş satırını görüntüleme
df.head()
df.tail()

# Dataframe'in boyutunu görüntüleme
df.shape

# Dataframe'in bilgilerini görüntüleme
df.info()

# Sütun isimlerini görüntüleme
df.columns

# Dataframe'in indeksini görüntüleme
df.index

# Sayısal verilerin istatistiksel özetini görüntüleme
df.describe().T

# Boş veri kontrolü
df.isnull().values.any()
df.isnull().sum()

# Kategorik, sayısal ve tarihsel sütunları ayırma
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["object"]]
num_cols = [col for col in df.columns if str(df[col].dtypes) in ["int64", "float64"]]
date_cols = [col for col in df.columns if str(df[col].dtypes) in ["datetime64[ns]"]]

# 2. Data Pre-Processing:

from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

# Mode imputation (en sık kullanılan değer ile doldurma)
# 'Cinsiyet', 'Il' ve 'Kan Grubu' için SimpleImputer kullanımı
mode_imputer = SimpleImputer(strategy='most_frequent')
df[['Cinsiyet', 'Il', 'Kan Grubu']] = mode_imputer.fit_transform(df[['Cinsiyet', 'Il', 'Kan Grubu']])

# Boş verileri 'None' ile doldurma
df[['Alerjilerim', 'Kronik Hastaliklarim', 'Baba Kronik Hastaliklari',
    'Anne Kronik Hastaliklari', 'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari']] = df[[
    'Alerjilerim', 'Kronik Hastaliklarim', 'Baba Kronik Hastaliklari',
    'Anne Kronik Hastaliklari', 'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari'
]].fillna('None')

# KNN Imputer kullanımı (Diğer verilere (komşulara) göre eksik verileri tahmin etme)
# 'Kilo' ve 'Boy' sütunları için
knn_imputer = KNNImputer(n_neighbors=5)
df[['Kilo', 'Boy']] = knn_imputer.fit_transform(df[['Kilo', 'Boy']])

# Sonuçları gözden geçirme
print(df.head())

# Boş verilerin kontrolü
df.isnull().sum()

from sklearn.preprocessing import LabelEncoder

# Label Encoding for 'Cinsiyet'
label_encoder = LabelEncoder()
df['Cinsiyet'] = label_encoder.fit_transform(df['Cinsiyet'])

# Sonuçları kontrol etme
print(df[['Cinsiyet']].head())

# Sonuçları gözden geçirme
print(df.head())

# 3. Visualizations:

# Yan etkilerin cinsiyete göre dağılımını görselleştirme (count plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Yan_Etki', hue='Cinsiyet', palette='Set2')
plt.title('Yan Etkilerin Cinsiyete Göre Dağılımı', fontsize=14)
plt.xlabel('Frekans', fontsize=12)
plt.ylabel('Yan Etkiler', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper right', title='Cinsiyet', fontsize=10)
plt.tight_layout()
plt.show()

# Yan etkilerin alerji türlerine göre dağılımını görselleştirme (heatmap)
heatmap_data = df.groupby(['Yan_Etki', 'Alerjilerim']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Frekans'})
plt.title('Yan Etkilerin Alerji Türlerine Göre Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Alerjiler', fontsize=14)
plt.ylabel('Yan Etkiler', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.show()


# Boy ve Kilo arasındaki ilişkiyi görselleştirme (scatter plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Boy'], y=df['Kilo'], hue=df['Kronik Hastaliklarim'], palette='coolwarm', s=100)
plt.title('Boy ve Kilonun Kronik Hastalıklara Etkisi', fontsize=14)
plt.xlabel('Boy (cm)', fontsize=12)
plt.ylabel('Kilo (kg)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Kronik Hastalıklarım', fontsize=10)
plt.subplots_adjust(right=0.75)
plt.show()

# Kan grubu ve yan etkiler arasındaki ilişkiyi görselleştirme (bar plot)
plt.figure(figsize=(10, 6))
sns.countplot(x=df['Yan_Etki'], hue=df['Kan Grubu'], palette='Set2')
plt.title('Kan Grubunun Yan Etkilere Etkisi', fontsize=14)
plt.xlabel('Yan Etkiler', fontsize=12)
plt.ylabel('Frekans', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper right', title='Kan Grubu', fontsize=10)
plt.tight_layout()
plt.show()

# Boy ve Kilo'nun yan etkilere etkisini görselleştirme (scatter plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Boy'], y=df['Kilo'], hue=df['Yan_Etki'], palette='coolwarm', s=100)
plt.title('Boy ve Kilonun Yan Etkilere Etkisi', fontsize=14)
plt.xlabel('Boy (cm)', fontsize=12)
plt.ylabel('Kilo (kg)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Yan Etkiler', fontsize=10)
plt.subplots_adjust(right=0.75)
plt.show()

