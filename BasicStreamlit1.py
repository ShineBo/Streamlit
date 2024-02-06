
#Stream Basic Functions
import streamlit as st

#Title
st.title("Hello Streamlit")

#Header
st.header("This is a header")

#subheader
st.subheader("This is subheader")

#Text
st.text("Hellow Welcome to Streamlit!!")

#Success, Info, Warning , Error, Exception

# success
st.success("Success Message" )
 
# success
st.info("Information")
 
# success
st.warning("Warning Message")
 
# success
st.error("Error Message" )
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write text
st.write("Text with write")

#Using write function, we can also display code in coding format.
# This is not possible using st.text(”).
 
# Writing python inbuilt function range()
st.write(range(10))
