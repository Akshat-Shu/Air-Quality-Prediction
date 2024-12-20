import numpy as np

def get_AQI(concentrations, AQI_limits):
    max_individual_AQI = -1
    back_limit = -1
    for pollutant, limits in AQI_limits.items():
        if(pollutant not in concentrations or np.isnan(concentrations[pollutant])): continue
        for limit, (low, high) in limits.items():
            if(concentrations[pollutant] >= limit):
                max_individual_AQI = max(max_individual_AQI, (
                    low + (high - low) * (concentrations[pollutant] - limit) / (back_limit - limit)
                ))
                break
            back_limit = limit
    return max_individual_AQI