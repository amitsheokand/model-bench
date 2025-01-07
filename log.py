import platform

current_platform = platform.system()

def log_bench_data(args, id, loading_time, inference_time, provider):

    # Create benchmark data
    benchmark_data = {
        "_id": {
            "$oid": str(id)
        },
        "data": [
            {
                "Ok": [
                    {
                        "Ok": {
                            "metrics": [
                                {
                                    "initial_load_time": f"{loading_time * 1000:.0f}ms",
                                    "memory": "Unknown",
                                    "outputs": {
                                        "output": 0
                                    },
                                    "schedule_config": {
                                        "backup_type": provider,
                                        "type": provider,
                                        "backend_config": {
                                            "memory": "Unknown",
                                            "power": "Unknown",
                                            "precision": "Unknown"
                                        }
                                    },
                                    "cached_load_time": "Unknown",
                                    "flops": "Unknown",
                                    "inference_time": f"{inference_time * 1000:.0f}ms"
                                }
                            ],
                            "model": args.model_path
                        }
                    }
                ]
            },
        ]
    }

    return benchmark_data