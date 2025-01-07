import argparse
import time
import platform
from inference import run_inference

# Import the correct module based on the platform
current_platform = platform.system()

if current_platform == 'Darwin':  # macOS
    from mac.utils import load_model
    provider_choices = ['CPU', 'CoreML']
    default_provider = 'CPU'
elif current_platform == 'Windows':  # Windows
    from windows.utils import load_model
    provider_choices = ['CPU', 'DirectML', 'CUDA', 'TensorRT', 'OpenVINO']
    default_provider = 'CPU'
else:
    raise NotImplementedError(f"Unsupported platform: {current_platform}")


# Parse command line arguments
parser = argparse.ArgumentParser(description='Run ONNX model inference.')
parser.add_argument('--model_path', type=str, required=True, help='Path to the ONNX model file.')
parser.add_argument('--provider', type=str, choices=provider_choices, default=default_provider, help='Execution provider to use.')
parser.add_argument('--runs', type=int, default=1, help='Number of times to run the inference.')
args = parser.parse_args()

# Load model and measure loading time
start_time = time.time()
session = load_model(args.model_path, args.provider)
loading_time = time.time() - start_time
print(f"Model loading time: {loading_time:.4f} seconds")

# Run inference and measure inference time
inference_time, ort_output = run_inference(session, args.runs)
print(f"Inference time: {inference_time:.4f} seconds", f"Runs: {args.runs}")
