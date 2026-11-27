from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="Secure Delivery Platform Lab")
requests = Counter("lab_http_requests_total", "Handled API requests", ["route"])

@app.get("/health")
def health():
    requests.labels(route="health").inc()
    return {"status": "ok"}

@app.get("/items")
def items():
    requests.labels(route="items").inc()
    return {"items": [{"id": 1, "name": "demo"}]}

@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
