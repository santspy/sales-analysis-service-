import pandas as pd
from typing import Dict, Any


class MetricsCalculator:

    @staticmethod
    def calculate(df: pd.DataFrame, coluna: str) -> Dict[str, Any]:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
        df = df.dropna(subset=[coluna])

        vendas = df[coluna]

        return {
            "total": float(vendas.sum()),
            "media": float(vendas.mean()),
            "mediana": float(vendas.median()),
            "desvio_padrao": float(vendas.std()),
            "minimo": float(vendas.min()),
            "maximo": float(vendas.max()),
            "quantidade_registros": int(len(vendas))
        }