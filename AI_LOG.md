# AI_LOG – FlowTask

## 1. Proje ve AI Kullanım Amacı

Bu proje, verilen teknik değerlendirme görevi kapsamında geliştirilmiş kurgusal bir teknoloji hizmeti landing page uygulamasıdır.

Geliştirme sürecinde yapay zeka, kodlama ve problem çözme sürecini destekleyen bir yardımcı araç olarak kullanılmıştır.

AI kullanımındaki temel amaçlar:

* Proje yapısının planlanması
* Backend başlangıç kodunun oluşturulması
* Frontend yapısının hazırlanması
* Form doğrulama yaklaşımının oluşturulması
* Test senaryolarının planlanması
* Dokümantasyonun hazırlanması

AI tarafından üretilen çıktılar doğrudan kabul edilmemiş, lokal ortamda çalıştırılarak doğrulanmıştır.

## 2. Kullanılan AI Aracı

Geliştirme sürecinde ChatGPT kullanılmıştır.

ChatGPT özellikle kod üretimi, hata ayıklama, test senaryoları ve dokümantasyon konusunda yardımcı araç olarak kullanılmıştır.

## 3. Görev Dağılımı

### AI tarafından yapılanlar

AI aşağıdaki konularda öneriler ve başlangıç kodları sağlamıştır:

* Flask + SQLite mimarisinin önerilmesi
* `app.py` için Flask API başlangıç kodu
* HTML landing page yapısı
* Responsive CSS yapısı
* JavaScript form gönderimi
* Client-side ve server-side validation yaklaşımı
* SQLite kayıt yapısı
* Otomatik test dosyası için başlangıç kodu
* README ve AI_LOG dokümantasyonu

### Geliştirici tarafından yapılanlar

Geliştirici tarafından:

* Görev gereksinimleri incelenmiştir.
* Proje yapısı oluşturulmuştur.
* Kodlar lokal ortamda çalıştırılmıştır.
* Form davranışları manuel olarak test edilmiştir.
* Veritabanı kayıtları kontrol edilmiştir.
* Client-side validation kontrol edilmiştir.
* Server-side validation doğrudan API isteğiyle test edilmiştir.
* Otomatik testler çalıştırılmıştır.
* AI çıktıları proje gereksinimlerine göre kontrol edilmiştir.
* Dokümantasyon ve teslim yapısı hazırlanmıştır.

## 4. Kabul Edilen Öneriler

### Flask + SQLite

AI tarafından küçük ölçekli proje için Flask ve SQLite kullanılması önerilmiştir.

Bu yaklaşım kabul edilmiştir.

Gerekçe:

* Projenin kapsamı küçük olduğu için yeterlidir.
* Kurulumu basittir.
* Server-side kayıt gereksinimini karşılar.
* Harici veritabanı servisi gerektirmez.

### Client-side + Server-side Validation

Her iki tarafta da doğrulama uygulanması önerilmiştir.

Bu yaklaşım kabul edilmiştir.

Client-side validation kullanıcı deneyimini iyileştirirken server-side validation istemciden bağımsız güvenlik kontrolü sağlar.

### Parametreli SQL

SQL sorgularında parametre kullanılması önerilmiştir ve kabul edilmiştir.

Örnek:

```python
connection.execute(
    """
    INSERT INTO requests
    (name, email, service, description)
    VALUES (?, ?, ?, ?)
    """,
    (name, email, service, description)
)
```

## 5. Değiştirilen / Uyarlanan Çıktılar

AI tarafından oluşturulan başlangıç kodları proje gereksinimlerine göre uyarlanmıştır.

Örneğin:

* Hizmet seçenekleri FlowTask senaryosuna göre belirlenmiştir.
* Form alanlarının karakter sınırları belirlenmiştir.
* Kullanıcı mesajları Türkçe hazırlanmıştır.
* Landing page metinleri kurgusal hizmete göre oluşturulmuştur.
* API endpoint'i `/api/requests` olarak yapılandırılmıştır.
* Veritabanı alanları talep formuna göre belirlenmiştir.
* Responsive tasarım mobil ekranlara göre düzenlenmiştir.
* Test senaryoları mevcut API davranışına göre düzenlenmiştir.

## 6. Doğrulama Süreci

AI tarafından oluşturulan kodların çalıştığını kontrol etmek için birden fazla doğrulama yapılmıştır.

### 6.1 Uygulamanın çalıştırılması

Flask uygulaması lokal ortamda çalıştırılmıştır:

```text
python app.py
```

Uygulama:

```text
http://127.0.0.1:5000
```

adresinde açılmıştır.

Landing page tarayıcıda görüntülenmiştir.

### 6.2 Başarılı form testi

Kurgusal test verileriyle form gönderilmiştir.

Örnek:

```text
Ad Soyad: test kullanıcısı
E-posta: test@example.com
Hizmet: Görev Otomasyonu
```

Başarılı API isteğinde:

```text
HTTP 201 Created
```

yanıtı alınmıştır.

