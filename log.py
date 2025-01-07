# import psutil
# import platform
# import json
#
# current_platform = platform.system()
#
# def log_bench_data(args, id, loading_time, inference_time, provider):
#     # Collect system information
#     cpu_info = {
#         "total_cores": psutil.cpu_count(logical=True),
#         "max_frequency": "Unknown",
#         "current_frequency": "Unknown",
#         "total_cpu_usage": f"{psutil.cpu_percent()}%",
#         "platform": current_platform,
#         "username": platform.node(),
#         "processor": platform.processor(),
#         "physical_cores": psutil.cpu_count(logical=False)
#     }
#
#     memory_info = psutil.virtual_memory()
#     memory_data = {
#         "total_ram": f"{memory_info.total / (1024 ** 3):.2f}GB",
#         "free_ram": f"{memory_info.available / (1024 ** 3):.2f} GB",
#         "used_ram": f"{memory_info.used / (1024 ** 3):.2f} GB",
#         "percentage": f"{memory_info.percent}"
#     }
#
#     # Create benchmark data
#     benchmark_data = {
#         "_id": {
#             "$oid": str(id)
#         },
#         "data": [
#             {
#                 "Ok": [
#                     {
#                         "Ok": {
#                             "metrics": [
#                                 {
#                                     "initial_load_time": f"{loading_time * 1000:.0f}ms",
#                                     "memory": "Unknown",
#                                     "outputs": {
#                                         "output": 0
#                                     },
#                                     "schedule_config": {
#                                         "backup_type": provider,
#                                         "type": provider,
#                                         "backend_config": {
#                                             "memory": "Unknown",
#                                             "power": "Unknown",
#                                             "precision": "Unknown"
#                                         }
#                                     },
#                                     "cached_load_time": "Unknown",
#                                     "flops": "Unknown",
#                                     "inference_time": f"{inference_time * 1000:.0f}ms"
#                                 }
#                             ],
#                             "model": args.model_path
#                         }
#                     }
#                 ]
#             },
#             {
#                 "cpu": [cpu_info]
#             },
#             {
#                 "gpu": []
#             },
#             {
#                 "memory": [memory_data]
#             }
#         ]
#     }
#
#     output_filename = f"{id}.json"
#     with open(output_filename, 'w') as f:
#         json.dump(benchmark_data, f, indent=4)
#
#     print(f"Benchmark data written to {output_filename}")


import psutil
import platform
import json

current_platform = platform.system()

def log_bench_data(args, id, loading_time, inference_time, provider):
    # Collect system information
    cpu_info = {
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": "Unknown",
        "current_frequency": "Unknown",
        "total_cpu_usage": f"{psutil.cpu_percent()}%",
        "platform": current_platform,
        "username": platform.node(),
        "processor": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False)
    }

    memory_info = psutil.virtual_memory()
    memory_data = {
        "total_ram": f"{memory_info.total / (1024 ** 3):.2f}GB",
        "free_ram": f"{memory_info.available / (1024 ** 3):.2f} GB",
        "used_ram": f"{memory_info.used / (1024 ** 3):.2f} GB",
        "percentage": f"{memory_info.percent}"
    }

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
            {
                "cpu": [cpu_info]
            },
            {
                "gpu": []
            },
            {
                "memory": [memory_data]
            }
        ]
    }

    return benchmark_data