from sentence_transformers import SentenceTransformer

# Load model once when server starts
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    """Convert text into a 384-dimensional vector."""
    return model.encode(text, convert_to_tensor=True)