import numpy as np

def alpha_beta_filter(z_measurements, x_init, v_init, dt, alpha, beta):
    """
    z_measurements: array of measurements
    x_init: initial position
    v_init: initial velocity
    dt: time step
    alpha: scaling factor position estimate
    beta: scaling factor velocity estimate

    returns:

    numpy arrays of

    x_estimates: position estimates
    v_estimates: velocity estimates
    x_predictions: position predictions
    v_predictions: velocity predictions
    """
    x_estimates = []
    v_estimates = []
    x_predictions = []
    v_predictions = []
    
    for k, z_measured in enumerate(z_measurements): 
        if k==0:
            # init
            x_predicted= x_init
            v_predicted= v_init
            x_estimated = x_predicted
            v_estimated = v_predicted
        else:
            # prediction update
            x_predicted = x_estimated + dt * v_estimated
            v_predicted = v_estimated
            residual = z_measured - x_predicted
            # new estimates
            x_estimated = x_predicted + alpha*residual
            v_estimated = v_predicted + beta * residual /dt
        
        x_estimates.append(x_estimated)
        v_estimates.append(v_estimated)
        x_predictions.append(x_predicted)
        v_predictions.append(v_predicted)
    
    return np.array(x_estimates), np.array(v_estimates), np.array(x_predictions), np.array(v_predictions)