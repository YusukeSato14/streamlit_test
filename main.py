import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib, cv2, csv
from PIL import Image


def main():
    st.sidebar.title("select datasets")
    run_file = st.sidebar.selectbox("Choose the datasets", get_datasets())
    if st.sidebar.button("run"):
        check_image(run_file)
    else:
        st.write("which?")

def get_datasets():
    files = os.listdir("./datasets")
    files_dir = [f for f in files if os.path.isdir(os.path.join("./datasets", f))]
    return files_dir

def check_image(run_file):
        i=1
        get_image(run_file, i)
        if st.button("younger"):
            i+=1
            st.write(i)
            get_image(run_file, i)
        elif st.button("next"):
            i+=1
            get_image(run_file, i)
        elif st.button("older"):
            i+=1
            get_image(run_file, i)

def get_image(run_file, i):
    path = "./datasets/" + run_file + "/" + run_file + ".csv"
    df = pd.read_csv(path)
    with open(path, newline="") as csvfile:
        images = csv.reader(csvfile)
        image_data = [ row for row in images]
        path_element=df.columns.get_loc("path")
        st.write(path_element)
        # image_bool = False
        st.write(image_data[i][path_element])
        image = Image.open("./" + image_data[i][path_element])
        st.image(image, caption="face data", use_column_width=True)





if __name__ == "__main__":
    main()
