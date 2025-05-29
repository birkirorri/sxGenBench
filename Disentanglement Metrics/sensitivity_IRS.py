import numpy as np

def compute_latent_sensitivity(mus, ys):
    """
    Compute how much each latent dimension responds to changes in each generative factor.

    Parameters:
        mus: np.ndarray of shape (num_latents, num_samples)
            The latent representation (e.g., from model outputs).
        ys: np.ndarray of shape (num_factors, num_samples)
            The ground truth generative factors (e.g., labels, batches, etc.)

    Returns:
        sensitivity: np.ndarray of shape (num_latents, num_factors)
            Sensitivity score for each latent w.r.t. each factor.
    """
    num_latents = mus.shape[0]
    num_factors = ys.shape[0]
    sensitivity = np.zeros((num_latents, num_factors))

    for i in range(num_factors):
        factor_vals = np.unique(ys[i])
        group_means = []

        for val in factor_vals:
            idx = ys[i] == val
            mean_latents = np.mean(mus[:, idx], axis=1)
            group_means.append(mean_latents)

        group_means = np.stack(group_means, axis=1)
        sensitivity[:, i] = np.std(group_means, axis=1)

    return sensitivity
