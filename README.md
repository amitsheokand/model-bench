# ONNX Model Inference Benchmark

This project runs ONNX model inference using different execution providers and logs the benchmark data into JSON files.

## Requirements

- Python 3.6+
- `onnxruntime`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amitsheokand/model-bench.git
    cd model-bench
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script with the following command:
```sh
python main.py --model_path <path_to_onnx_model> [--provider <provider>] [--runs <number_of_runs>]