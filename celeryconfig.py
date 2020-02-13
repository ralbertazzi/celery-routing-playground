broker_url = "amqp://localhost:5672"
result_backend = "redis://localhost:6379/1"
task_default_priority = 0
task_queue_max_priority = 10
imports = ("tasks",)
