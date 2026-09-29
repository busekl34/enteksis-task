# FlowTask – İşletmeler İçin Görev Otomasyonu

FlowTask, işletmelerin tekrar eden görevlerini, müşteri taleplerini ve iş akışlarını daha düzenli şekilde yönetmesine yardımcı olmak amacıyla geliştirilmiş kurgusal bir teknoloji hizmeti landing page uygulamasıdır.

Bu proje değerlendirme amacıyla hazırlanmıştır ve ticari kullanım amacı taşımaz.

## Proje Hakkında

FlowTask, işletmelerin otomasyon ihtiyaçlarını iletebildiği basit ve responsive bir web uygulamasıdır.

Kullanıcı aşağıdaki bilgileri girerek bir otomasyon talebi oluşturabilir:

* Ad Soyad
* E-posta
* Hizmet seçimi
* İhtiyaç açıklaması

Form gönderildiğinde veriler önce sunucu tarafında doğrulanır. Doğrulama başarılı olursa talep SQLite veritabanına kaydedilir. Kayıt başarılı olduktan sonra kullanıcıya başarı mesajı gösterilir.

## Kullanılan Teknolojiler

* Python 3
* Flask
* SQLite
* HTML5
* CSS3
* JavaScript
* unittest
* Git / GitHub

## Proje Yapısı

```text
enteksis-task/
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
├── AI_LOG.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

`requests.db` dosyası uygulama çalışırken otomatik olarak oluşturulur ve `.gitignore` içerisinde tutulduğu için Git deposuna gönderilmez.

## Temel Özellikler

* Responsive landing page
* Mobil ve masaüstü uyumlu tasarım
* Teknoloji hizmeti tanıtım alanı
* Otomasyon talep formu
* Hizmet seçimi
* Client-side form validation
* Server-side form validation
* Loading durumu
* Başarı durumu
* Hata durumu
* SQLite üzerinde veri saklama
* Otomatik API testleri
* Parametreli SQL sorguları
* Kullanıcı dostu hata mesajları

## Kurulum

### 1. Projeyi indirme

Projeyi GitHub üzerinden indirdikten sonra proje klasörüne girin.

### 2. Sanal ortam oluşturma

Windows:

```bash
python -m venv venv
```

Sanal ortamı etkinleştirmek için:

```bash
venv\Scripts\activate
```

### 3. Gerekli paketleri yükleme

```bash
pip install -r requirements.txt
```

### 4. Uygulamayı çalıştırma

```bash
python app.py
```

Uygulama çalıştıktan sonra tarayıcıdan:

```text
http://127.0.0.1:5000
```

adresine gidilebilir.

## Veri Akışı

Uygulamadaki temel veri akışı şu şekildedir:

```text
Kullanıcı
   ↓
HTML Formu
   ↓
Client-side Validation
   ↓
JavaScript fetch()
   ↓
POST /api/requests
   ↓
Flask Server
   ↓
Server-side Validation
   ↓
SQLite
   ↓
Başarılı kayıt
   ↓
API Response
   ↓
Kullanıcıya başarı mesajı
```

Başarılı veritabanı kaydı gerçekleşmeden kullanıcıya başarılı işlem mesajı gösterilmez.

## Form Doğrulama

Hem istemci hem de sunucu tarafında doğrulama uygulanmıştır.

### Ad Soyad

* Boş bırakılamaz.
* Minimum 2 karakter olmalıdır.
* Maksimum 100 karakter olabilir.

### E-posta

* Boş bırakılamaz.
* Geçerli bir e-posta formatında olmalıdır.
* Maksimum 150 karakter olabilir.

### Hizmet

Sadece aşağıdaki hizmetlerden biri seçilebilir:

* Görev Otomasyonu
* Talep Yönetimi
* İş Akışı Entegrasyonu

### Açıklama

* Boş bırakılamaz.
* Minimum 10 karakter olmalıdır.
* Maksimum 1000 karakter olabilir.

Sunucu tarafındaki doğrulama, istemci tarafındaki kontrollerin atlanması durumunda da verilerin kontrol edilmesini sağlar.

## Testler

Projede Flask test istemcisi kullanılarak otomatik testler hazırlanmıştır.

Testleri çalıştırmak için:

```bash
python -m unittest test_app.py
```

Test edilen senaryolar:

1. Geçerli talep oluşturma
2. Geçersiz e-posta
3. Geçersiz hizmet seçimi
4. Kısa açıklama

Son başarılı test sonucu:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.041s

OK
```

Dört testin tamamı başarıyla geçmiştir.

## Manuel Testler

Otomatik testlerin yanında uygulama lokal ortamda manuel olarak da kontrol edilmiştir.

### Başarılı form gönderimi

Kurgusal test verileri kullanılarak form gönderilmiş ve:

```text
HTTP 201 Created
```

yanıtı alınmıştır.

Talep SQLite veritabanına kaydedilmiştir.

### Client-side validation

Geçersiz e-posta formatı girildiğinde tarayıcının yerleşik form doğrulaması tarafından istek engellenmiştir.

### Server-side validation

Geçersiz e-posta adresi ile API endpoint'ine doğrudan istek gönderilmiştir.

Sunucu:

```text
HTTP 400 Bad Request
```

yanıtı vermiştir.

Bu test, sunucu tarafındaki doğrulamanın client-side validation'dan bağımsız olarak çalıştığını göstermektedir.

## Veritabanı

Uygulama SQLite kullanmaktadır.

Veritabanındaki `requests` tablosunda aşağıdaki alanlar bulunmaktadır:

* `id`
* `name`
* `email`
* `service`
* `description`
* `created_at`

