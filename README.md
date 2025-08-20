# FastAPI_x_Typer-CLI

Typer CLI + FastAPI API => Share the same business logics and Pydantic models

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
myapp add 1 2
myapp add 1 2 --json

# 2) 開 API（兩種方式擇一）
myapp serve --reload            # 透過 Typer 包一層
uvicorn app.api:app --reload    # 直接用 uvicorn 跑

# 3) 測 API
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"x":1,"y":2}'
```

## Resources

- [ChatGPT - Typer + FastAPI integration](https://chatgpt.com/s/t_68a59f7d2e888191a1bbc64bfb74d55a)

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
