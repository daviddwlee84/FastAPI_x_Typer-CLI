from .schemas import AddRequest, AddResult


def add_numbers(req: AddRequest) -> AddResult:
    # 真正的業務邏輯只放這裡（可連 DB、呼叫外部服務等）
    return AddResult(result=req.x + req.y)
