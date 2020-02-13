def route_task(name, args, kwargs, options, task=None, **kw):
    from tasks import io_bounded, io_bounded_hp, cpu_bounded

    task_queue = {
        io_bounded.name: "io",
        io_bounded_hp.name: "io",
        cpu_bounded.name: "cpu",
    }

    task_priority = {io_bounded_hp.name: 10}

    return dict(queue=task_queue[name], priority=task_priority.get(name))
