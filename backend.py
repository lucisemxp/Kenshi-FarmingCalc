NU_CONSUME = {
    "greenlander": 40*1,
    "scorchlander": 40*0.9,
    "shek": 40*1.25,
    "prince": 40*0.5,
    "drone": 40*0.5,
    "soldier": 40*0.6,
    "dog": 40*2,
    "beast": 40*2.25
}

FOOD_NU = {
    "bread": 30,
    "chewsticks": 20,
    "cookedVeg": 25,
    "driedMeat": 15,
    "dustwich": 70,
    "foodcube": 75,
    "gohan": 75,
    "meatwrap": 50,
    "ricebowl": 25
}

PROD = {
    "cactus": {
        "S": round(24 * 16 / (24 + 1.5), 2),
        "M": round(24 * 32 / (24 + 3.0), 2),
        "L": round(24 * 48 / (24 + 4.5), 2),
        "XL": round(24 * 64 / (24 + 6.0), 2),
    },

    "greenfruit": {
        "S": round(24 * 40 / (23.3 + 0.9), 2),
        "M": round(24 * 70 / (23.3 + 1.6), 2),
        "L": round(24 * 98 / (23.3 + 2.3), 2),
        "H": round(24 * 36 / (15 + 0.5), 2),
    },

    "riceweed": {
        "S": round(24 * 30 / (15 + 1.4), 2),
        "M": round(24 * 55 / (15 + 2.6), 2),
        "L": round(24 * 81 / (15 + 3.8), 2),
        "H": round(24 * 54 / (10 + 0.8), 2),
    },

    "wheatstraw": {
        "S": round(24 * 25 / (22 + 1.2), 2),
        "M": round(24 * 50 / (22 + 2.3), 2),
        "L": round(24 * 75 / (22 + 3.5), 2),
        "XL": round(24 * 100 / (22 + 4.7), 2),
        "H": round(24 * 36 / (14 + 0.5), 2),
    }
}

def safe_divide(numerator, denominator):
    if denominator == 0:
        return 0
    return round(numerator / denominator, 2)

