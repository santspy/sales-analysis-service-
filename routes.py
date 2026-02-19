from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.analysis_service import AnalysisService
from app.core.exceptions import ColunaNaoEncontradaError
import tempfile
from pathlib import Path

router = APIRouter()


@router.post("/analisar")
async def analisar_planilha(
    file: UploadFile = File(...),
    coluna: str = "Vendas"
):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp.write(await file.read())
            tmp_path = Path(tmp.name)

        service = AnalysisService(tmp_path, coluna)
        resultado = service.execute()

        return resultado

    except ColunaNaoEncontradaError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno no processamento.")