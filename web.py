import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if not todo in todos:
        todos.append(todo)
        functions.write_todos(todos)


st.title("Area21 ToDo APP")
st.subheader("Enthusiast Project")
st.write("This project is about all FUSS")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add ToDo", label_visibility="hidden", placeholder="Add New ToDo",
              on_change=add_todo, key="new_todo")
