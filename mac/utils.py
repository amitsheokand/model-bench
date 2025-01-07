import onnxruntime as ort


def load_model(model_path, provider):
    if provider == 'CoreML':
        providers = [
            ('CoreMLExecutionProvider', {
                "ModelFormat": "MLProgram", "MLComputeUnits": "ALL",
                "RequireStaticInputShapes": "0", "EnableOnSubgraphs": "0"
            }),
        ]
    else:
        providers = ['CPUExecutionProvider']

    session = ort.InferenceSession(model_path, providers=providers)
    return session
