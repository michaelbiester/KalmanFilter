def g_h_filter (data, x0, dx0, g, h, dt):
    """
    data : a M point data set as list or numpy array
    x0   : initial position / data point
    dx0  : initial velocity / change rate
    g    : weighting factor for position / data  updates
    h    : weighting factor for velocity / change rate updates
    dt   : fixed step size (time step)
    """
    # intialise position and change rate
    x = x0
    dx = dx0
    x_estimates = []
    for z in data:
        # prediction 
        x_predict = x + dx * dt
        dx_predict = dx
        # update 
        residual = z - x_predict
        x = x_predict + g * residual
        dx = dx_predict + h * (residual/dt)
        x_estimates.append(x)

    return x_estimates