Talebin SQLite veritabanına kaydedildiği ayrıca kontrol edilmiştir.

### 6.3 Client-side validation testi

E-posta alanına geçersiz bir format girilmiştir.

Tarayıcının yerleşik form doğrulaması isteğin gönderilmesini engellemiş ve kullanıcıya geçersiz e-posta formatı mesajı gösterilmiştir.

### 6.4 Server-side validation testi

Client-side kontrollerinden bağımsız olarak API endpoint'ine geçersiz e-posta verisi gönderilmiştir.

Sunucu:

```text
HTTP 400 Bad Request
```

yanıtı vermiştir.

Bu sonuç server-side validation'ın çalıştığını doğrulamıştır.

### 6.5 SQLite kayıt kontrolü

Başarılı form gönderiminden sonra SQLite veritabanındaki kayıtlar Python ile kontrol edilmiştir.

Kayıtların veritabanında tutulduğu doğrulanmıştır.

## 7. Otomatik Testler

Ek olarak `test_app.py` isimli bir test dosyası oluşturulmuştur.

Testler Flask test istemcisi kullanılarak çalıştırılmıştır.

Çalıştırılan komut:

```text
python -m unittest test_app.py
```

Test edilen senaryolar:

1. Geçerli talep oluşturma
2. Geçersiz e-posta
3. Geçersiz hizmet
4. Kısa açıklama

Sonuç:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.041s

OK
```

Dört testin tamamı başarıyla geçmiştir.

## 8. Karşılaşılan Gerçek Problem

Server-side validation testi sırasında ilk olarak PowerShell üzerinden JSON veri gönderilmeye çalışılmıştır.

PowerShell komut satırındaki JSON/tırnaklama nedeniyle istek beklenen biçimde oluşturulamamıştır.

Bu nedenle ilk deneme API'nin beklenen validation sonucunu doğrudan göstermemiştir.

Sorunu çözmek için aynı endpoint Python `urllib` kullanılarak test edilmiştir.

Python ile yapılan test sonucunda geçersiz e-posta isteği:

```text
HTTP 400 Bad Request
```

ile reddedilmiştir.

Bu şekilde server-side validation'ın gerçekten çalıştığı doğrulanmıştır.

Herhangi bir hata uydurulmamış; yalnızca geliştirme sırasında gerçekten karşılaşılan problem kaydedilmiştir.

## 9. AI Çıktılarının Kontrolü

AI tarafından oluşturulan kodlar aşağıdaki yöntemlerle kontrol edilmiştir:

* Lokal uygulama çalıştırma
* Tarayıcı üzerinden manuel form testi
* Client-side validation testi
* API endpoint testi
* SQLite kayıt kontrolü
* Otomatik unittest testleri

AI çıktısı çalıştırılmadan veya kontrol edilmeden doğru kabul edilmemiştir.

## 10. Kişisel Kararlar

Projenin küçük ve değerlendirme odaklı olması nedeniyle:

* React yerine HTML/CSS/JavaScript tercih edilmiştir.
* Büyük bir veritabanı sistemi yerine SQLite tercih edilmiştir.
* Gereksiz üçüncü taraf servislerden kaçınılmıştır.
* Kapsamın 3–4 saatlik hedef çalışma süresinde tamamlanabilmesi amaçlanmıştır.
* Gerçek kişisel veri kullanılmamıştır.
* Uygulama kurgusal bir teknoloji hizmeti olarak tasarlanmıştır.

Bu kararlar projenin temel gereksinimlerini mümkün olduğunca sade bir mimariyle karşılamak amacıyla alınmıştır.

## 11. Bilinen Sınırlamalar

Proje değerlendirme amacıyla hazırlanmış küçük ölçekli bir prototiptir.

Bu nedenle:

* Kullanıcı hesabı bulunmamaktadır.
* Yönetici paneli bulunmamaktadır.
* E-posta bildirim sistemi bulunmamaktadır.
* İleri seviye rate limiting uygulanmamıştır.
* CSRF gibi üretim ortamına yönelik ek güvenlik katmanları bulunmamaktadır.
* SQLite yüksek trafikli üretim sistemi için tasarlanmamıştır.

Bu özellikler görev kapsamının dışında bırakılmıştır.

## 12. Çalışma Süresi

Proje geliştirme süreci yaklaşık 3–4 saatlik aktif çalışma hedefi doğrultusunda yürütülmüştür.

Süre; geliştirme, test, hata ayıklama ve dokümantasyon aşamalarını kapsamaktadır.

## 13. Sonuç

AI, bu projede geliştiricinin yerine geçen bir sistem olarak değil, geliştirme sürecini hızlandıran ve teknik kararları destekleyen bir yardımcı araç olarak kullanılmıştır.

AI tarafından önerilen kodlar proje gereksinimlerine göre değerlendirilmiş, gerekli yerlerde değiştirilmiş ve çalıştırılarak doğrulanmıştır.

Son ürünün çalışması; manuel testler, API testleri, SQLite kontrolleri ve dört otomatik test ile doğrulanmıştır.