SQL sorgularında parametre kullanılmıştır:

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

Bu yaklaşım kullanıcı girdilerinin SQL sorgusuna doğrudan eklenmesini önler.

## Kullanılabilirlik ve Erişilebilirlik

Uygulamada temel erişilebilirlik ve kullanılabilirlik prensiplerine dikkat edilmiştir.

* Form alanları için `label` elementleri kullanılmıştır.
* Gerekli alanlar `required` ile belirtilmiştir.
* Form durum mesajı `aria-live="polite"` ile tanımlanmıştır.
* Klavye ile odaklanma durumları için görünür focus stilleri bulunmaktadır.
* Responsive tasarım uygulanmıştır.
* Mobil ekranlarda içerikler tek sütunlu yapıya geçmektedir.
* Gönderim sırasında buton devre dışı bırakılarak tekrar tekrar gönderim engellenmektedir.
* Loading, success ve error durumları kullanıcıya açık şekilde gösterilmektedir.

## Hata Yönetimi

API tarafında temel hata durumları ele alınmıştır.

Örneğin:

* Eksik veri → `400`
* Geçersiz e-posta → `400`
* Geçersiz hizmet → `400`
* Geçersiz açıklama → `400`
* Veritabanı hatası → `500`
* Başarılı kayıt → `201`

Kullanıcıya teknik hata ayrıntıları yerine anlaşılır hata mesajları gösterilmektedir.

## Güvenlik

Projede temel güvenlik kontrolleri uygulanmıştır:

* Server-side input validation
* İzin verilen hizmetlerin kontrol edilmesi
* SQL sorgularında parametre kullanılması
* Veritabanı dosyasının Git deposuna dahil edilmemesi
* Gerçek kişisel veri kullanılmaması
* `.env` dosyasının Git dışında tutulması

## Test Verisi

Projede yalnızca kurgusal test verileri kullanılmıştır.

Örnek test verisi:

```text
Ad Soyad: test kullanıcısı
E-posta: test@example.com
Hizmet: Görev Otomasyonu
```

Gerçek kişilere ait kişisel veriler kullanılmamıştır.

## Yapay Zeka Kullanımı

Projenin geliştirme sürecinde yapay zeka, geliştiriciyi destekleyen bir yardımcı araç olarak kullanılmıştır.

AI aşağıdaki konularda kullanılmıştır:

* Proje mimarisinin planlanması
* Flask backend başlangıç kodunun oluşturulması
* SQLite veri modeli
* HTML/CSS/JavaScript başlangıç yapısı
* Form doğrulama yaklaşımı
* Test senaryolarının oluşturulması
* README ve AI kullanım günlüğünün hazırlanması

Üretilen kodlar doğrudan kabul edilmemiş; lokal ortamda çalıştırılarak kontrol edilmiştir.

AI tarafından önerilen Flask + SQLite yapısı proje kapsamına uygun olduğu için kabul edilmiştir.

Kodlar proje gereksinimlerine göre uyarlanmış ve test edilmiştir.

Detaylı AI kullanım süreci `AI_LOG.md` dosyasında açıklanmaktadır.

## Hazır Şablon / Açık Kaynak Kullanımı

Projenin landing page tasarımı herhangi bir hazır web şablonundan alınmamıştır.

HTML, CSS ve JavaScript yapısı proje kapsamında oluşturulmuştur.

Harici bir ticari tema veya hazır UI şablonu kullanılmamıştır.

## Bilinen Eksikler ve Kapsam Sınırları

Bu proje değerlendirme amacıyla hazırlanmış küçük ölçekli bir prototiptir.

Bilinen kapsam sınırlamaları:

* Kullanıcı hesabı ve giriş sistemi bulunmamaktadır.
* E-posta bildirim sistemi bulunmamaktadır.
* Yönetici paneli bulunmamaktadır.
* Gelişmiş rate limiting uygulanmamıştır.
* CSRF koruması gibi üretim ortamına yönelik ileri seviye web güvenlik katmanları bulunmamaktadır.
* SQLite küçük ölçekli değerlendirme için kullanılmıştır; yüksek trafikli üretim ortamları için daha gelişmiş bir veritabanı tercih edilmelidir.
* Uygulama gerçek müşteri verileri veya ticari işlemler için tasarlanmamıştır.

Bu sınırlamalar projenin değerlendirme kapsamını küçük ve yönetilebilir tutmak amacıyla kabul edilmiştir.

## Kişisel Katkı

Projenin geliştirme sürecinde geliştirici tarafından:

* Proje gereksinimleri değerlendirilmiş,
* Kullanılacak teknoloji yaklaşımı seçilmiş,
* Kodlar lokal ortamda çalıştırılmış,
* Form ve API davranışları test edilmiş,
* SQLite kayıtları kontrol edilmiş,
* Client-side ve server-side validation test edilmiştir,
* Otomatik testler çalıştırılmış,
* Hatalı test senaryoları doğrulanmış,
* AI tarafından oluşturulan çıktılar kontrol edilip proje gereksinimlerine göre uyarlanmıştır.

AI, geliştirme sürecinde yardımcı araç olarak kullanılmış; sonucun çalıştığı geliştirici tarafından uygulama ve testlerle doğrulanmıştır.

## Proje Durumu

Proje değerlendirme amacıyla hazırlanmış çalışan bir prototiptir.

Temel kullanıcı akışı:

```text
Landing Page
     ↓
Hizmet seçimi
     ↓
Talep formu
     ↓
Client validation
     ↓
Server validation
     ↓
SQLite kayıt
     ↓
Başarı mesajı
```

Proje ticari kullanım amacı taşımaz.
