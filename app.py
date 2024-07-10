import streamlit as st

tools = [
    {
        "name": "Tool 1",
        "description": "This is the description for Tool 1.",
        "usage": "Usage instructions for Tool 1."
    },
    {
        "name": "Tool 2",
        "description": "This is the description for Tool 2.",
        "usage": "Usage instructions for Tool 2."
    },
    {
        "name": "Tool 3",
        "description": "This is the description for Tool 3.",
        "usage": "Usage instructions for Tool 3."
    }
]

st.title("工具集展示")

for tool in tools:
    st.header(tool["name"])
    st.write(tool["description"])
    with st.expander("使用說明"):
        st.write(tool["usage"])
    st.markdown("---")

if st.button('添加新工具'):
    st.text_input('工具名稱', key='new_tool_name')
    st.text_area('工具描述', key='new_tool_description')
    st.text_area('使用說明', key='new_tool_usage')
    if st.button('提交'):
        new_tool = {
            "name": st.session_state['new_tool_name'],
            "description": st.session_state['new_tool_description'],
            "usage": st.session_state['new_tool_usage']
        }
        tools.append(new_tool)
        st.experimental_rerun()





