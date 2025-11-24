import streamlit as st

if "reset" not in st.session_state:
    st.session_state.reset = False

def reset_fields():
    st.session_state.apikey = ""
    st.session_state.bundle = ""
    st.session_state.appid = ""
    st.session_state.project = ""

st.title("Codemagic.yaml Generator")

if st.button("Очистить поля"):
    reset_fields()

apikey = st.text_input("APIKEY NAME", key="apikey")
bundle = st.text_input("Bundle ID", key="bundle")
appid = st.text_input("App ID", key="appid")
project = st.text_input("Xcode Project / Scheme (без .xcodeproj)", key="project")

TEMPLATE = open("codemagic-template.yaml").read()
EMAIL = st.secrets.get("EMAIL", "{EMAIL}")

if apikey and bundle and appid and project:
    yaml = TEMPLATE \
        .replace("{APIKEY_NAME}", apikey) \
        .replace("{BUNDLE_ID}", bundle) \
        .replace("{APP_ID}", appid) \
        .replace("{PROJECT_NAME}", project) \
        .replace("{EMAIL}", EMAIL)

    st.subheader("Generated codemagic.yaml")
    st.download_button(
        label="Скачать",
        data=yaml,
        file_name="codemagic.yaml",
        mime="text/yaml"
    )
    st.code(yaml, language="yaml")

else:
    st.info("Fill all fields to see the result 👇")
