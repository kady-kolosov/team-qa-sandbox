# Покрытие e2e тестами сервиса авторизации онлайн кинотеатра

## ВАЖНО! Перед запуском создайте и активируйте виртуальное окружение, а после установите зависимости

## Запуск тестов

- Запуск маркированных тестов для ревью: pytest -v --tb=line -m need_review
- Запуск тестов покупки новым пользователем через карту RU: pytest -v --tb=line -m new_user_card_ru_subscription_purchase
- Запуск тестов покупки старым пользователем через карту RU: pytest -v --tb=line -m old_user_card_ru_subscription_purchase
- Запуск тестов покупки новым пользователем через СБП RU: pytest -v --tb=line -m new_user_sbp_ru_subscription_purchase
- Запуск тестов покупки старым пользователем пользователем через СБП RU: pytest -v --tb=line -m old_user_sbp_ru_subscription_purchase
- Запуск тестов покупки новым пользователем через карту KZ: pytest -v --tb=line -m new_user_card_kz_subscription_purchase
- Запуск тестов покупки старым пользователем пользователем через карту KZ: pytest -v --tb=line -m old_user_card_kz_subscription_purchase

## Стек

- Python
- Selenium

## Старт

### Создать и активировать виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
```
или

```bash
/opt/homebrew/bin/python3.14 -m venv .venv
source .venv/bin/activate
```

### Установить зависимости

```bash
.venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Чек-лист проверок:

РФ Карта
- Приобретение триала
- Провести рекуррент после приобретения триала
- Провести возврат

РФ СБП
- Приобретение триала
- Провести рекуррент после приобретения триала
- Провести возврат

СНГ Карта
- Приобретение триала
- Провести рекуррент после приобретения триала
- Провести возврат
