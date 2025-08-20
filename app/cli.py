import json
import typer
from typing import Optional
from .schemas import AddRequest
from .service import add_numbers

app = typer.Typer(help="MyApp CLI")


@app.command(help="Add two numbers from CLI")
def add(
    x: float = typer.Argument(..., help="first operand"),
    y: float = typer.Argument(..., help="second operand"),
    json_out: bool = typer.Option(False, "--json", help="output JSON"),
):
    res = add_numbers(AddRequest(x=x, y=y))
    if json_out:
        typer.echo(json.dumps(res.model_dump()))
    else:
        typer.echo(f"Result: {res.result}")


@app.command(help="Run the FastAPI server (convenience wrapper)")
def serve(
    host: str = "0.0.0.0",
    port: int = 8000,
    reload: bool = typer.Option(False, help="auto-reload on code changes"),
):
    import uvicorn

    uvicorn.run("app.api:app", host=host, port=port, reload=reload)


def main():
    app()


if __name__ == "__main__":
    main()
