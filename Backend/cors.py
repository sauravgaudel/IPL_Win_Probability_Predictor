from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],  # frontend URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
