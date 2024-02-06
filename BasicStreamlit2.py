
#Stream Basic Functions
import streamlit as st
from PIL import Image

#Display Images:
img = Image.open("newLenna.jpeg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

#checkbox
#A checkbox returns a boolean value. 
#When the box is checked, it returns a True value 
#else returns a False value.


# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
 
    # display the text if the checkbox returns True value
    st.text("Showing the widget")
    st.image(img,width=50)

    
# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Computer', 'English','Business'))
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
st.success(status)