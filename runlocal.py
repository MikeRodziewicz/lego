"""
Start of the home app running on the RpiZero

"""
import uvicorn


def run_local():
    uvicorn.run(
        "main.app:app",
        reload=True,
        host="0.0.0.0",
        port=8000
    )


if __name__ == "__main__":
    run_local()
