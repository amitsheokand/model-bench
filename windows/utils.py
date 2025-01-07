import onnxruntime as ort

def load_model(model_path, provider):
    if provider == 'DirectML':
        providers = ['DmlExecutionProvider']
    elif provider == 'CUDA':
        providers = ['CUDAExecutionProvider']
    elif provider == 'TensorRT':
        providers = ['TensorrtExecutionProvider']
    elif provider == 'OpenVINO':
        providers = ['OpenVINOExecutionProvider']
    else:
        providers = ['CPUExecutionProvider']

    session = ort.InferenceSession(model_path, providers=providers)
    return session