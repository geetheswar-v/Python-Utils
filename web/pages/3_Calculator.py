import streamlit as st
import sys
import pandas as pd

sys.path.append('/home/geetheswar/Documents/projects/ChatMate')
from calculator.evaluator.evaluator import Evaluator
from calculator.converter import *

st.title('Calculator')

calc = Evaluator()
equation = st.text_input('Enter an equation:', key='equation')

if equation:
    try:
        result = calc.evaluate(equation)
        st.write('Result:', result)
    except Exception as e:
        st.write('Error:', str(e))

st.title('Converter')
header = st.header('Length Converter')
units = st.selectbox('select the units: ', UNITS)
header.header(f'{str(units).capitalize()} Converter')
c1, c2 = st.columns(2)
with c1:
    value = st.text_input(f"Enter The {units} to Convert", key='value')
with c2:
    fro = st.selectbox('from', list(get_units(units)), key='from')
if units == 'currency':
    to = st.selectbox('to', list(get_units(units)), key='to')
    convert_btn = st.button('Convert')


def table(values, units):
    conversion = {
        'units': list(units),
        'Values': values
    }
    df = pd.DataFrame(conversion)
    df = df.reset_index(drop=True)
    st.write(df)


if value:
    if units != 'currency':
        values = []
        for key, item in get_units(units).items():
            ans = converter(int(value), fro, key, units)
            values.append(f'{ans} {item}')
        table(values, list(get_units(units).keys()))
    else:
        if convert_btn:
            st.text(f'{value}{CURRENCY.get(fro)} is converted into {converter(1, fro, to, "currency")}{CURRENCY.get(to)}')
