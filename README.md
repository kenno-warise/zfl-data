# zfl-data

[![PyPI - Version](https://img.shields.io/pypi/v/zfl-data.svg)](https://pypi.org/project/zfl-data)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zfl-data.svg)](https://pypi.org/project/zfl-data)

![zfl-data_1](https://github.com/kenno-warise/zfl-data/assets/51676019/bab9bc05-aeaf-41ff-aa6d-f023894f6c57)

-----

**目次**

- [詳細](#詳細)
- [インストール](#インストール)
- [設定](#設定)
- [License](#license)

## 詳細


## インストール

```console
$ pip install zfl-data
```

## 設定

`myproject/settings.py`

```python
INSTALLED_APPS = [
    ...,
    "data",
]
```

プロジェクト直下のテンプレートを読み込むように設定

```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

アナリティクスレポートを取得する際に必要な「secret_key.json」を読み込む設定

```python
try:
    ZEROFROMLIGHT_DIR = '/var/www/secret'
    ZEROFROMLIGHT_PATH = os.path.join(ZEROFROMLIGHT_DIR, 'secret_key.json')

    with open(ZEROFROMLIGHT_PATH, 'r') as secret_file:
        ZEROFROMLIGHT_KEYS = json.load(secret_file)

except FileNotFoundError:
    ZEROFROMLIGHT_DIR = '/home/kenno/pylist/website/secret'
    ZEROFROMLIGHT_PATH = os.path.join(ZEROFROMLIGHT_DIR, 'secret_key.json')

    with open(ZEROFROMLIGHT_PATH, 'r') as secret_file:
        ZEROFROMLIGHT_KEYS = json.load(secret_file)
```

`myproject/urls.py`

```
...python
from django.urls import path, include

urlpatterns = [
    ...,
    path('', include('ai.urls')),
]
```

zfl-dataのテンプレートである「index.html」ではテンプレートタグ「{% extends '...' %}」で「base.html」を読み込むように設定しているので、「templates/base.html」を作成する必要があります。

```console
$ mkdir templates && touch templates/base.html
```

base.htmlの内容

```html
{% load static %}
<html lang="ja" prefix="og: http://ogp.me/ns#">
  <head>

    <!-- BootStrap CSS Link -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <!-- StaticFiles CSS -->
    {% block ai-style %}{% endblock %}

  </head>
  <body>

    <!-- Djangoテンプレートタグ -->

    {% block content %}
    {% endblock %}

    <!-- BootStrap jQuery -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

  </body>
</html>
```

サーバーを起動

```cosole
$ python3 manage.py runserver
```

## License

`zfl-data` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
