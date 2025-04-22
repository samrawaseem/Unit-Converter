import streamlit as st

st.title("🌏Unit Converter")
st.markdown("### Converts Length, Weight, and Time instantly")
st.write("Welcome ! Select, Category")

category = st.selectbox("Choose a category" , ["Length","Weight","Time"])

def convert_units (category, value, unit):
    if category == "Length" :
        if unit == "Kilometers to Miles" :
            return value * 0.621371
        elif unit == "Miles to Kilometers" :
            return value / 0.621371
        
        elif category == "Weight":
            if unit == "Kilograms to Pounds" :
                return value * 2.20462
            elif unit == "Pounds to Kilograms" :
                return value / 2.20462
            elif category == "Time":
                if unit == "Seconds to Minutes" :
                    return value / 60
                elif unit == "Minutes to Seconds" :
                    return value * 60
                elif unit == "Hours to Minutes" :
                    return value * 60
                elif unit == "Minutes to Hours" :
                    return value / 60
                elif unit == "Hours to days" :
                    return value / 24
                elif unit == "Days to Hours" :
                    return value * 24
                return 0
            
if category == "Length":
                unit= st.selectbox("Select a unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
     unit= st.selectbox("Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Time":
     unit= st.selectbox("Select a unit", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Hours to days", "Days to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")

