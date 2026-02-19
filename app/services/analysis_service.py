from pathlib import Path
from typing import Dict, Any
from app.infrastructure.loader import ExcelLoader
from app.domain.metrics import MetricsCalculator
from app.core.exceptions import ColunaNaoEncontradaError
from app.core.logger import get_logger

logger = get_logger()


class AnalysisService:

    def __init__(self, file_path: Path, coluna_vendas: str):
        self.file_path = file_path
        self.coluna_vendas = coluna_vendas

    def execute(self) -> Dict[str, Any]:
        logger.info("Iniciando análise da planilha.")

        loader = ExcelLoader(self.file_path)
        df = loader.load()

        if self.coluna_vendas not in df.columns:
            raise ColunaNaoEncontradaError(
                f"Coluna '{self.coluna_vendas}' não encontrada."
            )

        metrics = MetricsCalculator.calculate(df, self.coluna_vendas)

        logger.info("Análise finalizada com sucesso.")
        return metrics