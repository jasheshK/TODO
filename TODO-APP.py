import streamlit as st 
import funmain as fun

st.title("My ToDo APP")
st.subheader("This is an TODO APP by ~ Jashesh")

todos = fun.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    fun.write_todos(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        
st.text_input(label = "", placeholder="Add new todo..",
              on_change=add_todo, key = "new_todo")