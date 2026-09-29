import unittest

from app import app


class FlowTaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_valid_request(self):
        response = self.client.post(
            "/api/requests",
            json={
                "name": "Test Kullanıcısı",
                "email": "test@example.com",
                "service": "Görev Otomasyonu",
                "description": "Müşteri taleplerini otomatikleştirmek istiyorum."
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_invalid_email(self):
        response = self.client.post(
            "/api/requests",
            json={
                "name": "Test Kullanıcısı",
                "email": "gecersiz-email",
                "service": "Görev Otomasyonu",
                "description": "Müşteri taleplerini otomatikleştirmek istiyorum."
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_invalid_service(self):
        response = self.client.post(
            "/api/requests",
            json={
                "name": "Test Kullanıcısı",
                "email": "test@example.com",
                "service": "Geçersiz Hizmet",
                "description": "Müşteri taleplerini otomatikleştirmek istiyorum."
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_short_description(self):
        response = self.client.post(
            "/api/requests",
            json={
                "name": "Test Kullanıcısı",
                "email": "test@example.com",
                "service": "Görev Otomasyonu",
                "description": "Kısa"
            }
        )

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
