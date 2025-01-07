import argparse
import json
import os
import time
import platform
import uuid

from inference import run_inference
from log import log_bench_data

# Import the correct module based on the platform
current_platform = platform.system()

if current_platform == 'Darwin':  # macOS
    from mac.utils import load_model
    provider_choices = ['CPU', 'CoreML', 'all']
    default_provider = 'all'
elif current_platform == 'Windows':  # Windows
    from windows.utils import load_model
    provider_choices = ['CPU', 'DirectML', 'CUDA', 'TensorRT', 'OpenVINO', 'all']
    default_provider = 'all'
else:
    raise NotImplementedError(f"Unsupported platform: {current_platform}")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run ONNX model inference.')
parser.add_argument('--model_path', type=str, required=True, help='Path to the ONNX model file.')
parser.add_argument('--provider', type=str, choices=provider_choices, default=default_provider, help='Execution provider to use.')
parser.add_argument('--runs', type=int, default=1, help='Number of times to run the inference.')
args = parser.parse_args()

# if file does not exist, quit
if not os.path.exists(args.model_path):
    print("Model file not found, exiting...")
    exit()

id = uuid.uuid4()
benchmark_results = []

# Function to run inference and log data
def run_and_log(provider):

    # Load model and measure loading time
    start_time = time.time()
    session = load_model(args.model_path, provider)
    loading_time = time.time() - start_time
    # print(f"Model loading time ({provider}): {loading_time:.4f} seconds")

    # Run inference and measure inference time
    inference_time, ort_output = run_inference(session, args.runs)
    # print(f"Inference time ({provider}): {inference_time:.4f} seconds", f"Runs: {args.runs}")

    # Log benchmark data
    benchmark_results.append(log_bench_data(args, id, loading_time, inference_time, provider))

# Run inference for the specified provider(s)
if args.provider == 'all':
    for provider in provider_choices[:-1]:  # Exclude 'all' from the list
        run_and_log(provider)
else:
    run_and_log(args.provider)

# # Save all benchmark data to a single JSON file
# output_filename = f"{id}.json"
# with open(output_filename, 'w') as f:
#     json.dump(benchmark_results, f, indent=4)

print(f"{benchmark_results}")