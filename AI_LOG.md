# AI_LOG.md

## 1. AI Kullanım Amacı

Bu proje geliştirilirken yapay zeka, geliştiriciyi destekleyen bir yardımcı araç olarak kullanılmıştır.

AI; proje planlama, kod geliştirme, hata ayıklama, test tasarımı, dokümantasyon ve deployment sürecinde destek amacıyla kullanılmıştır.

Üretilen çıktılar doğrudan ve kontrol edilmeden kullanılmamış; lokal ortamda çalıştırılmış, test edilmiş ve proje gereksinimlerine göre değiştirilmiştir.

---

## 2. AI Kullanılan Alanlar

AI aşağıdaki konularda kullanılmıştır:

- Landing page yapısının planlanması
- Flask backend başlangıç yapısının oluşturulması
- API endpoint tasarımı
- Form validation yaklaşımının oluşturulması
- HTML/CSS/JavaScript geliştirme desteği
- Veritabanı yapısının planlanması
- Otomatik test senaryolarının oluşturulması
- Hata mesajlarının düzenlenmesi
- Deployment sorunlarının analiz edilmesi
- README.md hazırlanması
- Test ve geliştirme sürecinin dokümante edilmesi

---

## 3. Başlangıçtaki Teknik Yaklaşım

İlk geliştirme aşamasında küçük ölçekli prototip için SQLite kullanılmıştır.

Bu yaklaşım lokal geliştirme ve ilk testler sırasında kullanılmıştır.

Ancak deployment aşamasında uygulamanın kalıcı ve erişilebilir bir PostgreSQL veritabanına bağlanması gerektiği değerlendirilmiştir.

Bu nedenle veritabanı yapısı PostgreSQL/Supabase'e geçirilmiştir.

---

## 4. AI Çıktılarının Uyarlanması

AI tarafından önerilen kodlar proje gereksinimlerine göre kontrol edilmiş ve gerekli yerlerde değiştirilmiştir.

Örneğin:

- API doğrulama kuralları proje gereksinimlerine göre düzenlenmiştir.
- İzin verilen hizmetler açık bir liste/set üzerinden kontrol edilmiştir.
- SQL sorgularında parametreli kullanım tercih edilmiştir.
- Başarı mesajının yalnızca veritabanı kaydı başarılı olduktan sonra gösterilmesi sağlanmıştır.
- Loading, success ve error durumları frontend akışına eklenmiştir.
- Testler gerçek veritabanına bağımlı olmayacak şekilde mock kullanılarak düzenlenmiştir.

---

## 5. Deployment Sırasında Karşılaşılan Hata

PostgreSQL'e geçişten sonra Render üzerinde ilk deployment sırasında veritabanı bağlantı kodunda bir hata oluşmuştur.

Eski SQLite yaklaşımından kalan kodda bağlantı nesnesi üzerinde doğrudan `execute()` kullanılmıştır.

Render loglarında aşağıdaki hata görülmüştür:

```text
AttributeError: 'psycopg2.extensions.connection' object has no attribute 'execute'
```

Sorunun PostgreSQL bağlantısında cursor kullanımının gerekli olmasından kaynaklandığı tespit edilmiştir.

Kod aşağıdaki yapıya uyarlanmıştır:

```python
connection = get_db_connection()
cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO requests
    (name, email, service, description)
    VALUES (%s, %s, %s, %s)
    """,
    (name, email, service, description)
)

connection.commit()
```

Düzeltmeden sonra uygulama Render üzerinde tekrar deploy edilmiş ve canlı duruma geçmiştir.

---

## 6. Test Süreci

Kod değişiklikleri lokal ortamda test edilmiştir.

Otomatik testlerde dört farklı senaryo bulunmaktadır:

1. Geçerli talep
2. Geçersiz e-posta
3. Geçersiz hizmet
4. Kısa açıklama

Son test sonucu:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.011s

OK
```

Geçerli talep testinde gerçek PostgreSQL bağlantısı yerine `unittest.mock` kullanılmıştır.

Bu sayede test:

- HTTP endpoint davranışını,
- başarılı response'u,
- SQL `execute()` çağrısını,
- veritabanı `commit()` çağrısını

kontrol edebilmektedir.

---

## 7. Canlı Ortam Doğrulaması

Otomatik testlerin yanında canlı uygulama üzerinde manuel test gerçekleştirilmiştir.

**Canlı uygulama:**

https://enteksis-task.onrender.com

Kurgusal test verileri kullanılarak form gönderilmiştir.

Başarılı form gönderiminden sonra:

```text
Talebiniz başarıyla kaydedildi.
```

mesajı gösterilmiştir.

Ardından Supabase Table Editor üzerinden kayıt kontrol edilmiş ve form verisinin PostgreSQL veritabanına gerçekten kaydedildiği doğrulanmıştır.

Bu kontrol ile aşağıdaki uçtan uca akış doğrulanmıştır:

```text
Frontend
   ↓
