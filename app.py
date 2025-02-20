import streamlit as st
import subprocess
import os

st.title("FreeFEM++ Streamlit App")

# User input for FreeFEM++ script
user_code = st.text_area("Enter your FreeFEM++ code here:", value="""
mesh Th = square(10, 10);
fespace Vh(Th, P1);
Vh u, v;

solve Laplace(u, v) = int2d(Th)( dx(u) * dx(v) + dy(u) * dy(v) )
                    - int2d(Th)(v)
                    + on(1, 2, 3, 4, u=0);

plot(u);
""")

# When the user clicks the Run button
if st.button("Run FreeFEM++"):
    # Save the FreeFEM++ code to a file
    with open("script.edp", "w") as f:
        f.write(user_code)

    # Execute FreeFEM++ using subprocess
    result = subprocess.run(["/usr/freefem/bin/FreeFem++", "script.edp"], capture_output=True, text=True)

    # Display output
    st.subheader("FreeFEM++ Output:")
    st.text(result.stdout)
    st.subheader("FreeFEM++ Errors (if any):")
    st.text(result.stderr)
