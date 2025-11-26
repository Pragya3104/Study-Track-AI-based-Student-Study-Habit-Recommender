import streamlit as st
from db_functions import (
    insert_log, fetch_logs, fetch_all,
    update_log, delete_log, create_table
)

create_table()

def student_ui():
    st.header("Student Study Log")

    sid = st.text_input("Student ID")
    subject = st.text_input("Subject")
    topic = st.text_input("Topic")
    duration = st.number_input("Duration (min)", min_value=1)

    if st.button("Save Log"):
        insert_log(sid, subject, topic, int(duration))
        st.success("Log saved successfully")

    if st.button("Fetch My Logs"):
        df = fetch_logs(sid)
        st.dataframe(df)

def admin_ui():
    st.header("Admin Panel")

    user = st.text_input("Admin Username")
    pwd = st.text_input("Admin Password", type="password")

    if user == "admin" and pwd == "admin123":
        st.success("Logged in")

        option = st.selectbox("Select Action", [
            "View All Logs",
            "Add Log",
            "Update Log",
            "Delete Log"
        ])

        if option == "View All Logs":
            st.dataframe(fetch_all())

        elif option == "Add Log":
            sid = st.text_input("Student ID")
            subject = st.text_input("Subject")
            topic = st.text_input("Topic")
            duration = st.number_input("Duration", min_value=1)
            if st.button("Add"):
                insert_log(sid, subject, topic, int(duration))
                st.success("Added")

        elif option == "Update Log":
            rid = st.number_input("Record ID", min_value=1)
            new_dur = st.number_input("New Duration", min_value=1)
            if st.button("Update"):
                update_log(int(rid), int(new_dur))
                st.success("Updated")

        elif option == "Delete Log":
            rid = st.number_input("Record ID", min_value=1)
            if st.button("Delete"):
                delete_log(int(rid))
                st.success("Deleted")

def main():
    st.title("Study Track - Streamlit App")

    menu = st.sidebar.radio("Select Role", ["Student", "Admin"])

    if menu == "Student":
        student_ui()
    else:
        admin_ui()

if __name__ == "__main__":
    main()
