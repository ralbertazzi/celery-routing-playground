# celery-routing-playground

Start Celery worker:
```bash
celery worker -A celeryapp --concurrency 1 --prefetch-multiplier 1 -Q io --loglevel debug
```

Start tasks and verify that priority is working:
```bash
python main.py
```
