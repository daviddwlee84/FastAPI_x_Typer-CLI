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
