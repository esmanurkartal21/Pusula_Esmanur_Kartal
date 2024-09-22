Esmanur Kartal / esmanurkartal21@gmail.com

İLAÇ YAN ETKİLERİ VERİ ANALİZİ

GENEL BAKIŞ

Bu proje, ilaç yan etkileri, hasta demografisi ve sağlık durumlarıyla ilgili bir veri setinin analizini içerir. Analiz, Keşifsel Veri Analizi (EDA), veri ön işleme ve değişkenler arasındaki ilişkileri keşfetmek için çeşitli görselleştirmeler içerir. Yan etkiler, cinsiyet, boy, kilo ve sağlık durumları gibi faktörler arasındaki bağlantılar incelenir.

DOSYALAR

side_effect_data 1.xlsx: Hastaların ilaç kullanımı, yan etkileri, alerjileri, kronik hastalıkları ve demografik bilgilerini içeren veri seti.

pusula_esmanur_kartal.py: EDA, veri ön işleme ve görselleştirmeleri gerçekleştiren Python scripti.

PUSULA CASE STUDY SUMMARY.pdf: Projenin kod çıktılarını görüntüleyen bir pdf.

README.md: Veri analizinin ve projenin genel amacını özetleyen bir dosya.

PROJE YAPISI

1. Keşifsel Veri Analizi (EDA):

Veri setinin yapısı incelenir, eksik değerler kontrol edilir ve kategorik ve sayısal sütunlar analiz edilir.

2. Veri Ön İşleme:

Eksik değerler farklı imputation teknikleri kullanılarak doldurulmuştur:

SimpleImputer (Cinsiyet, İl ve Kan Grubu gibi kategorik sütunlar için)

KNN Imputer (Boy ve Kilo gibi sürekli değişkenler için)

Kategorik sütunlar 'None' ile doldurulmuştur.

'Cinsiyet' sütunu, sayısal analize uygun hale getirmek için Label Encoding ile dönüştürülmüştür.

3. Görselleştirmeler:
   
Verideki desenleri keşfetmek için şu görselleştirmeler oluşturulmuştur:

Yan etkilerin cinsiyete göre dağılımı için bir count plot.

Yan etkiler ve alerji türleri arasındaki ilişkiyi keşfetmek için bir heatmap.

Boy ve kilo ile kronik hastalıklar arasındaki ilişkiyi gösteren scatter plot.

Kan grubunun yan etkiler üzerindeki etkisini inceleyen bir bar plot.

Boy ve kilo arasındaki ilişkinin yan etkilere olan etkisini inceleyen scatter plot.

KURULUM VE GEREKSİNİMLER

Kodu çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

pandas

seaborn

matplotlib

scikit-learn

Bu kütüphaneleri aşağıdaki komut ile kurabilirsiniz:

pip install pandas seaborn matplotlib scikit-learn

Kodu Nasıl Çalıştırabilirsiniz:

1. Repoyu yerel bilgisayarınıza klonlayın:

git clone https://github.com/esmanurkartal21/Pusula_Esmanur_Kartal.git

2. Proje dizinine gidin:
   
cd Pusula_Esmanur_Kartal

3. Python scriptini çalıştırın:
   
python pusula_esmanur_kartal.py

Unutmayın, side_effect_data 1.xlsx dosyasını pusula_esmanur_kartal.py ile aynı dizine yerleştirmelisiniz.
