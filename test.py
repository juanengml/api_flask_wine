import numpy
import joblib
import pandas as pd 
import numpy as np
from console_logging.console import Console
console = Console()

def main():
  console.log("LOADING MODEL...")
  model = joblib.load("model.pkl")

  data = [[1.1, 1.0, 2.0, 1.6]]
  console.info("PREDICT DATA...")

  res = model.predict(data)
  console.success(res)

if __name__ == "__main__":
    main()
