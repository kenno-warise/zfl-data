from django.core.management.base import BaseCommand
from data.models import GoogleAccess, Popular
from .analytics_api import print_response, print_response_web
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):

        # ブログ閲覧数取得処理
        # Popular.objects.all().delete()
        # for title, path, view in print_response():
        #     Popular.objects.create(
        #                 title=title, path=path, view=view
        #     )

        # アクセス数取得処理
        google_access = [row for row in print_response_web()]
        #print('Googleデータ1')
        #print(google_access)

        print('Googleモデル')
        print(GoogleAccess.objects.all())

        for google_value, date_number in zip(google_access, reversed(range(len(google_access)))):
            get_datetime = datetime.date.today() - datetime.timedelta(days=date_number)
            get_model_data = GoogleAccess.objects.filter(date_data=get_datetime)

            # get_model_dataの内容が空だった場合、for文処理を行われない。
            # 空の場合は手前の要素が継続される。
            for row in get_model_data:
                get_access_data = row.access_data

            GoogleAccess.objects.update_or_create(
                    date_data=get_datetime,
                    access_data=get_access_data,
                    defaults={
                        'date_data': get_datetime,
                        'access_data': google_value,
                    }
            )

        self.stdout.write(self.style.SUCCESS('更新完了'))
