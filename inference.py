import numpy as np
import time

def run_inference(session, runs):
    # Get model inputs
    input_names = [model_input.name for model_input in session.get_inputs()]
    input_shapes = [model_input.shape for model_input in session.get_inputs()]
    input_types = [model_input.type for model_input in session.get_inputs()]

    # Generate input data
    input_data = {}
    for name, shape, dtype in zip(input_names, input_shapes, input_types):
        if dtype == 'tensor(uint8)':
            data = np.random.randint(0, 256, size=shape, dtype=np.uint8)
        elif dtype == 'tensor(float32)':
            data = np.random.rand(*shape).astype(np.float32)
        else:
            raise ValueError(f"Unsupported data type: {dtype}")
        input_data[name] = data

    input_feed = [(name, input_data[name]) for name in input_names]
    input_feed_dict = dict(input_feed)

    # Measure inference time
    total_inference_time = 0
    for _ in range(runs):
        start_time = time.time()
        ort_output = session.run([output.name for output in session.get_outputs()], input_feed_dict)
        total_inference_time += time.time() - start_time

    average_inference_time = total_inference_time / runs
    return average_inference_time, ort_output