JavaScript fetch()
   ↓
Flask API
   ↓
Server validation
   ↓
PostgreSQL / Supabase
   ↓
Successful response
   ↓
Frontend success message
```

---

## 8. AI Çıktılarının Doğrulanması

AI tarafından önerilen kodların çalıştığı yalnızca metinsel olarak kabul edilmemiştir.

Doğrulama için:

- Uygulama lokal ortamda çalıştırılmıştır.
- Otomatik testler çalıştırılmıştır.
- Form gönderimleri yapılmıştır.
- Client-side validation kontrol edilmiştir.
- Server-side validation kontrol edilmiştir.
- Render deployment logları incelenmiştir.
- Canlı uygulama üzerinden form gönderilmiştir.
- Supabase üzerinde oluşan kayıt kontrol edilmiştir.

Bu kontroller sonucunda gerekli görülen kod değişiklikleri yapılmıştır.

---

## 9. Kullanılmayan / Değiştirilen Öneriler

Geliştirme sürecinde AI tarafından önerilen yaklaşımlar doğrudan kabul edilmemiştir.

Özellikle başlangıçta kullanılan SQLite yaklaşımı deployment gereksinimleri nedeniyle PostgreSQL/Supabase yapısına geçirilmiştir.

Ayrıca testlerde gerçek veritabanına bağımlılık yerine mock kullanılması tercih edilmiştir.

Bu kararların amacı testleri daha izole ve tekrarlanabilir hale getirmektir.

---

## 10. Kişisel Katkı

Geliştirici tarafından:

- Gereksinimler analiz edilmiştir.
- Teknoloji seçimi yapılmıştır.
- Proje dosya yapısı oluşturulmuştur.
- Kodlar çalıştırılmıştır.
- Hatalar incelenmiştir.
- Deployment süreci yönetilmiştir.
- Veritabanı bağlantısı kurulmuştur.
- Testler çalıştırılmıştır.
- Canlı uygulama kontrol edilmiştir.
- Supabase kayıtları doğrulanmıştır.
- AI tarafından üretilen çıktılar proje gereksinimlerine göre değiştirilmiştir.

AI, geliştirme sürecinde yardımcı araç olarak kullanılmıştır; nihai kararlar ve doğrulamalar geliştirici tarafından yapılmıştır.

---

## 11. Test Verileri

Projede yalnızca kurgusal test verileri kullanılmıştır.

Örnek:

```text
Ad Soyad: Test Kullanıcısı
E-posta: test@example.com
Hizmet: Görev Otomasyonu
```

Gerçek kişisel veri kullanılmamıştır.

---

## 12. Proje Gereksinimlerinin Kontrolü

Değerlendirme çalışmasında belirtilen temel gereksinimler kontrol edilmiştir:

- [x] Teknoloji hizmetini açıklayan landing page
- [x] Problem ve sağlanan değer açıklaması
- [x] Mobil ve masaüstü responsive tasarım
- [x] Ad Soyad alanı
- [x] E-posta alanı
- [x] Hizmet seçimi
- [x] Açıklama alanı
- [x] Client-side validation
- [x] Server-side validation
- [x] Loading durumu
- [x] Success durumu
- [x] Error durumu
- [x] Server-side kalıcı kayıt
- [x] Başarılı kayıt sonrası success mesajı
- [x] Otomatik testler
- [x] Canlı deployment
- [x] README.md
- [x] AI_LOG.md
- [x] Git commit geçmişi

---

## 13. Sonuç

AI desteğiyle geliştirilen kod ve dokümantasyon, uygulama çalıştırılarak ve test edilerek doğrulanmıştır.

Özellikle PostgreSQL'e geçiş, Render deployment hatasının çözülmesi, otomatik testlerin çalıştırılması ve canlı veritabanı kaydının doğrulanması geliştirme sürecinin önemli kontrol noktaları olmuştur.

Proje, değerlendirme amacıyla hazırlanmış çalışan bir prototip olarak teslim edilmektedir.