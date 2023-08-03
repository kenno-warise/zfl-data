from django.test import TestCase # type: ignore
from django.urls import reverse # type: ignore


class IndexTest(TestCase):
    def test_data_pageview(self):
        """
        /data/の表示テスト
        """
        response = self.client.get(reverse("data:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "現在チャートはありません")

    
