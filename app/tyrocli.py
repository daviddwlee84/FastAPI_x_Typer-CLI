from pydantic import Field, BaseModel
import tyro
from typing import Annotated

from .schemas import AddRequest
from .service import add_numbers

MAKE_REQUIRED_ARGS_POSITIONAL = True


class Add(AddRequest):
    """Add two numbers together."""

    # NOTE: why we don't use `json` is because this will have warning
    # UserWarning: Field name "json" in "Add" shadows an attribute in parent "AddRequest"
    json_out: bool = Field(False, description="output JSON")


class Serve(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = Field(False, description="auto-reload on code changes")


# NOTE: if you only have one command and you want to use the subcommand feature, you need to add a dummy command for Tyro
COMMANDS = Add | Serve


def main():
    args = tyro.cli(
        COMMANDS,
        config=(
            (tyro.conf.PositionalRequiredArgs,)
            if MAKE_REQUIRED_ARGS_POSITIONAL
            else None
        ),
    )
    if isinstance(args, Add):
        result = add_numbers(args)
        if args.json_out:
            print(result.model_dump_json())
        else:
            print(f"Result: {result.result}")
    elif isinstance(args, Serve):
        import uvicorn

        uvicorn.run("app.api:app", host=args.host, port=args.port, reload=args.reload)
    else:
        raise ValueError(f"Unknown command: {args}")


if __name__ == "__main__":
    main()
