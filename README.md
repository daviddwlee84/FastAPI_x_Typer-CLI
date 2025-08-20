# FastAPI-based API x Typer-based CLI

[Typer](https://typer.tiangolo.com/) CLI + [FastAPI](https://fastapi.tiangolo.com/) API => Share the same business logics and Pydantic models

> - Typer is based on [Click](https://click.palletsprojects.com/en/stable/)
> - Typer is not using Pydantic: [Alternatives, Inspiration and Comparisons - Typer](https://typer.tiangolo.com/alternatives/?h=pyda#pydantic)
> - [Tyro](https://brentyi.github.io/tyro/) does!

```bash
app/
    __init__.py
    service.py        # 業務邏輯（API/CLI 共用）
    schemas.py        # Pydantic 輸入/輸出模型
    api.py            # FastAPI
    cli.py            # Typer
pyproject.toml
```

```bash
uv sync --all-groups
```

```bash
# 1) CLI
cli add 1 2
cli add 1 2 --json

# 2) 開 API（兩種方式擇一）
cli serve --reload            # 透過 Typer 包一層
uvicorn app.api:app --reload    # 直接用 uvicorn 跑

# 3) 測 API
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"x":1,"y":2}'
# API Doc: http://localhost:8000/docs

# 4) Pydantic AutoCLI version
autocli add --x 1 --y 2

# 5) Tyro version (recommend!!)
# NOTE: we make MAKE_REQUIRED_ARGS_POSITIONAL then `tyrocli add --x 1 --y 2` won't work
tyrocli add 1 2
# NOTE: `--json_out` also works
tyrocli add 1 2 --json-out
tyrocli serve
```

## Todo

- [ ] Submit Task Queue Scenario
  - [daviddwlee84/Celery-Redis-TaskQueue: Showcase of Celery x Redis for Task Queue](https://github.com/daviddwlee84/Celery-Redis-TaskQueue)
- [ ] Docker Compose

## Resources

- [ChatGPT - Typer + FastAPI integration](https://chatgpt.com/s/t_68a59f7d2e888191a1bbc64bfb74d55a)

Related Stuff

- [endaaman/pydantic-autocli: Automatic CLI generator from Pydantic models with subcommand support and argument validation](https://github.com/endaaman/pydantic-autocli)
- [mansenfranzen/autodoc_pydantic: Seamlessly integrate pydantic models in your Sphinx documentation.](https://github.com/mansenfranzen/autodoc_pydantic)
  - [🌟 Features — autodoc_pydantic 2.2.0 documentation](https://autodoc-pydantic.readthedocs.io/en/stable/index.html)
- Tyro
  - [Hierarchical Structures - tyro](https://brentyi.github.io/tyro/examples/hierarchical_structures/#pydantic-integration)
  - [Subcommands - tyro](https://brentyi.github.io/tyro/examples/subcommands/)
  - [tyro.conf - tyro](https://brentyi.github.io/tyro/api/tyro/conf/#tyro.conf.PositionalRequiredArgs)
    - `tyro.conf.PositionalRequiredArgs`: Make all required arguments (those without default values) positional.
  - `use_underscores` – If True, uses underscores as word delimiters in the help text instead of hyphens. This only affects the displayed help; *both underscores and hyphens are treated equivalently during parsing*. The default (False) follows the GNU style guide for command-line options.

---

How I setup project

```bash
uv init --python 3.13
uv venv
source .venv/bin/activate
uv add "fastapi[standard]" uvicorn typer pydantic
uv add --dev black
```

---

Trouble Shooting

=> If we want to use `[project.scripts]` to create CLI

warning: Skipping installation of entry points (`project.scripts`) because this project is not packaged; to install entry points, set `tool.uv.package = true` or define a `build-system`

- [ChatGPT - Make a project a package](https://chatgpt.com/share/68a59f97-bf00-8012-a3d8-2cae1fb96614)
