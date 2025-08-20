import typer
from pydantic_autocli import AutoCLI
from .schemas import AddRequest
from .service import add_numbers


class AddAutoCLI(AutoCLI):
    """Auto-generated CLI from Pydantic models"""

    def run_add(self, req: AddRequest):
        """Add two numbers from CLI (automatically generated from AddRequest schema)"""
        result = add_numbers(req)
        if hasattr(result, "result"):
            typer.echo(f"Result: {result.result}")
        else:
            typer.echo(str(result))


# Integrate pydantic-autocli with our main typer app
add_cli = AddAutoCLI()


# For direct execution with pydantic-autocli
def main():
    add_cli.run()


if __name__ == "__main__":
    main()
