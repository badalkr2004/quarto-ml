"""
Lecture 1 tutorial — Function approximation intuition

Run:
    python tutorial_function_approximation.py

Requires: numpy, matplotlib
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def true_f(x: np.ndarray) -> np.ndarray:
    """Unknown 'reality' we pretend not to know when learning."""
    return np.sin(2 * np.pi * x)


def make_dataset(n: int = 15, noise: float = 0.15, seed: int = 0):
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(0, 1, size=n))
    y = true_f(x) + rng.normal(0, noise, size=n)
    return x, y


def poly_fit_predict(x_train, y_train, x_query, degree: int):
    """Initial guess = polynomials of given degree; refine = least squares."""
    coeffs = np.polyfit(x_train, y_train, degree)
    return np.polyval(coeffs, x_query)


def demo_guess_and_refine():
    x_train, y_train = make_dataset()
    x_grid = np.linspace(0, 1, 400)

    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=True)
    degrees = [1, 3, 12]  # underfit → reasonable → overfit (memorize noise)

    for ax, deg in zip(axes, degrees):
        y_hat = poly_fit_predict(x_train, y_train, x_grid, deg)
        ax.plot(x_grid, true_f(x_grid), "k--", lw=1.5, label="true f (unknown)")
        ax.plot(x_grid, y_hat, lw=2, label=f"degree-{deg} model")
        ax.scatter(x_train, y_train, c="C3", zorder=3, label="data D")
        ax.set_title(f"Guess family: poly deg {deg}")
        ax.set_xlabel("x")
        ax.legend(fontsize=8)

    axes[0].set_ylabel("y")
    fig.suptitle("Start with a guess (model family), refine with data D")
    fig.tight_layout()
    fig.savefig("01_guess_and_refine.png", dpi=140)
    print("Saved 01_guess_and_refine.png")


def demo_random_labels():
    """
    Lecture thought experiment: with flexible models you can fit *random* labels.
    Semantics are not automatic — capacity can memorize nonsense.
    """
    rng = np.random.default_rng(1)
    x = np.linspace(0, 1, 20)
    y_true = (true_f(x) > 0).astype(float)
    y_random = rng.integers(0, 2, size=len(x)).astype(float)

    x_grid = np.linspace(0, 1, 400)
    # High-capacity polynomial as a crude stand-in for a flexible learner
    y_hat_true = poly_fit_predict(x, y_true, x_grid, degree=18)
    y_hat_rand = poly_fit_predict(x, y_random, x_grid, degree=18)

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
    axes[0].scatter(x, y_true, c="C0", label="structured labels")
    axes[0].plot(x_grid, y_hat_true, c="C0")
    axes[0].set_title("Fit meaningful labels")
    axes[0].set_xlabel("x")

    axes[1].scatter(x, y_random, c="C1", label="random labels")
    axes[1].plot(x_grid, y_hat_rand, c="C1")
    axes[1].set_title("Fit random labels (still possible!)")
    axes[1].set_xlabel("x")

    for ax in axes:
        ax.set_ylim(-0.2, 1.2)
        ax.legend(fontsize=8)

    fig.suptitle("Flexible models can fit noise — need probabilistic / generalization thinking")
    fig.tight_layout()
    fig.savefig("01_random_labels.png", dpi=140)
    print("Saved 01_random_labels.png")


def image_as_vector_demo():
    """Show P×Q image → R^{PQ} vector (Lecture X-ray stacking idea)."""
    P, Q = 4, 5
    img = np.arange(P * Q).reshape(P, Q)
    vec = img.reshape(-1, order="F")  # column-stack, as in lecture
    print("\nImage (P x Q):")
    print(img)
    print(f"\nAs vector in R^{P*Q} (column-stacked):")
    print(vec)
    print(f"shape: {vec.shape}")


if __name__ == "__main__":
    demo_guess_and_refine()
    demo_random_labels()
    image_as_vector_demo()
    # Uncomment to open interactive windows:
    # plt.show()
    plt.close("all")
