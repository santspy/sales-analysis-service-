import pandas as pd
from app.domain.metrics import MetricsCalculator


def test_calculo_metricas():
    df = pd.DataFrame({"Vendas": [100, 200, 300]})
    resultado = MetricsCalculator.calculate(df, "Vendas")

    assert resultado["total"] == 600.0
    assert resultado["media"] == 200.0
    assert resultado["quantidade_registros"] == 3