from deepface import DeepFace

from helper.utils import getEnv

# Environment retrieve
DB_PATH = getEnv("DEEPFACE_DB_PATH", "sample/")
MODEL = getEnv("DEEPFACE_MODEL", "Facenet")
BACKEND = getEnv("DEEPFACE_BACKEND", "fastmtcnn")
DISTANCE_METRIC = getEnv("DEEPFACE_DISTANCE_METRIC", "euclidean_l2")
ANTI_SPOOFING = getEnv("DEEPFACE_ANTI_SPOOFING", "True").lower() == "true"
ENCOFRCE_DETECTION = getEnv("DEEPFACE_ENFORCE_DETECTION", "False").lower() == "true"
SILENT = getEnv("DEEPFACE_SILENT", "True").lower() == "true"

def find(img_path, path = ""):
    return DeepFace.find(
        silent=SILENT,
        img_path=img_path,
        db_path=f"sample/{path}",
        model_name=MODEL,
        detector_backend=BACKEND,
        enforce_detection=ENCOFRCE_DETECTION,
        distance_metric=DISTANCE_METRIC,
        anti_spoofing=ANTI_SPOOFING,
    )