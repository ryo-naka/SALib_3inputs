import numpy as np


def evaluate(X: np.ndarray, A: float = 7.0, B: float = 0.1) -> np.ndarray:
    """Borehole function:

    `f(x) = \sin(x_{1}) + A \sin(x_{2})^2 + Bx^{4}_{3}\sin(x_{1})`

    The Borehole function models water flow through a borehole.
    Its simplicity and quick evaluation makes it a commonly used function
    for testing a wide variety of methods in computer experiments.

    See listed references below.


    Parameters
    ----------
    X : np.ndarray
        An `N*D` array holding values for each parameter, where `N` is the 
        number of samples and `D` is the number of parameters 
        (in this case, three).
 

    Returns
    -------
    Y : np.ndarray

    References
    ----------
    .. [1] Virtual Library of Simulation Experiments: Test Functions and Datasets
           https://www.sfu.ca/~ssurjano/borehole.html
    """
    r_w, r, T_u, H_u, T_l, H_l, L, K_w = [X[:, j] for j in range(X.shape[1])]
    Y = np.zeros(X.shape[0])
    Y = 2 * np.pi * T_u * (H_u - H_l) / (np.log(r / r_w) * \
        (1 + 2 * L * T_u / (np.log(r / r_w) * r_w ** 2 * K_w) + T_u / T_l))

    return Y
