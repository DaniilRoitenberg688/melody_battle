# Melody Battle - Веб-сервис для организации музыкальных викторин

## Описание проекта
Melody Battle - это веб-сервис, позволяющий организовывать и участвовать в музыкальных викторинах (мелоди-батлах) на основе плейлистов Яндекс.Музыки. Сервис предназначен для любителей музыкальных игр и викторин.

## Основные функции
- Регистрация организаторов мелоди-батлов
- Создание батлов на основе плейлистов Яндекс.Музыки
- Присоединение участников через QR-код или ссылку
- Система подсчета очков и определения победителей
- Адаптивный интерфейс для мобильных и десктопных устройств

## Технологический стек
- Frontend: Vue.js
- Backend: Flask
- База данных: SQLite
- Дополнительные технологии: QR-код генератор, API Яндекс.Музыки

## Установка и запуск

### Требования
- Python 3.8+
- Node.js
- Vue CLI

### Установка
1. Клонировать репозиторий:
```bash
git clone [URL репозитория]
```

2. Установка зависимостей Backend:
```bash
cd backend
pip install -r requirements.txt
```

3. Установка зависимостей Frontend:
```bash
cd frontend
npm install
```

### Запуск
1. Запуск Backend:
```bash
cd backend
python app.py
```

2. Запуск Frontend:
```bash
cd frontend
npm run serve
```

## Структура проекта
```
melody-battle/
├── backend/
│   ├── app.py
│   ├── models/
│   └── services/
├── frontend/
│   ├── src/
│   ├── components/
│   └── views/
└── docs/
```

## API Endpoints
- POST `/api/register` - Регистрация организатора
- POST `/api/login` - Авторизация
- POST `/api/battles` - Создание нового батла
- GET `/api/battles/{id}` - Получение информации о батле
- POST `/api/battles/{id}/join` - Присоединение к батлу
- POST `/api/battles/{id}/score` - Отправка результатов

## База данных
### Структура таблиц
- User (id, login, password)
- Melodi_battle (mb_id, user_id)
- Score (id, mb_id, score)

## Разработка
### План разработки
1. Недели 1-2: Дизайн интерфейса
2. Недели 3-4: Разработка backend
3. Недели 5-6: Разработка frontend
4. Недели 7-8: Тестирование и деплой

## Будущие улучшения
- Система очков и вознаграждений
- Интеграция с другими музыкальными сервисами
- Система ставок
- Расширенная статистика игроков

## Авторы
[Имена авторов проекта]

## Лицензия
[Тип лицензии]

## Поддержка
По всем вопросам обращаться: [контактная информация]
