import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    calc = np.array(list).reshape(3, 3)

    mean = [
        np.mean(calc, axis = 0).tolist(),
        np.mean(calc, axis = 1).tolist(),
        np.mean(calc).item()
    ]
    variance = [
        np.var(calc, axis = 0).tolist(),
        np.var(calc, axis = 1).tolist(),
        np.var(calc).item()
    ]
    std = [
        np.std(calc, axis = 0).tolist(),
        np.std(calc, axis = 1).tolist(),
        np.std(calc).item()
    ]
    maximum = [
        np.max(calc, axis = 0).tolist(),
        np.max(calc, axis = 1).tolist(),
        np.max(calc).item()
    ]
    minimum = [
        np.min(calc, axis = 0).tolist(),
        np.min(calc, axis = 1).tolist(),
        np.min(calc).item()
    ]
    total = [
        np.sum(calc, axis = 0).tolist(),
        np.sum(calc, axis = 1).tolist(),
        np.sum(calc).item()
    ]

    return {
        "mean": mean,
        "variance": variance,
        "standard deviation": std,
        "max": maximum,
        "min": minimum,
        "sum": total
    }