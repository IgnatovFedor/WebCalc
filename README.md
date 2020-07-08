Запуск веб-сервиса:

```bash
git clone https://github.com/IgnatovFedor/WebCalc
cd WebCalc
pip install -r requirements.txt
uvicorn webcalc.main:app --reload
```

Swagger доступен по `http://127.0.0.1:8000/docs`

Эндпоинты:
- `/sum` - вычисляет сумму аргументов
- `/mult` - вычисляет произведение аргументов

Аргументы: `a`, `b`

Пример запроса:
```bash
curl -X POST "http://127.0.0.1:8000/sum" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"a\":1,\"b\":2}"
```