AQI_limits = {
    'CO(GT)': {
        30.5: (301.0, 500.0),
        15.5: (201.0, 300.0),
        12.5: (151.0, 200.0),
        9.5: (101.0, 150.0),
        4.5: (51.0, 100.0),
        0.0: (0.0, 50.0)
    },
    'NOx(GT)': {
        1600.0: (0.0, 0.0), # No entry with concentration greater than 1600
        400.0: (401.0, 500.0),
        280.0: (301.0, 400.0),
        180.0: (201.0, 300.0),
        80.0: (101.0, 200.0),
        40.0: (51.0, 100.0),
        0.0: (0.0, 50.0)
    },
    'NO2(GT)': {
        1250.0: (301.0, 500.0),
        650.0: (201.0, 300.0),
        361.0: (151.0, 200.0),
        101.0: (101.0, 150.0),
        54.0: (51.0, 100.0),
        0.0: (0.0, 50.0)
    },
    "NMHC(GT)": {
        1201.0: (451.0, 500.0),
        1001.0: (301.0, 450.0),
        701.0: (201.0, 300.0),
        501.0: (151.0, 200.0),
        301.0: (101.0, 150.0),
        101.0: (51.0, 100.0),
        0.0: (0.0, 50.0)
    },
    "C6H6(GT)": {
        70.0: (0.0, 0.0), # No entry with concentration greater than 70
        50.1: (451.0, 500.0),
        25.1: (301.0, 450.0),
        15.1: (201.0, 300.0),
        10.1: (151.0, 200.0),
        5.1: (101.0, 150.0),
        1.6: (51.0, 100.0),
        0.0: (0.0, 50.0)
    }
}