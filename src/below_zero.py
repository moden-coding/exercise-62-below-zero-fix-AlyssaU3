#!/usr/bin/env python3

import pandas as pd

def below_zero():
    below_zero=[]
    zero= pd.read_csv("src/kumpula-weather-2017.csv")
    days= zero["Air temperature (degC)"]
    for day in days:
        if day<0:
            below_zero.append(day)
    return len(below_zero)

def main():
    result = below_zero()
    print(f"Number of days below zero: {result}")
if __name__ == "__main__":
    main()