def consume_calc(green, scorch, shek, prince, drone, soldier, dog, beast, soilCactus, soilFruit, soilRice, soilWheat):
    total = 0
    total += NU_CONSUME["greenlander"]*green
    total += NU_CONSUME["scorchlander"]*scorch
    total += NU_CONSUME["shek"]*shek
    total += NU_CONSUME["prince"]*prince
    total += NU_CONSUME["drone"]*drone
    total += NU_CONSUME["soldier"]*soldier
    total += NU_CONSUME["dog"]*dog
    total += NU_CONSUME["beast"]*beast

    FOOD_REQ = {
        "breadReq": round(total/FOOD_NU["bread"], 2),
        "stickReq": round(total/FOOD_NU["chewsticks"], 2),
        "coockedVegReq": round(total/FOOD_NU["cookedVeg"], 2),
        "driedReq": round(total/FOOD_NU["driedMeat"], 2),
        "dustReq": round(total/FOOD_NU["dustwich"], 2),
        "cubeReq": round(total/FOOD_NU["foodcube"], 2),
        "gohanReq": round(total/FOOD_NU["gohan"], 2),
        "wrapReq": round(total/FOOD_NU["meatwrap"], 2),
        "bowlReq": round(total/FOOD_NU["ricebowl"], 2)
    }

    cactus_factor = soilCactus / 100 if soilCactus > 0 else 0
    fruit_factor = soilFruit / 100 if soilFruit > 0 else 0
    rice_factor = soilRice / 100 if soilRice > 0 else 0
    wheat_factor = soilWheat / 100 if soilWheat > 0 else 0

    PROD_REQ ={
        "breadProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": safe_divide(FOOD_REQ["breadReq"]*10, PROD["wheatstraw"]["S"] * wheat_factor),
            "WS_M": safe_divide(FOOD_REQ["breadReq"]*10, PROD["wheatstraw"]["M"] * wheat_factor),
            "WS_L": safe_divide(FOOD_REQ["breadReq"]*10, PROD["wheatstraw"]["L"] * wheat_factor),
            "WS_XL": safe_divide(FOOD_REQ["breadReq"]*10, PROD["wheatstraw"]["XL"] * wheat_factor),
            "WS_H": safe_divide(FOOD_REQ["breadReq"]*10, PROD["wheatstraw"]["H"] * wheat_factor)
        },

        "chewProdReq": {
            "CA_S": safe_divide(FOOD_REQ["stickReq"]*8, PROD["cactus"]["S"] * cactus_factor),
            "CA_M": safe_divide(FOOD_REQ["stickReq"]*8, PROD["cactus"]["M"] * cactus_factor),
            "CA_L": safe_divide(FOOD_REQ["stickReq"]*8, PROD["cactus"]["L"] * cactus_factor),
            "CA_XL": safe_divide(FOOD_REQ["stickReq"]*8, PROD["cactus"]["XL"] * cactus_factor),
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": 0,
            "WS_M": 0,
            "WS_L": 0,
            "WS_XL": 0,
            "WS_H": 0
        },

        "vegProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": safe_divide(FOOD_REQ["coockedVegReq"]*8, PROD["greenfruit"]["S"] * fruit_factor),
            "GF_M": safe_divide(FOOD_REQ["coockedVegReq"]*8, PROD["greenfruit"]["M"] * fruit_factor),
            "GF_L": safe_divide(FOOD_REQ["coockedVegReq"]*8, PROD["greenfruit"]["L"] * fruit_factor),
            "GF_H": safe_divide(FOOD_REQ["coockedVegReq"]*8, PROD["greenfruit"]["H"] * fruit_factor),
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": 0,
            "WS_M": 0,
            "WS_L": 0,
            "WS_XL": 0,
            "WS_H": 0
        },

        "driedProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": 0,
            "WS_M": 0,
            "WS_L": 0,
            "WS_XL": 0,
            "WS_H": 0
        },

        "dustwProdReq": {
            "CA_S": safe_divide(FOOD_REQ["dustReq"]*8, PROD["cactus"]["S"] * cactus_factor),
            "CA_M": safe_divide(FOOD_REQ["dustReq"]*8, PROD["cactus"]["M"] * cactus_factor),
            "CA_L": safe_divide(FOOD_REQ["dustReq"]*8, PROD["cactus"]["L"] * cactus_factor),
            "CA_XL": safe_divide(FOOD_REQ["dustReq"]*8, PROD["cactus"]["XL"] * cactus_factor),
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": safe_divide(FOOD_REQ["dustReq"]*10, PROD["wheatstraw"]["S"] * wheat_factor),
            "WS_M": safe_divide(FOOD_REQ["dustReq"]*10, PROD["wheatstraw"]["M"] * wheat_factor),
            "WS_L": safe_divide(FOOD_REQ["dustReq"]*10, PROD["wheatstraw"]["L"] * wheat_factor),
            "WS_XL": safe_divide(FOOD_REQ["dustReq"]*10, PROD["wheatstraw"]["XL"] * wheat_factor),
            "WS_H": safe_divide(FOOD_REQ["dustReq"]*10, PROD["wheatstraw"]["H"] * wheat_factor)
        },

        "cubeProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": safe_divide(FOOD_REQ["cubeReq"]*8, PROD["greenfruit"]["S"] * fruit_factor),
            "GF_M": safe_divide(FOOD_REQ["cubeReq"]*8, PROD["greenfruit"]["M"] * fruit_factor),
            "GF_L": safe_divide(FOOD_REQ["cubeReq"]*8, PROD["greenfruit"]["L"] * fruit_factor),
            "GF_H": safe_divide(FOOD_REQ["cubeReq"]*8, PROD["greenfruit"]["H"] * fruit_factor),
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": safe_divide(FOOD_REQ["cubeReq"]*10, PROD["wheatstraw"]["S"] * wheat_factor),
            "WS_M": safe_divide(FOOD_REQ["cubeReq"]*10, PROD["wheatstraw"]["M"] * wheat_factor),
            "WS_L": safe_divide(FOOD_REQ["cubeReq"]*10, PROD["wheatstraw"]["L"] * wheat_factor),
            "WS_XL": safe_divide(FOOD_REQ["cubeReq"]*10, PROD["wheatstraw"]["XL"] * wheat_factor),
            "WS_H": safe_divide(FOOD_REQ["cubeReq"]*10, PROD["wheatstraw"]["H"] * wheat_factor)
        },

        "gohanProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": safe_divide(FOOD_REQ["gohanReq"]*8, PROD["greenfruit"]["S"] * fruit_factor),
            "GF_M": safe_divide(FOOD_REQ["gohanReq"]*8, PROD["greenfruit"]["M"] * fruit_factor),
            "GF_L": safe_divide(FOOD_REQ["gohanReq"]*8, PROD["greenfruit"]["L"] * fruit_factor),
            "GF_H": safe_divide(FOOD_REQ["gohanReq"]*8, PROD["greenfruit"]["H"] * fruit_factor),
            "RW_S": safe_divide(FOOD_REQ["gohanReq"]*10, PROD["riceweed"]["S"] * rice_factor),
            "RW_M": safe_divide(FOOD_REQ["gohanReq"]*10, PROD["riceweed"]["M"] * rice_factor),
            "RW_L": safe_divide(FOOD_REQ["gohanReq"]*10, PROD["riceweed"]["L"] * rice_factor),
            "RW_H": safe_divide(FOOD_REQ["gohanReq"]*10, PROD["riceweed"]["H"] * rice_factor),
            "WS_S": 0,
            "WS_M": 0,
            "WS_L": 0,
            "WS_XL": 0,
            "WS_H": 0
        },

        "meatProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": 0,
            "RW_M": 0,
            "RW_L": 0,
            "RW_H": 0,
            "WS_S": safe_divide(FOOD_REQ["wrapReq"]*10, PROD["wheatstraw"]["S"] * wheat_factor),
            "WS_M": safe_divide(FOOD_REQ["wrapReq"]*10, PROD["wheatstraw"]["M"] * wheat_factor),
            "WS_L": safe_divide(FOOD_REQ["wrapReq"]*10, PROD["wheatstraw"]["L"] * wheat_factor),
            "WS_XL": safe_divide(FOOD_REQ["wrapReq"]*10, PROD["wheatstraw"]["XL"] * wheat_factor),
            "WS_H": safe_divide(FOOD_REQ["wrapReq"]*10, PROD["wheatstraw"]["H"] * wheat_factor)
        },

        "bowlProdReq": {
            "CA_S": 0,
            "CA_M": 0,
            "CA_L": 0,
            "CA_XL": 0,
            "GF_S": 0,
            "GF_M": 0,
            "GF_L": 0,
            "GF_H": 0,
            "RW_S": safe_divide(FOOD_REQ["bowlReq"]*10, PROD["riceweed"]["S"] * rice_factor),
            "RW_M": safe_divide(FOOD_REQ["bowlReq"]*10, PROD["riceweed"]["M"] * rice_factor),
            "RW_L": safe_divide(FOOD_REQ["bowlReq"]*10, PROD["riceweed"]["L"] * rice_factor),
            "RW_H": safe_divide(FOOD_REQ["bowlReq"]*10, PROD["riceweed"]["H"] * rice_factor),
            "WS_S": 0,
            "WS_M": 0,
            "WS_L": 0,
            "WS_XL": 0,
            "WS_H": 0
        }
    }

    return FOOD_REQ, PROD_REQ