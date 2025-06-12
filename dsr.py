import streamlit as st
import pandas as pd
from datetime import datetime
import os

DATA_FILE = "dsr_data.csv"

# --- Load CSV ---
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Date", "Tasks Done", "Blockers", "Next Steps"])

# --- Save CSV ---
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# --- Initial Load ---
if "dsr_data" not in st.session_state:
    st.session_state.dsr_data = load_data()

st.title("📝 Daily Status Report (DSR)")

# --- Add New Entry ---
with st.expander("➕ Add New Report"):
    with st.form("dsr_form"):
        name = st.text_input("Name")
        date = st.date_input("Date", value=datetime.now())
        tasks_done = st.text_area("What did you work on today?")
        blockers = st.text_area("Any blockers?")
        next_steps = st.text_area("Planned for tomorrow")
        submit = st.form_submit_button("Submit")

        if submit:
            if name.strip() == "" or tasks_done.strip() == "":
                st.error("Please fill in required fields: Name and Tasks Done")
            else:
                new_row = {
                    "Name": name,
                    "Date": date.strftime("%Y-%m-%d"),
                    "Tasks Done": tasks_done,
                    "Blockers": blockers,
                    "Next Steps": next_steps
                }
                st.session_state.dsr_data = pd.concat(
                    [st.session_state.dsr_data, pd.DataFrame([new_row])], ignore_index=True)
                save_data(st.session_state.dsr_data)
                st.success("Report added successfully ✅")

# --- Editable Table ---
st.subheader("📋 Editable DSR Table")

edited_df = st.data_editor(
    st.session_state.dsr_data,
    num_rows="dynamic",
    use_container_width=True,
    key="dsr_editor"
)

if edited_df.equals(st.session_state.dsr_data) is False:
    st.session_state.dsr_data = edited_df
    save_data(edited_df)
    st.success("Changes saved to file.")

# --- Delete Row ---
st.subheader("🗑️ Delete Entry")
if len(st.session_state.dsr_data) > 0:
    delete_index = st.selectbox("Select row to delete (index)", options=st.session_state.dsr_data.index)
    if st.button("Delete Row"):
        st.session_state.dsr_data.drop(delete_index, inplace=True)
        st.session_state.dsr_data.reset_index(drop=True, inplace=True)
        save_data(st.session_state.dsr_data)
        st.success("Row deleted successfully.")
else:
    st.info("No reports available to delete.")
